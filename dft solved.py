# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:34:13 2024

@author: adity
"""

import numpy as np

n=np.arange(0, 6)

def impulse(n):
    if n==0:
        return 1
    else:
        return 0
    
def t_shift(n, t):
    n1=n-t
    n2=impulse(n1)
    return n2

x = [impulse(i) + 2*t_shift(i, 1) + 5*t_shift(i, 2) + 6*t_shift(i, 3) for i in n]

ch=1
while(ch!=0):
    N=int(input('\nValue of N: '))
    w=(2*np.pi/N)
    
    def sum(k):
        sm=0
        for i in range(N):
            exp=np.exp(-1j*w*i*k)
            sm+=x[i]*exp
        return sm
    
    dm=[]
    print('\nFourier Coefficiants: ')
    for k in range(N):
        dm.append(sum(k)/N)
        print(dm[k])
        
    dm1=[]
    print('\nDFT Coefficiants: ')
    for k in range(N):
        dm1.append(sum(k))
        print(dm1[k])
        
    def inv_sum(k):
        sm=0
        for i in range(N):
            exp=np.exp(1j*w*i*k)
            sm+=x[i]*exp
        return sm
    
    dm2=[]
    print('\nIDFT Coefficiants: ')
    for k in range(N):
        dm2.append(inv_sum(k)/N)
        print(dm2[k])
        
    ch=int(input("\nIf you want to exit press 0   :"))