'''
Created on 09 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from Bio import SeqIO

def gc_Content ():
    path_to_file = '<path_to_file>'
    cg_ratio=0      #percentual value of the biggest CG ratio 
    id=""           #id of the sequence with the biggest CG ratio
    with open(path_to_file, mode='r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            C=0
            G=0
            _cg_ratio=0
            description = record.description
            sequence = record.seq
            C=sequence.count("C")
            G=sequence.count("G")
            _cg_ratio=((C+G)/len(sequence))*100
            if _cg_ratio>cg_ratio:
                cg_ratio=_cg_ratio
                id=description
    print (id)
    print (cg_ratio)
if __name__ == '__main__':
    gc_Content()