'''
Created on 12 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def read_file ():
    f = open("<path_to_file>", "r")
    i=0
    n=""
    m=""
    a=""
    k=""
    for x in f:
        if i==0:
            n=x.replace("\n", "")
        if i==1:
            m=x.replace("\n", "")
        if i==2:
            a=x.replace("\n", "")
        if i==3:
            k=x.replace("\n", "")
        i+=1
    return n,m,a,k

def create_dict(a):
    dict={}
    lst=a.split()
    for i in lst:
        dict[i] = lst.index(i)+1 
    return dict


if __name__ == '__main__':
    n,m,a,k=read_file()
    dict=create_dict(a)
    result=""
    for i in k.split():
        if dict.get(i):
            result=result+str(dict.get(i)) + " "
        else:
            result=result+"-1 "
    print(result)
            
            
            