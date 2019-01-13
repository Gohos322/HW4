'''
Created on 07 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
# Import parts of Biopython
from Bio import SeqIO

def read_file ():
    # File path to your FASTA file
    path_to_file = '<path_to_file>'   # <--- substitute by your local path
    dna=[]
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    with open(path_to_file, mode='r') as handle:
    
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            dna.append(str(record.seq))
    return dna


def pDistance(dna):
    distance_matrix=[[0.0 for _ in range(len(dna))] for _ in range(len(dna)) ]
    for i in range(len(dna)):
        diff=0
        first=dna[i]
        for j in range(len(dna)):
            if i == j:
                continue
            last=dna[j]
            for x in range(len(first)):
                if first[x] != last[x]:
                    diff+=1
            distance_matrix[i][j]=diff/len(first)
            diff=0
    return distance_matrix
    
if __name__ == '__main__':
    matrix=pDistance(read_file())
    for x in matrix:
        for y in matrix[matrix.index(x)]:
            print(y, end=" ")
        print ("")
    
    
    
    
    