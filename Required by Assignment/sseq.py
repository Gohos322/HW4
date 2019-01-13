'''
Created on 10 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from Bio import SeqIO
def read_file ():
    # File path to your FASTA file
    path_to_file = '<path_to_file>'   # <--- substitute by your local path
    
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    sequence=[""]*2
    i=0
    with open(path_to_file, mode='r') as handle:
    
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            sequence[i] = record.seq            
            i+=1
    return sequence

def index(dna, subsequence):
    col=[0]*len(subsequence)
    x=0
    for nt in subsequence:
        i=0
        for nt1 in dna:
            i+=1
            if nt==nt1 and i>col[x-1]:
                col[x]=i
                x+=1
                break
    return col

if __name__ == '__main__':
    s= read_file()
    for i in index(s[0], s[1]):
        print(i, end= " ")