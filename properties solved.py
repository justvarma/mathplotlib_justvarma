import numpy as np

x=[]
n=int(input('Enter Size: '))
print('Enter value: ')
for i in range(n):
    ip=float(input())
    x.append(ip)
print(x)

def period(x):
    ln=len(x)
    for N in range(1, ln):
        if all(x[j]==x[j%N] for j in range(ln)):
            return N
    return ln
N=period(x)
print('Period: ', N)

def dtfs(n, l):
    sm=0
    w=(2*np.pi)/N
    for i in range(N):
        exp=np.exp(-1j*i*w*n)
        sm+=l[i]*exp
    return sm

dm=[]
print('\nOrginal Period: ')
for i in range(N):
    dm.append(dtfs(i, x)/N)
    print(dm[i])

ts=int(input('\nTime shifting: '))
x1=[0]*n
for i in range(N):
    x1[i]=x[i-ts]

dm1=[]
print('\nWithout Property: ')
for k in range(N):
    dm1.append(dtfs(k, x1)/N)
    print(dm1[k])
     
dm2=[]
w=(2*np.pi)/N
print('\nWith Property: ')
for k in range(N):
    dm2.append(dm[k]*np.exp(-1j*k*w*ts))
    print(dm2[k])