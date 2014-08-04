import sys
import re

def parse(lines):
	all_lines = []
	for l in lines:
		l.replace('\n', '')
		l.replace('\r', '')
		l.replace('\t', '')
		l = l.strip()
		all_lines.append(l)
	all_lines = "".join(all_lines)
	print all_lines

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		parse(f.readlines())
			
