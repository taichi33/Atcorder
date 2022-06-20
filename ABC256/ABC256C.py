import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

h1,h2,h3,w1,w2,w3=map(int,input().split())
h=[h1,h2,h3]
w=[w1,w2,w3]

board=[0,0,0,0,0,0,0,0,0]
sol=0

def search(k,h,w):
    i=k//3
    j=k%3
    val_h=h[i]-sum(board[3*i:3*i+3])
    val_w=w[j]-(board[j]+board[j+3]+board[j+6])
    if j==2 and i ==2:
        a= val_h
        if a == val_w and a>=1:
            global sol
            sol+=1
            return
        else:
            return
    if j==2:
        a= val_h
        if a <= val_w and a>=1:
            board[k]=a
            search(k+1,h,w)
            board[k]=0
    elif i==2:
        a= val_w
        if a <= val_h and a>=1:
            board[k]=a
            search(k+1,h,w)
            board[k]=0
    else:
        for a in range(1,val_w):
            if a < val_h:
                board[k]=a
                search(k+1,h,w)
                board[k]=0
search(0,h,w)
print(sol)
