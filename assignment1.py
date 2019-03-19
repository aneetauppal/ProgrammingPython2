#!/usr/bin/python
#Aneeta Uppal
#2016
#auppal@uncc.edu


sequence = raw_input('Enter Your Sequence Here:') 

import re

a = re.search('ACG|GCA', sequence)
if a:
    print 'True for Part A'
else:
    print 'False for Part A'
 
b = re.search('ACG.*GCA', sequence)
if b:
    print 'True For Part B'
else:
    print 'False for Part B'

c = re.search('ACG.*(?<!GCA\Z)', sequence)
if c:
    print 'True for Part C'
else:
    print 'False for Part C'

d = re.search('(?P<seq>.)(?P=seq){5}', sequence)
if d:
    print 'True for Part D'
else:
    print 'False for Part D'


e = re.search('(^ATGC)(AT|CG|AG|CT)(A$)', sequence)

if e:
    print 'True for Part E'
else:
    print 'False for Part E'
