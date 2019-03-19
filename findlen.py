#!/usr/bin/python

import itertools
import sys

vcf = raw_input('Enter your filename:')

def vcf_parser(vcf_file):
    file = open(vcf_file, 'r')
    for line in file:
#        if not line.startswith ('#'):
        splitfile = line.strip()
        parts = line.split()
        print(parts)
   #         for i in range(len(parts)):
    #           print i, parts[i]     

vcf_parser(vcf)
