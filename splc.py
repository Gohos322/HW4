'''
Created on 06 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def _deleteIntrons (dna, intron):
    if dna.find(intron)==-1:
        return dna
    index=dna.find(intron)
    exon=dna[0:index]
    exon+=dna[index+len(intron):]
    return _deleteIntrons(exon, intron)  

def splicinRNA(dna, intron_list):
    for intron in intron_list:
        dna=_deleteIntrons(dna, intron)
    mrna=TranscribeDNAtoRNA(dna)
    return translatingToProtein(mrna)

def TranscribeDNAtoRNA(dna):
    return dna.replace("T", "U")
    
def translatingToProtein (s):
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
        "AUG": "" ,
        "UUA": "L",
        "UUG": "L",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "AAA": "K",
        "AAG": "K",
        "AUG": "M",
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
    protein=""
    for i in range(0,(len(s)//3)):
        protein+=codon_table.get(s[(i*3):(i*3)+3])
    return protein

if __name__ == '__main__':
    dna="ATGGACGATGGATTCCACGACAGCGACGCCAAACCCGGCTCTTATACCTAACTTGGAGTT"
    dna+="GCGTGGAGTTCACAGGTGGGTTGTTCCGGTCACGCCACTTGAGACCATTTAAAGCCTGTC"
    dna+="CGAAGAGCGCCGGCGCGTACCAAGAGCTCGGCCAACAGGTCAACTGGTGCAATGGATCTT"
    dna+="GTCTGATTTATGCCTAAGATTCCTAGGCCTCAGATACGCATATGTCTATTTGTGAATCGT"
    dna+="ACCAATCGGTCTGGACGATATAGCCGCGCAAGTGGATGCAGCGGACGCGGTCAAGCCGTC"
    dna+="CAAAGAAGTACAAAAAACAGTGTTATGTCACAGTTGCTGCGTGAGCCTCAGCAAATATTG"
    dna+="CTATATCATAAGTCGCCTTGAATTTTGATAAGGTCGGCCAGGATCAGGGCGCGGCTGTAG"
    dna+="GTGCCATGGGTTTGGCTGAGTTGGCTTTACCAGTTGTAGACGGGCGTTACCCACACGAAC"
    dna+="GTCACGGCCCTCAGTATGCTGGACTGTATTCTTCATCTTCGAACTGCCCCTCACAACTGC"
    dna+="ATTCTTTATCGACACAGCTGTATAGCGCGGCTAACTACATGCGGTAATGAGGCTCGTATT"
    dna+="TGCAGAGTCAGCGTGTTACCGCTGAAACGATCTGCCAACATTTGCGATGGAGCCCAGCTT"
    dna+="GGATAACCTACGTCGTTCTCGTTTAAGCCCCGTCTGCCGCAGCACGCTATTATCGTCAAA"
    dna+="ACCAACTACCCGGTTCATATACAAGGCTCCCAGGGCTCGCTGCTGCAAACAATACGTCTA"
    dna+="TTTCGCAAGGGACCCCGTTTATGGCTTGGAGGTGAGCCGGCTGATTGGAAGGCACGTTAT"
    dna+="TGGGTATGGGTGACCCCATGACGGCGCTGCCCAGAAATGGTCAGAAGCTGTCTGAATGGA"
    dna+="ATAGGCTTACTCCTGTGGAGCGAGCACCGTCGTCACCTGACCTTCCTCAGAGTCGGGTGC"
    dna+="CGCGTATTAAGTCTGAGAAGCTTAGCAGTTCCCTTCTAA"
    intron_list=[
"CTGAAACGATCTGCCAA",
"TGAGTTGGCTTTACCAGTTGT",
"ACCTACGTCGTTCTCGTTTAAGCCCCGTCTGC",
"GCGGCTAACTACATGCGGTAATGAG",
"CGTATTAAGTCTG",
"CACCTGACCTTCCT",
"ACCTAACTTGGAGTTGCGTGGAGTT",
"AATCGTACCAATCGGTCTGGACGATATAGCCG",
"GGCCAACAGGTCAACTGGTGCAATGGATCTTGTCTGATTTATGCCT",
"AGGCACGTTATTG",
"ACTGTATTCTTCATCTTCGAAC",
"CTTGAGACCATTTAAA",
"AATACGTCTATTTCGCAAGGGACCCCGTTTATGGCTTGGAGGTG",
"AGTCGCCTTGAATTTTGATAAGGTCGG",
"TGTTATGTCACAGTTGCTGCGTGAGCCTC",
"CCCAGAAATGGTCAGAAGCTGTCTGAATGGAATAGGCTTACTCCTG",
"TCGTCAAAACCAACTACCC"
]
    print(splicinRNA(dna, intron_list))