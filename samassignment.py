#!/usr/bin/python

class GeneExpression():
    InstanceCount = 0

    def __init__(self):
        GeneExpression.InstanceCount +=1
#Problem 1 Implement a class method that keeps track of instances
    @classmethod
    def print_instance(cls):
        print "There are "+str(cls.InstanceCount)+" instances."
#Problem 2 method take input of gene exp file and parses out info store in the expression values of all genes
    def ImportData(self,file):
        file = open(file)
        lines=()
        dict ={}
        for line in file:
            print line
            lines = line.split()
            dict.update({lines[0]:lines[1]})
        return dict

    def ExpressionValue(self,sampleID,geneName):
        file = "/Users/samanthakaiser/Desktop/"+sampleID+".txt"
        print file
        Inst.ImportData(file)
        print[sampleID,dict[sample]]

    def Difference(self,sampleID1,sampleID2):
        file1 = "/Users/samanthakaiser/Desktop/"+sampleID1+".txt"
        file2 = "/Users/samanthakaiser/Desktop/"+sampleID2+".txt"
        dict1=Inst1.ImportData(file1)
        dict2=Inst2.ImportData(file2)
        for key in dict1:
            for key2 in dict2:
                if key2 == key:
                    diff=float(dict1[key])-float(dict2[key2])
                    print key,"%.4f" % float(dict1[key]),"%.4f" % float(dict2[key2]),"%.4f" % diff

Inst1=GeneExpression()
Inst2=GeneExpression()

print(Inst1.Difference("2670","2683"))
