#!/usr/bin/python

import re 

dictionary = {'ORGANISM':[], 'GINUMBER':[], 'ACCESSION':[], 'GENE1':[], 'GENE2':[], 'ORIGIN':[],}

class Genbank(object):
    def __init__(self, filename):
        self.filename = filename
    def openfile(self):
        with open(self.filename, 'r') as GenBank:
             file = GenBank.readlines()
             file2 = ''.join(file)
             header1 = re.search('(ORIGIN.*//)',file2,flags=re.DOTALL)
             origincode = header1.group()
             dictionary['ORIGIN'].append(origincode)
             Gene1 = re.search("(gene.*[0-9]*\.\.[0-9]*.*\n.*/gene=\"[A-Z0-9]*)",file2)
             gene = Gene1.group()
             dictionary['GENE1'].append(gene)
             Gene2 = re.search("(gene.*([0-9]*\.\.[0-9])*.*\n.*/gene=\"[A-Z0-9]*)",file2)
             genes2 = Gene2.group()
             dictionary['GENE2'].append(genes2)
             for line in file:
                 if line.startswith('ACCESSION'):
                    match1 = re.search("([A-Z][0-9][0-9][0-9][0-9][0-9])",line)
                    dictionary['ACCESSION'].append(match1.group())
                 if line.startswith('VERSION'):
                    line = line.replace('VERSION     U49845.1  GI:','')
                    dictionary['GINUMBER'].append(line)
                 if line.startswith('ORGANISM'):
                    line = line.replace('ORGANISM','')
                    dictionary['ORGANISM'].append(line)
        return dictionary
    def Method_2(self):
        Dict = self.openfile()
        organism = Dict['ORGANISM']
        ginumber = Dict['GINUMBER']
        accession_num = Dict['ACCESSION']
 #       print (organism, ginumber)
        print 'ORGANISM:', organism[0],'\nGI_NUMBER:', ginumber[0],'\nACESSION_NUMBER:', accession_num[0]

    def Method_3(self):
        data = self.openfile()
        one = data['GENE1']
        two = data['GENE2']
        one = ''.join(one)
        loc1 = re.search('([0-9]*\.\.[0-9]*)',one)
        gene3 = re.search('gene=\"([A-Z0-9]*)',one)
        two = ''.join(two)
        loc2 = re.search('ment.([0-9]*\.\.[0-9]*)',two)
        gene4 = re.search('gene=\"([A-Z0-9]*)',two)
        print "Gene:",gene3.group(1),"Range:",loc1.group(), "\nGene:",gene4.group(1),"Range:",loc2.group(1)

    def Method_4(self):
        Dict = self.openfile()
        seq = Dict['ORIGIN']
        string1 = "".join(seq)
        string1 = "".join(i for i in string1 if not i.isdigit())
        string1 = string1.replace('ORIGIN','').replace('\n','').replace('\t','').replace('//','')
        sub = re.sub("[^acgt]*","",string1)
        return sub


print "Aneeta Uppal \n auppal@uncc.edu"

result = Genbank('hla.gb.txt')

print result.openfile()
result.Method_2()
result.Method_3()
print result.Method_4()

