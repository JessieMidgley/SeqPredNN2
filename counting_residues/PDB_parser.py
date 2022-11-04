#!/usr/bin/env python3

from Bio.PDB import *
import os
import gzip

res_list = []
res_dict = {'GLY': 0, 'ALA': 0, 'CYS': 0, 'PRO': 0, 'VAL': 0,
            'ILE': 0, 'LEU': 0, 'MET': 0, 'PHE': 0, 'TRP': 0,
            'SER': 0, 'THR': 0, 'ASN': 0, 'GLN': 0, 'TYR': 0,
            'ASP': 0, 'GLU': 0, 'HIS': 0, 'LYS': 0, 'ARG': 0}
print(res_dict)

p = PDBParser(QUIET='True')
path = "/apps/PDB/pdb/zipped"

print("scanning pdb directory...")
for gz_file in os.scandir(path):
    if gz_file.name.endswith(".ent.gz"):
        fullpath = os.path.join(path, gz_file)
        file_name = gz_file.name[3:7]
        print(file_name)
        with gzip.open(fullpath, 'rt') as file:
            structure = p.get_structure(file_name, file)

            for model in structure:
                for residue in model.get_residues():
                    if residue.get_resname() in res_dict:
                        res_dict[residue.get_resname()] += 1
                print(res_dict)
                with open('res_dict.txt','w') as file:
                    for key, value in res_dict.items():
                        file.write('%s  %s\n' % (key, value))

print(res_dict)


