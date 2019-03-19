#!/usr/bin/python

from __future__ import print_function
import string


class Basesequence(object):
    def __init__(self, seqstring):
        self.seqstring = seqstring

    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in 'TCAGtcag'}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        with open(self.seqstring, 'r') as sequence:
            for line in sequence:
                if not line.startswith('>'):
                    sequences = line.strip()
                if sequences invalid:
                    raise Exception(
                    'Warning sequence contains errors: ' +
                    str(invalid))

class DNAsequence(Basesequence):
    TranslationTable = string.maketrans('TCAGtcag', 'AGUCaguc')

    def gc_content(self):
        seq = self.get_sequence.upper()
        return (seq.count('G') + seq.count('C'))/len(seq)

    @classmethod
    def invalid_chars(self, seqstring):
        return {char for char in seq if char not in 'TCAGtcag'}

    def __init__(self, seqstring):
        invalid = self.invalid_chars(seqstring)
        if invalid:
            raise Exception(
                'Warning sequence contains errors: ' +
                str(invalid))

        super(DNASequence, self).__init__(seqstring)

    def transcribe(self):
        return RNASequence(
        self.get_sequence().translate(self.TranslationTable))


class RNAsequence(Basesequence):
    codontable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                  "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
                  "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
                  "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
                  "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                  "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                  "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                  "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                  "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                  "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                  "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                  "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                  "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                  "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                  "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                  "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
                  }

    @classmethod
    def translate_codon(self, codon):
        return self.codontable[codon.upper()]

    def __init__ (self, seqstring):
        super(RNAsequence, self).__init__(seqstring)

    def translate(self, frame=1):
        return ''.join([self.translate_codon(self.get_sequence()[n:n+3])
                        for n in
                        range(frame-1,
                              len(self.get_sequence()) -
                              (len(self.get_sequence()) - (frame-1)) % 3,
                              3)])

rnaseq = Basesequence('/Users/aneetauppal/Graduate_MS/Spring_Semester_2016/Programming\ 2/Python\ Scripts/hw6/hw6c.fa')

print(rnaseq1.RNAsequence())
print(rnaseq1.DNAsequence())
print(rnaseq1.Basesequence())

for n in range(1,4):
    print('Frame', n, rnaseq1.translate(n), sep = ' ')