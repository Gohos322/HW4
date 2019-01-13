'''
Created on 12 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def read_file ():
    f = open("<path_to_file>", "r")
    i=0
    n=""
    m=""
    for x in f:
        if i==0:
            n=x.replace("\n", "")
        if i==1:
            m=x.replace("\n", "")
        i+=1
    return n,m

if __name__ == '__main__':
    n,a=read_file()
    b=[]
    for x in a.split():
        b.append(int(x))
    b.sort()
    for i in b:
        print(i, end=" ")
    