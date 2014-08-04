#/usr/bin/python
import sys
import re

def find_token(line):
	r = re.search(r"buscar_en_mapa\('([0-9a-zA-Z]+)'\)", line)
	if r:
		print r.group(1)
		exit(1)

if __name__=="__main__":
	with open(sys.argv[1]) as f:
		for line in f:
			find_token(line)
