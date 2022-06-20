import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

N=int(input())
A=list(map(int,input().split()))

P=0
masu=[0,0,0,0]

for i in A:
    masu[0]=1
    for j in range(i):
        if masu[3-j]==1:
            P +=1
    for j in range(4-i):
        masu[3-j]=masu[3-i-j]
    for j in range(i):
        masu[j]=0
print(P)
