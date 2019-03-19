input_file = open('parsedtater.txt')
for lines in input_file:
	line = lines.split()
	print line[3]
