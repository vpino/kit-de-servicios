import fileinput
import re

for line in fileinput.input():
	#line = re.sub('ns +IN +A +192\.168\.1\.53','bar', line.rstrip())
	#line = re.sub('?=(a in ns .)\1MAS\1MASMAS|','MATCH', line.rstrip()
	line = re.match("(?('kj')A|B)",line.rstrip())
	#print(line.group(1) or line.group(2))
	print(line)