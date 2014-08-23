#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys, re, json, urllib2, os
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
from get_token import find_token
from download_coords import download_coords

res = {}

def parse(line, region):
	region = str(region)
	line = line.strip()
	if res.get(region) is None:
		res[region] = {}
	if line.startswith("<img src"):
		match = re.search("marker([0-9]+) = addMarker.'(-*[0-9]+\.[0-9]+)','(-*[0-9]+\.[0-9]+)','([a-zA-Z]+)'", line)
		if match:
			if res[region].get(match.group(1)) is None:
				res[region][match.group(1)] = {}
			res[region][match.group(1)]["latitude"] = match.group(2)
			res[region][match.group(1)]["longitude"] = match.group(3)
			res[region][match.group(1)]["name"] = match.group(4) 
	elif line.startswith("ocultar"):
		pass
	else:
		parts = line.split("var latlng")
		#do part 1
		match = re.search("}\);infowindow([0-9]+) = addInfobox\('(.+)'\);", parts[0])
		if match:
			station = match.group(1)
			if res[region].get(station) is None:
				res[region][station] = {}
			try:
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
			
				res[region][station]["prices"] = prices
				res[region][station]["address"] = address
				res[region][station]["ammenities"] = ammenities
				res[region][station]["schedule"] = schedule
				res[region][station]["payment_methods"] = pay_methods
			except:
                                sys.stderr.write(line)
                                pass			

		#part 2
		match = re.search("marker([0-9]+) = addMarker.'(-*[0-9]+\.[0-9]+)','(-*[0-9]+\.[0-9]+)','([a-zA-Z]+)'", parts[1])
		if match:
                        if res[region].get(match.group(1)) is None:
                                res[region][match.group(1)] = {}
                        res[region][match.group(1)]["latitude"] = match.group(2)
                        res[region][match.group(1)]["longitude"] = match.group(3)
                        res[region][match.group(1)]["name"] = match.group(4)

def get_prices_from_table(prices_table):
	trs = prices_table.find_all("tr")
	ret = []
	for tr in trs:
		tds = tr.find_all("td")
		re = {'type': str(tds[0].text)}
		p = Popen(["./get_price_from_url.sh " + tds[1].img["src"][:-1]], stdout=PIPE, shell=True)

		price = p.communicate()
		price = price[0].strip()
		re['price'] = price[1:]
		ret.append(re)
	return ret

def get_address_from_table(address_table):
	return str(address_table.td.text.encode("utf-8", "ignore"))

def get_ammenities_from_table(ammenities_table):
	counter = 0
	type_map = {0: "bathroom", 1: "pharmacy", 2: "mechanic", 3: "kiosk"}
	ret = {}
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
				return str(td.text)

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

if __name__ == "__main__":
	token = find_token('token.html')
	for region in xrange(1, 16):
		download_coords(token, region, 'coords.html')
		with open('coords.html') as f:
			for line in f:
				parse(line, region)
	
	os.remove('coords.html')
	os.remove('token.html')
	print json.dumps(res)
