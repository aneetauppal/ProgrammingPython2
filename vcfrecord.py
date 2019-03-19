#!/usr/bin/python

class VcfRecord:
    def __init__(self, vcf_line):
        self.data =(vcf_line)

    def get_chr(self):
        return (str(self.data).split()([0])
