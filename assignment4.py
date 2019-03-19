output_file.close()#!/usr/bin/python

import itertools
import sys

vcf = raw_input('Enter your filename:')

def vcf_parser(vcf_file):
    file = open(vcf_file, 'r')
    vcf_out = open('assign3.vcf.out', 'w')
    file_header ="ID\t\tCOORDINATE\tREF\tALT\tHG00096\t\t\t\tHG00097\t\t\t\tHG00099\t\t\t\tHG00100\t\t\t\tHG00101\t\t\t\tHG00102\t\t\t\tHG00103\t\t\t\tHG00104\t\t\t\tHG00106\t\t\t\tHG00108\t\t\t\tHG00109\n"
    vcf_out.write(file_header)
    for line in file:
        if not line.startswith ('#'):
            splitfile = line.strip()
            parts = line.split()
            for i in range(len(parts)):
               # print i, parts[i]
               file_info = (parts[2],"\tChr", parts[0], ":", parts[1],"\t", parts[3],"\t", parts[4],"\t", parts[9],"\t", parts[10],"\t", parts[11],"\t", parts[12],"\t", parts[13],"\t", parts[14],"\t", parts[15], "\t", parts[16], "\t", parts[17],"\t", parts[18],"\t", parts[19],"\n")
               finalvcf = ''.join(map(str,(file_info)))
               vcf_out.write(finalvcf)

vcf_parser(vcf)

