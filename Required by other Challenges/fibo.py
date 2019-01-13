'''
Created on 10 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def fibonacci(n):
    a=[0]*n
    for i in range (0,n):
        if i == 0:
            a[i]=1
            continue
        if i == 1:
            a[i]=1
            continue
        a[i]=a[i-1]+a[i-2]
    return a[-1]
if __name__ == '__main__':
    print(fibonacci(25))