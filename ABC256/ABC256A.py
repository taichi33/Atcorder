import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

N=int(input())

print(2**N)
