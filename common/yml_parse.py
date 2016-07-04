import yaml

def parseYaml(path, filename):

	f = open(path + str(filename) )
	# use safe_load instead load
	dataMap = yaml.safe_load(f)

	f.close()

	return dataMap