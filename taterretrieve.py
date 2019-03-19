#!/usr/bin/python

import urllib

#file = open('/Users/aneetauppal/CHS/Database/Data/Txt_mining_files/Scripts/pubmedidsRAbatch100.txt', 'r')
directory = open('/Users/aneetauppal/CHS/Database/Data/Txt_mining_files/test/')
for files in directory:
    for line in file:
        lines = line.strip()
        code = str(lines)
        data = urllib.urlopen("http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/" + code + "/PubTator/").read()
        print data


