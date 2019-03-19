#!/usr/bin/python

class geneexpression():
    instancecount = 0

    def __init__(self):
        geneexpression.instancecount +=1
    @classmethod
    def printinstance(cls):
        print ('There are' +str(cls.instancecount)+ 'instances.')

    def openfile(self, file):
        file = open(file)
        lines = ()
        dictionary = {}
        for line in firstfile:
            lines  = line.split()     
            dictionary.update({[lines[0]]:lines[1]})
            print (line) 
            return dictionary 

    def method_2(self, ID, name):
        key = "/Users/aneetauppal/Graduate_MS/Spring_Semester_2016/Programming\ 2/Python\ Scripts/TCGA/" +ID+".txt"
        print (key) 
        inst.importdata(key)
        print ([ID,dictionary[sample]])

    def method_3(self, ID1, ID2):
        file1 = "/Users/aneetauppal/Graduate_MS/Spring_Semester_2016/Programming\ 2/Python\ Scripts/TCGA/" +ID1+".txt"
        file2 = "/Users/aneetauppal/Graduate_MS/Spring_Semester_2016/Programming\ 2/Python\ Scripts/TCGA/" +ID2+".txt"
        dictionary1 = f1.openfile(file1)
        dictionary2 = f2.openfile(file2)
        for key2 in dictionary1:
            for key3 in dictionary2:
                if key3 == key2:
                     Totaldiff =float(dictionary1[key2])-float(dictionary2[key3])
                     output = open('expressionvalue.out','w')
                     output.write(key2, "%.4f" % float(dictionary1[key2]), "%.4f" % float(dictionary2[key3]), "%.4f" % Totaldiff)
                     print ("%.4f" % float(dictionary1[key2]), "%.4f" % float(dictionary2[key3]), "%.4f" % Totaldiff)

f1 = geneexpression()
f2 = geneexpression()

print(f1.method_3("2670","2683"))
