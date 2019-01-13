'''
Created on 11 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from Bio import SeqIO

def get_dna (file_name):
    # File path to your FASTA file
    path_to_file = '<path_to_file>' + file_name  # <--- substitute by your local path
    
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    dna=""
    
    with open(path_to_file, mode='r') as handle:
    
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            dna = str(record.seq)
            
    return dna

def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def compute_rna(dna):

    _rnas=[]
    _rnas.append(dna.replace("T", "U"))
    _rnas.append(reverse_complement(dna).replace("T", "U"))
    return _rnas

def get_protein(rna, offset):
    codon_table= {
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGA": "R",
        "AGG": "R",
        "AAU": "N",
        "AAC": "N",
        "GAU": "D",
        "GAC": "D",
        "UGU": "C",
        "UGC": "C",
        "CAA": "Q",
        "CAG": "Q",
        "GAA": "E",
        "GAG": "E",
        "GGU": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
        "CAU": "H",
        "CAC": "H",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "UUA": "L", 
        "UUG": "L",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "AAA": "K",
        "AAG": "K",
        "AUG": "M",     #start
        "UUU": "F",
        "UUC": "F",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "AGU": "S",
        "AGC": "S",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "UGG": "W",
        "UAU": "Y",
        "UAC": "Y",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "UAG": "",
        "UGA": "",
        "UAA": "",        
        }
    _found_start=False
    proteins= []
    _proteins= []
    for i in range(0,(len(rna)//3)):
        codon=rna[(i*3+offset):((i*3+offset))+3]
        amin=codon_table.get(codon)
        if amin == "M":
            _proteins.append("")
            _found_start=True
                
        if amin == "":
            _found_start=False
        
        if _found_start==False:
            if len(_proteins) > 0:   
                for i in _proteins:
                    proteins.append(i)
            _proteins = []
            continue
        
        if _found_start == True and amin != None:
            for i in _proteins:
                x = _proteins.index(i)
                i+=amin
                _proteins[x] = i
            
    return proteins
    
    
if __name__ == '__main__':
    rnas = compute_rna(get_dna("rosalind_orf.txt"))
    protein_list=[]
    for rna in rnas:
        protein_list = protein_list + get_protein(rna, 0)
        protein_list = protein_list + get_protein(rna, 1)
        protein_list = protein_list + get_protein(rna, 2)
    print("\n".join(set(protein_list)))
        
        