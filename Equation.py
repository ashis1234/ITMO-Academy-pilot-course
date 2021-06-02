'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
# mod=1000000007
mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')



    
def solve():

    
    s = si()
    if '.' not in s:
        c = int(s)
    else:
        c,c1 = 0,0
        cnt,f = 0 ,len(s)
        for i in range(len(s)):
            if s[i]=='.':
                f = i
                break
            x = int(s[i])
            c = c*10 + x
        for i in range(len(s)-1,f,-1):
            c1 = c1*(1/10) + int(s[i])
        c += (c1/10)
    l = 0
    r = 10**18
    while r-l > 10**-6:
        m = (l+r)/2

        x = m**2 + m**(1/2)
        if x  <= c:
            ans = m
            l = m 
        else:
            r = m 
    print(ans)










    



        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()