import urllib2, urllib

def download_coords(token, region, filename):
	params = {'region' : region, 'comuna':'', 'token': token, 'combustible': '', 'bandera': ''}
	req = urllib2.Request('http://www.bencinaenlinea.cl/web2/mapa_mostrarresultados.php', urllib.urlencode(params))
	req.add_header('Host', 'www.bencinaenlinea.cl')
	req.add_header('Connection', 'keep-alive')
	req.add_header('Content-Length', '77')
	req.add_header('Cache-Control', 'max-age=0')
	req.add_header('Accept', 'text/javascript, text/html, application/xml, text/xml, */*')
	req.add_header('X-Prototype-Version', '1.7')
	req.add_header('Origin', 'http://www.bencinaenlinea.cl')
	req.add_header('X-Requested-With', 'XMLHttpRequest')
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
	req.add_header('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
	req.add_header('Referer', 'http://www.bencinaenlinea.cl/web2/buscador.php?region=%s' % region)
	req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
	req.add_header('Accept-Language', 'en-US,en;q=0.8')
	req.add_header('Cookie', 'PHPSESSID=p43ubr5pg7fi3t50b0ksm5tfl0; __utma=180638004.342772581.1407129747.1407129747.1407129747.1; __utmb=180638004.2.10.1407129747; __utmc=180638004; __utmz=180638004.1407129747.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)')

	r = urllib2.urlopen(req)
	f = open(filename, 'w')
	f.write(r.read())
	f.close()

if __name__ == "__main__":
	download_coords('d655bc674b4b02a8a35fc2df36be61ff',1, "coords.html")
