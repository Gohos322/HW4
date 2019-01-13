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

def find_lcsq(x, y):
    matrix=[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1) ]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                matrix[i+1][j+1] = matrix[i][j] +1
            else:
                matrix[i+1][j+1]= max(matrix[i+1][j], matrix[i][j+1])
            
    lcsq=""
    i, j = len(x), len(y)
    while i !=0 and j !=0:
        if matrix[i][j] == matrix[i-1][j]:
            i -= 1
        elif matrix[i][j] == matrix[i][j-1]:
            j -= 1
        else:
            lcsq += x[i-1]
            i-=1
            j-=1
    print(lcsq[::-1])
        
if __name__ == '__main__':
    z = read_file()
    find_lcsq(z[0], z[1])
    
    