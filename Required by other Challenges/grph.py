'''
Created on 09 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from Bio import SeqIO

def vertex ():
    path_to_file = '<path_to_file>'
    vertexes=[]
    with open(path_to_file, mode='r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            description = record.description
            sequence = record.seq
            vertexes+=[[description, str(sequence)]]
    return vertexes

def adjacency_List(vertexes):
    vertexes_clone=vertexes[::]
    adjacency_list=[]
    for vertex in vertexes:
        suffix=vertex[1][-3:]
        for vertex_clone in vertexes_clone:
            if vertexes.index(vertex)==vertexes_clone.index(vertex_clone):
                continue
            prefix=vertex_clone[1][:3]
            if suffix==prefix:
                adjacency_list+=[[vertex[0], vertex_clone[0]]]
    return adjacency_list
if __name__ == '__main__':
    for a in adjacency_List(vertex()):
        print(a[0]+" " + a[1])