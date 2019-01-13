'''
Created on 11 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
from itertools import permutations
def permutation(n):
    perm_list=[]
    numbers=[]
    for num in range(1, n+1):
        numbers.append(num)
    for perm in permutations(numbers):
        perm_list.append(perm)
    print (len(perm_list))
    a=[[0]]*len(perm_list)
    for i in range(len(perm_list)):
        a[i]=str(perm_list[i])
    for i in a:
        print(i.replace("("," ").replace(")", " ").replace(","," ").replace(" ", "", 1))
    
        
if __name__ == '__main__':
    permutation(3)