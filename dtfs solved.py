import numpy as np

x = []
n = int(input('Size: '))
for i in range(n):
    el = float(input())
    x.append(el)
print(x)

def period(x):
    ln=len(x)
    for N in range(1, ln):
        if all(x[j]==x[j%N] for j in range(ln)):
            return N
    return ln
N=period(x)
print('Period: ', N)

def sum(k):
    sm=0
    w=(2*np.pi)/N
    for i in range(N):
        exp=np.exp(-1j*i*w*k)
        sm+=x[i]*exp
    return sm

dm=[]
for i in range(N):
    dm.append(sum(i)/N)
    print(dm[i])
    
mg=[]
ph=[]

for i in range(len(dm)):
    mg.append(((dm[i].real)**2+(dm[i].imag)**2)**0.5)     #mg.append(np.abs(dm[i]))
    ph.append(np.arctan(dm[i].imag/dm[i].real))
    
for i in range(n):
    print(mg[i])
    print(ph[i])