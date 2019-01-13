'''
Created on 07 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
# Import parts of Biopython
from Bio import SeqIO

def read_file ():
    # File path to your FASTA file
    path_to_file = 'C:\\Users\\Lorenzo\\Downloads\\rosalind_splc (1).txt'   # <--- substitute by your local path
    
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs
    # or there will be any other problem)
    with open(path_to_file, mode='r') as handle:
    
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
    
            # Extract individual parts of the FASTA record
            identifier = record.id
            description = record.description
            sequence = record.seq
    
            # Example: adapt to extract features you are interested in
            print('----------------------------------------------------------')
            print('Processing the record {}:'.format(identifier))
            print('Its description is: \n{}'.format(description))
            amount_of_nucleotides = len(sequence)
            print('Its sequence contains {} nucleotides.'.format(amount_of_nucleotides))
if __name__ == '__main__':
   read_file()