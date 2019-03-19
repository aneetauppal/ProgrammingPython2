#!/usr/bin/python 

class VcfHeader(object):
    def __init__ (self, vcf_header):
       self.header = vcf_header.replace('#','')
       self.fields = str(self.header).split()[:9]
       self.samples = str(self.header).split()[9:]

       def __str__(self):
           return('fields: ' + ' '.join(self.fields) + '\nsamples: ' + ' '.join(self.samples))

 __repr__ = __str__

class VcfRecord(object):
    def __init__(self, vcf_line):
        self.data = vcf_line
        self.chr = self.get_chr()
        self.pos = self.get_pos()
        self.id = self.get_id()
        self.ref = self.get_ref()
        self.alt = self.get_alt()
        self.qual = self.get_qual()
        self.filt = self.get_filt()
        self.formt = self.get_format()
        self.gentypes = self.get_genotypes()
        self.info = self.vcf_info()

    def get_chr(self):
        return(str(self.data).split()[0])
    def get_pos(self):
        return(str(self.data).split()[1])
    def get_id(self):
        return(str(self.data).split()[2])
    def get_ref(self):
        return(str(self.data).split()[3])
    def get_alt(self):
        return(str(self.data).split()[4])
    def get_qual(self):
        return(str(self.data).split()[5])
    def get_filt(self):
        return(str(self.data).split()[6])
    def get_format(self):
        return(str(self.data).split()[8])
    def get_gentypes(self):
        return(self.data.split()[9:])
    def vf_info(self):
        info = VCFinfo(str(self.data).split()[7])
        return(info)

class VCFinfo(object):
    def __init__ (self, vcf_info):
        for inf in vcf_info.split(';'):
            if inf.startswith('AC'):
                self.AC = inf.split('=')[-1].split(',')
        for inf in vcf_info.split(';'):
            if inf.startswith('AF'):
                self.AF = inf.split('=')[-1].split(',')
        for inf in vcf_info.split(';'):
            if inf.startswith('AN'):
                self.AN= inf.split('=')[-1].split(',')
        for inf in vcf_info.split(';'):
            if inf.startswith('NS'):
                self.NS= inf.split('=')[-1].split(',')
        for inf in vcf_info.split(';'):
            if inf.startswith('DP'):
                self.DP= inf.split('=')[-1].split(',')
        for inf in vcf_info.split(';'):
            if inf.startswith('VT'):
                self.VT= inf.split('=')[-1].split(',')
    def __str__ (self):
        return('AC='+ ','.join(self.AC) + 'AF=' + ','.join(self.AF) + 'AN=' + ','.join(self.AN) + 'NS=' + ','.join(self.DP) + 'VT=' + ','.join(self.VT))

    __repr__ = __str__ 

class VcfFile(object):
    def __init__ (self, filename):
        self.filename = filename
        self.vh, self.vrs = self.load_vcf()

    def load_vcf(self):
        vrs =[]
        with open(self.filename, 'r') as fh:
            for line in fh:
                if line.startswith('#'):
                    vh = VcfHeader(line)
                else:
                    vrs.append(VcfRecord(line))
                return(vh, vrs)
    
    __repr__ = __string__ 
