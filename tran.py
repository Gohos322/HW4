'''
Created on 04 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def transitionToTransvertion(s1, s2):
    transition=0
    transvertion=0
    for nt1, nt2 in zip(s1, s2):
        if nt1 != nt2:
            if (nt1 == "A" and nt2 == "G") or (nt1=="G" and nt2== "A") or (nt1=="C" and nt2== "T") or (nt1=="T" and nt2== "C"):
                transition+=1
            else:
                transvertion+=1
            
    return transition/transvertion
if __name__ == '__main__':
    s1="GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
    s2="TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
    print(transitionToTransvertion(s1, s2))