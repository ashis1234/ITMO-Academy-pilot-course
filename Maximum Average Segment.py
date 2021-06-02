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

    # for _ in range(ii()):

    n,d = mi()
    a = li()

    def check(mx):

       
        pre = [0]*n

        for i in range(n):
            if i > 0:
                pre[i] += pre[i-1]
            pre[i] += (a[i] - mx)

        mnx = [[ pre[0] , 0]]

        for i in range(1,n):
            x = mnx[-1]
            if pre[i] < mnx[-1][0]:
                x = [pre[i] , i ]
            mnx.append(x)
        
        for i in range(n):
            x = i - d 
            if (i+1) >= d and  pre[i] >= 0:
                return [1,1,i+1]
            if x < 0:
                continue
            if mnx[x][0] <= pre[i]:
                return [ 1 , mnx[x][1]+2 , i+1] 

        return [0,0,0]


    l = 0
    r = max(a)
    ans1 = 0
    while r - l > 10**-6:
        m = l+(r-l)/2
        p = check(m)
        if p[0] and ans1 <= m:
            ans1 = m
            ans = p[1:]
            l = m
        else:
            r = m
    print(*ans)

    






        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()