import sys, os, re
import download_token


def find_token(file_name):
	if not os.path.isfile(file_name):
		download_token.download_token(1, file_name)
	with open(file_name) as f:
		for line in f:
			r = re.search(r"buscar_en_mapa\('([0-9a-zA-Z]+)'\)", line)
			if r:
				return r.group(1)

if __name__=="__main__":
	find_token(sys.argv[1])
