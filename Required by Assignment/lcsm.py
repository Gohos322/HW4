'''
Created on 12 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''

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

def find_lcsm(s):
    
    result=[]
    sample=s[0]
        
    for idx1 in range(1, len(s)):
        row1=s[idx1]
        for idx2 in range(0, len(sample)):
            for n in range(2, len(sample)+1):                
                if idx2+n > len(sample):
                    continue
                sub1=sample[idx2:idx2+n]
                if not sub1 in row1:
                    break
                result.append(sub1)
    subs=set(result)
    x=0
    common_sub=[]
    for i in subs:
        for idx1 in range(0, len(s)):
            row1=s[idx1]
            if i in row1:
                x+=1
        if x==len(s):
            common_sub.append(i)
        x=0
    print (max(common_sub, key=len))
                        
if __name__ == '__main__':
    find_lcsm(read_file())