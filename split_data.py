import sys, re

res = {}

#r = re.compile("}\);infowindow[0-9]+ = addInfobox\(([^\)]+)\)")
def parse(line, region):
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
		#part 2
		match = re.search("marker([0-9]+) = addMarker.'(-*[0-9]+\.[0-9]+)','(-*[0-9]+\.[0-9]+)','([a-zA-Z]+)'", parts[1])
		if match:
                        if res[region].get(match.group(1)) is None:
                                res[region][match.group(1)] = {}
                        res[region][match.group(1)]["latitude"] = match.group(2)
                        res[region][match.group(1)]["longitude"] = match.group(3)
                        res[region][match.group(1)]["name"] = match.group(4)

if __name__ == "__main__":
	num_lines = 1
	for line in open(sys.argv[1]):
		parse(line, sys.argv[2])
		num_lines += 1
	print res
