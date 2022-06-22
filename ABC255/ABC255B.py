import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

from decimal import *
getcontext().prec = 18

N,K=map(int,input().split())
A=list(map(int,input().split()))
xy=[map(int,input().split()) for _ in range(N)]
x,y=[list(i) for i in zip(*xy)]


R=0
for i in range(N):
    Light_min=100000000000
    for j in A:
        Light=(x[j-1]-x[i])**2+(y[j-1]-y[i])**2
        if Light_min>Light:
            Light_min=Light
    if R< Light_min:
        R=Light_min

R=Decimal(R).sqrt()
print(R)
