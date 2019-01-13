'''
Created on 07 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
# Import parts of Biopython
from Bio import SeqIO

def read_file (file_name):
    # File path to your FASTA file
    path_to_file = '<path_to_file>'+file_name   # <--- substitute by your local path
    
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    matrix = []
    with open(path_to_file, mode='r') as handle:
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            identifier = record.id
            description = record.description
            sequence = record.seq
            dna=[]
            for i in sequence:
                dna.append(i)
            matrix.append(dna)
    return matrix

def consensus(matrix):
    row,col = len(matrix), len(matrix[0])
    #create an empty list with a number of rows equal to col, and a number of columns equal to row
    profile_matrix=[[None for _ in range(col)] for _ in range(4) ]    
    for i in range(col):
        A=0
        C=0
        G=0
        T=0
        for j in range(row):
            A+= 1 if matrix[j][i] == "A" else 0
            C+= 1 if matrix[j][i] == "C" else 0
            G+= 1 if matrix[j][i] == "G" else 0
            T+= 1 if matrix[j][i] == "T" else 0
        profile_matrix[0][i] = A
        profile_matrix[1][i] = C
        profile_matrix[2][i] = G
        profile_matrix[3][i] = T

    nts={
        0: "A",
        1: "C",
        2: "G",
        3: "T"
    }
    
    _consensus=""
    
    for i in range(col):
        max=0
        nt=""
        for j in range(4):
            if profile_matrix[j][i] > max:
                max = profile_matrix[j][i]
                nt=nts.get(j)
        _consensus+=nt
    print(_consensus)
    
            
    for i in profile_matrix:
        _pm=nts.get(profile_matrix.index(i)) + ": "
        for j in range(len(i)):
            _pm += str(i[j]) + " "
        print(_pm)

if __name__ == '__main__':
    consensus(read_file("rosalind_cons.txt"))