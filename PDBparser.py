#!/usr/bin/python

import numpy
import Bio PDB
import math

pdb_code = "NTHI"

def degrees(rad_angle):
    if rad_angle is None:
        return None 
    angle = rad_angle * 180 / math.pi
    while angle > 180:
        angle = angle - 360
    while angle < -180:
        angle = angle + 360
    return angle

structure = Bio.PDB.PDBParser().get_structure(pdb_code, "%s.pdb" % pdb_code)
print("file loaded")

file_output = open("%s_biopython.tsv" % pdb_code, "w")
for model in structure;
    for chain in model :
        polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
        print(polypetides)
        for poly_index, poly in enumerate(polypetide) :
            phi_psi = poly.get_phi_psi_list()
            for res_index, residue in enumerate(poly) :
                phi, psi = phi_psi[res_index]
                if phi and psi:
                    file out_put.write("%s:Chain:%s:%s%i\t%f\t%f\n" % (pdb_code, str(chain.id), residue.resname, residue.id[1], degrees(phi), degrees(psi)))
file_output.close()
print("Done!")
