#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys, re, json, urllib2, os, argparse, ConfigParser
from bs4 import BeautifulSoup
from get_token import find_token
from download_coords import download_coords
from pymongo import MongoClient

res = {}
current_station = 1
debug = False
db = None

def parse(line, region, current_station_data = {}):
    global current_station
    region = str(region)
    line = line.strip()
    if res.get(region) is None:
        res[region] = {'stations':[]}
    if line.startswith("<img src"):
        current_station_data = {}
        match = re.search("Servicio, (.+)<script>", line)
        if match:
            res[region]['name'] = match.group(1)
            match = None
        match = re.search("marker([0-9]+) = addMarker.'(-*[0-9]+\.[0-9]+)','(-*[0-9]+\.[0-9]+)','([a-zA-Z]+)'", line)
        if match:
            current_station_data["latitude"] = match.group(2)
            current_station_data["longitude"] = match.group(3)
            current_station_data["name"] = match.group(4) 
    elif line.startswith("ocultar"):
        pass
    else:
        parts = line.split("var latlng")
        #do part 1
        match = re.search("}\);infowindow([0-9]+) = addInfobox\('(.+)'\);", parts[0])
        if match:
            soup = BeautifulSoup(match.group(2))
            data = soup.find_all("table")
            prices_table = data[1]
            address_table = data[2]
            ammenities_table = data[3]
            schedule_table = data[4]
            pay_methods_table = data[5]
        
            prices = get_prices_from_table(prices_table)
            address = get_address_from_table(address_table)
            ammenities = get_ammenities_from_table(ammenities_table)
            schedule = get_schedule_from_table(schedule_table)
            pay_methods = get_pay_methods_from_table(pay_methods_table)
        
            current_station_data["prices"] = prices
            current_station_data["address"] = address
            current_station_data["ammenities"] = ammenities
            current_station_data["schedule"] = schedule
            current_station_data["payment_methods"] = pay_methods
          

        #part 2
        match = re.search("marker([0-9]+) = addMarker.'(-*[0-9]+\.[0-9]+)','(-*[0-9]+\.[0-9]+)','([a-zA-Z]+)'", parts[1])
        if match:
            current_station_data["latitude"] = match.group(2)
            current_station_data["longitude"] = match.group(3)
            current_station_data["name"] = match.group(4)
        current_station_data['id'] = current_station
        res[region]['stations'].append(current_station_data)

        current_station_data = {}
        current_station += 1

def get_prices_from_table(prices_table):
    trs = prices_table.find_all("tr")
    ret = []
    l = len(trs)
    for i in xrange(1, l):
        tds = trs[i].find_all('td')
        re = {'type': str(tds[0].text), 'price': float(tds[1].text), 'lastUpdated': str(tds[2].text)}        
        ret.append(re)
    return ret

def get_address_from_table(address_table):
    return address_table.td.text.encode("utf-8", "replace")

def get_ammenities_from_table(ammenities_table):
    counter = 0
    type_map = {0: "bathroom", 1: "pharmacy", 2: "mechanic", 3: "kiosk"}
    ret = {'bathroom': False, 'pharmacy': False, 'mechanic': False, 'kiosk': False}
    for td in ammenities_table.find_all("td"):
        if td.img is not None and td.img["src"].endswith('no.gif'):
            ret[type_map[counter]] = False
        else:
            ret[type_map[counter]] = True
        counter += 1    
    return ret

#We are assuming each station only has one schedule
def get_schedule_from_table(schedule_table):
    #First one is only the title
    trs = schedule_table.find_all("tr")[1:]
    for tr in trs:
        for td in tr.find_all("td"):
            if "24" in td.text:
                return "24 hrs"
            else:
                return td.text.encode("utf-8", "replace")

def get_pay_methods_from_table(pay_methods_table):
    #First one is only the tile
    ret = {"cash" : False, "check": False, "credit_card": False, "debit_card": False}
    tr = pay_methods_table.find_all("tr")[1:]
    #There should be only one tr
    type_map = {"./img/ico_dinero.gif": "cash", "./img/ico_cheque.gif": "check", "./img/ico_retail.gif": "credit_card", "./img/ico_card.gif": "debit_card"}
    for td in tr[0].find_all("td"):
        if td.img is None: continue
        name = type_map[td.img['src']]
        ret[name] = True
    return ret

def get_args():
    parser = argparse.ArgumentParser(description='Scrape bencinaenlinea.cl for current chilean gas/fuel prices and station locations across the country',
        epilog='Happy sniffing!')
    parser.add_argument('-d', '--debug', action='store_true', help='Run in debug mode')
    parser.add_argument('-r', '--regions', choices=[x for x in xrange(1, 15)], help='Number of regions to process (starting from 1)', default=14, type=int)
    parser.add_argument('-c', '--config', help='Route to config file', default='sniffer.cfg', type=str)
    return parser.parse_args()

def get_config(args):
    global db
    config = ConfigParser.ConfigParser()
    config.read(args.config)

    mongo = MongoClient(config.get('DB', 'host'), int(config.get('DB', 'port')))
    db = mongo[config.get('DB', 'db')]


if __name__ == "__main__":
    args = get_args()
    get_config(args)
    debug = args.debug
    token = find_token('token.html')
    for region in xrange(1, args.regions + 1):
        download_coords(token, region, 'coords.html')
        with open('coords.html') as f:
            for line in f:
                parse(line, region, {})

    db.data.insert(res)
    
    if debug is True:
        os.remove('coords.html')
        os.remove('token.html')
        #print json.dumps(res)
