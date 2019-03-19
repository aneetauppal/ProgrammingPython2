#usr/bin/python
import re

inputfile = raw_input("Provide VCF File name:")

def extract(filename):
	data = open(filename, 'r')
	outputfile = open("lab03.vcf.out", 'w')
	columnheaders = "ID\t\tCOORDINATE\tREF\tALT\tHG00096\t\t\t\tHG00097\t\t\t\tHG00099\t\t\t\tHG00100\t\t\t\tHG00101\t\t\t\tHG00102\t\t\t\tHG00103\t\t\t\tHG00104\t\t\t\tHG00106\t\t\t\tHG00108\t\t\t\tHG00109\n"
	outputfile.write(columnheaders)
	for line in data:
		if not line.startswith ('#'):
			separatecolumns = line.split("\t")
			
			datarow = separatecolumns[2],"\tChr", separatecolumns[0], ":", separatecolumns[1],"\t", separatecolumns[3],"\t", separatecolumns[4],"\t", separatecolumns[9],"\t", separatecolumns[10],"\t", separatecolumns[11],"\t", separatecolumns[12],"\t", separatecolumns[13],"\t", separatecolumns[14],"\t", separatecolumns[15], "\t", separatecolumns[16], "\t", separatecolumns[17],"\t", separatecolumns[18],"\t", separatecolumns[19],"\n"
			mappeddatarow = ''.join(map(str,(datarow)))
			outputfile.write(mappeddatarow)
				
extract(inputfile)