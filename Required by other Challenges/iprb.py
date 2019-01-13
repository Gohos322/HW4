'''
Created on 09 gen 2019

@author: Lorenzo Guenci (Student ID 1532651)'''

def compute_probability(k,m,n):
    
    #===========================================================================
    # Input Parameters: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
    #   - k individuals are homozygous dominant for a factor, 
    #   - m are heterozygous,  
    #   - n are homozygous recessive.
    #===========================================================================
    
    tot = float(k+m+n)
    
    k_first=(k/tot)*((k-1)/(tot-1)) + (k/tot)*(m/(tot-1)) + (k/tot)*(n/(tot-1))
    
    m_first=(m/tot)*(k/(tot-1)) + (m/tot)*((m-1)/(tot-1))*0.75 + (m/tot)*(n/(tot-1))*0.5
    
    n_first=(n/tot)*(k/(tot-1)) + (n/tot)*(m/(tot-1))*0.5 #+ (n/tot)*((n-1)/(tot-1))*0
    
    return k_first + m_first + n_first
    
if __name__ == '__main__':

    print(compute_probability(25,29,16))
    