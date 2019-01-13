'''
Created on 12 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from Bio import SeqIO

def read_file ():
    # File path to your FASTA file
    path_to_file = '<path_to_file>'   # <--- substitute by your local path

    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    with open(path_to_file, mode='r') as handle:
    
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            sequence = record.seq
    return str(sequence)
    
def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def find_Palindrome (s):
    result=[]
    for i in range(0, len(s)):
        for j in range(4, 13):
            if i+j > len(s):
                continue
            sub1=s[i:i+j]
            sub2=reverse_complement(sub1)
            if sub1 == sub2:
                result.append([i+1,len(sub1)])
    print("\n".join(' '.join(str(z) for z in i) for i in result))
if __name__ == '__main__':
    find_Palindrome(read_file())