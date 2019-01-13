'''
Created on 13 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def read_file ():
    f = open("<path_to_file>", "r")
    i=0
    total_node=0
    edge_list=[]
    for x in f:
        if i==0:
            total_node=int(x.replace("\n", ""))
        else:
            edge_list.append(x.replace("\n", ""))
        i+=1
    return total_node, edge_list

def prepare_imput(total_node, edge_list):
    vertex_list=[[] for _ in range(total_node+1) ]
    for i in range(len(edge_list)):
        x,y=edge_list[i].split()
        x=int(x)
        y=int(y)
        vertex_list[x].append(y)
        vertex_list[y].append(x)
    return vertex_list

def count_missing_edge(vertex_list):
    missing_edge=0
    a=[]
    visited= [False for _ in range(len(vertex_list)) ]
    for i in range(1,len(vertex_list)):
        if not visited[i]:
            a.append(i)
            while len(a)>0:
                curr=a.pop(0)
                visited[curr]=True
                neighbor=vertex_list[curr]
                for j in range(len(neighbor)):
                    _next=neighbor[j]
                    if not visited[_next]:
                        a.append(_next)
            missing_edge+=1
    return missing_edge-1   
 

if __name__ == '__main__':
    a,b=read_file()
    print(count_missing_edge(prepare_imput(a,b)))
    