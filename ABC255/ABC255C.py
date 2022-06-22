import sys
import os
f = open('input.txt', 'r')
sys.stdin = f


X,A,D,N=map(int,input().split())

if D>=0:
    val_max=A+D*(N-1)
    val_min=A
else:
    val_max=A
    val_min=A+D*(N-1)


if X<=val_min:
    answer=abs(X-val_min)
elif X>val_max:
    answer=abs(X-val_max)
else:
    answer1 = abs((X-A) % D)
    answer2 = abs((X-A) % -D)
    answer=min(answer1,answer2)


print(answer)
