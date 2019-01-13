'''
Created on 11 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)
'''
def mortalFibonacciRabbits(n,m):
    rabbits = []                                                               
    months = 0                                                                     
    while months < n:  
        if months == 0:
            rabbits.append(1)
            months +=1
            continue
        if months == 1:
            rabbits.append(1)
            months+=1
            continue                                                            
        if months < m:          #before the m-th month, the rabbits follow the classic Fibonacci sequence
            rabbits.append(rabbits[-1]+rabbits[-2])
        elif months == m:       #the m-th month the very first rabbits couple will die
            rabbits.append(rabbits[-1]+rabbits[-2] -1)
        else:                   #after that point the relation that describe the rabbits population's growth is the following
            rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-(m+1)])
        months +=1
    return rabbits[-1]
if __name__ == '__main__':
    print(mortalFibonacciRabbits(35, 29))