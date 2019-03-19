#!/usr/bin/python3 

#Aneeta Uppal Assignment 3, programming 2

import sys
import glob

VCF_name = input('Enter your file to parse here:')

def create_header(VCF_name):
  header1 = 'ID\t' 
 # header2 = 'Coordinate\t'
  #header3 = 'Ref\t'
  #header4 = 'Alt\t'
  #header5 = 'Genotype\t'

  if len(VCF_name) == 0:
    print('Nothing is here')
    sys.exit()

  for line in VCF_name:
    sample_id = line.split('-')[0]
    header1 = header1 + sample_id + '\t'
  header1 = header1.rstrip()
  return header1
    
def parse_info(VCF_name):
  for IDs

  gene_data = {}
  gene_ids = []
  for counter, VCF_name in enumerate(VCF_name):
    
