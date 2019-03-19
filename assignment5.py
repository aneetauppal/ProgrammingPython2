#!/usr/bin/python

class Genbank_input(object):
    def __init__ (self, gen_info):
        self.data = gen_info
        self.locus = self.get_loc()
        self.definition = self.get_defin()
        self.accession = self.get_access()
        self.version = self.get_version()
        self.keywords = self.get_keywords()
        self.source = self.get_source()
        self.organism = self.get_organism()
        self.reference = self.get_ref()
        self.authors = self.get_authors()
        self.title = self.get_title()
        self.comment = self.comments()
        self.features = self.get_features()
        self.origin = self.get_origin()



    def get_loc(self):
        return(str(self.data).split()[0])
    def get_defin(self):
        return(str(self.data).split()[1])
    def get_access(self):
        return(str(self.data).split()[2])
    def get_version(self):
        return(str(self.data).split()[3])
    def get_keywords(self):
        return(str(self.data).split()[4])
    def get_source(self):
        return(str(self.data).split()[5])
    def get_organism(self):
        return(str(self.data).split()[6:10])
    def get_reference(self):
        return(str(self.data).split()[12])
    def get_authors(self):
        return(str(self.data).split()[13])
    def get_title(self):
        return(str(self.data).split()[14])
    def get_comments(self):
        return(str(self.data).split()[20:21])
    def get_features(self):
        return(str(self.data).split()[24:])
    def get_origin(self):
        return(str(self.data).split()[0])
