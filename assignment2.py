#!/usr/bin/python3

aminoacid = {'Ala':['GCU','GCC','GCA','GCG'],
                'Arg':['CGG','CGC','CGA','CGG','AGA','AGG'],
                'Asn':['AAU','AAC'],
                'Asp':['GAU', 'GAC'],
                'Cys':['UCU', 'UGC'],
                'Gln':['CAA', 'CAG'],
                'Glu':['GAA', 'GAG'],
                'Gly':['GGU', 'GGC', 'GGA','GGG'],
                'His':['CAU', 'CAC'],
                'Ile':['AUU', 'AUC', 'AUA'],
                'Leu':['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
                'Lys':['AAA', 'AAG'],
                'Met':['AUG'],
                'Phe':['UUU', 'UUC'],
                'Pro':['CCG', 'CCU', 'CCA', 'CCC'],
                'Ser':['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                'Thr':['ACU', 'ACC', 'ACA', 'ACG'],
                'Try':['UGG'],
                'Tyr':['UAU','UAC'],
                'Val':['GUU', 'GUC', 'GUA', 'GUG'],
                'Stop':['UAA', 'UGA'],'Start':['AUG'],}

for key in sorted(aminoacid.keys(), key = lambda k:k. lower()):
    print(key,':', aminoacid[key], 'The number of Codons present:', (len(aminoacid[key])))


