'''
Created on 04 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def findMotif(s, t):
    motif=[]
    _find(s,t,0,motif)
    return motif
def _find(s, t, start, lst):
    if s.find(t, start, len(s)) ==-1:
        return
    occ = (s.find(t, start, len(s)))+1
    lst.append(occ)
    _find(s,t,occ,lst)
if __name__ == '__main__':
    s="GTTGCGGCTGGCGGCTGTTAAGTGCGGCTGGCGGCTGGCGGCTGACTGTAGCGGCTGTTCGCGGCTGTTGCGTCGCGGCTGAAGGTGAGCGGCTGTCCTTAAGCGGCTGGCGGCTGGTTGCGGCTGGCGGCTGTACGGCGGCTGTGCGGCTGGCGGCTGGCGGCTGCGCGGCTGGCGGCTGCTAACGGCGGCTGGGCAAGAGCGGCTGTGCGGCTGCGCGGCTGCGGCGGCTGGGTGGTAACGGCGGCTGGCGGCTGGATGCGGCTGGGCGGCTGGCGGCTGTATCACTCAGCGGCTGCAGCGCACAGCGGCTGAGCGGCTGAACGCGGCTGTGCGGCTGAAAGCCTGCGGGCGGCTGGGGCGGCTGCGGCGGCTGGCGGCTGTCGCGGCTGCGCGGCTGATTGCGGCTGGACACTGCGGCTGCGCGGCTGGCGCGGCTGGTGCGGCTGGCCGAGAATGGCGGCGGCTGGGCGGCTGGCGGCTGAGTAAGGCGGCTGGCGGCTGTCATGCGGCTGGACGTGCGGCTGAGCGGCTGTACAGCGGCTGCGCGGCTGGCGGCTGAATCGCGGCTGTCTTCCTGCGGCTGGCGGCTGGCGGCTGGAGAGGCGCGGCTGGCGGCTGGGCGGCTGGCGGCTGCCGCGGCTGAGCGGCTGGCGGCTGGCGGCTGGCGGCTGTATGCGGCTGGGAGTTAGCGGCTGCGACGCGGCTGCTGGCGGCTGGCAGCGGCTGTCACTTGCGGCTGGTGTGGATGCGGCTGTAACGCGGCTGTCAGCGGCTGGCGGCTGATCTGTCAGAGCAGCCTGGCGGCTGGCGGCTGGCGGCTGCAGGCCCCGGGGTCGCGGCTGATCGAGAGCGGCTGCCCGCGGCTGGCGCGGCTGGCGAGCGGCTGCGTCGCGGCTGAGGCGGCGGCTG"
    t="GCGGCTGGC"
    for index in findMotif(s, t):
        print(index, end=" ")