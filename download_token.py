import urllib2

def download_token(region, filename):
	req = urllib2.Request('http://www.bencinaenlinea.cl/web2/buscador.php?region=%s' % region)
	req.add_header('Host', 'www.bencinaenlinea.cl')
	req.add_header('Connection', 'keep-alive')
	req.add_header('Cache-Control', 'max-age=0')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
	req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
	req.add_header('Accept-Language', 'en-US,en;q=0.8')
	req.add_header('Cookie', 'PHPSESSID=p43ubr5pg7fi3t50b0ksm5tfl0; __utma=180638004.342772581.1407129747.1407129747.1407129747.1; __utmc=180638004; __utmz=180638004.1407129747.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)')
	r = urllib2.urlopen(req)
	f = open(filename, "w")
	f.write(r.read())
	f.close()
	

if __name__ == "__main__":
	download_token(1, 'token.html')
