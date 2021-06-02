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

def get1(p,x1):
    cnt = 0
    for i in p:
        cnt += abs(i-x1)
    return cnt

def get(p):

    l = 0
    r = int(1e9+5)
    c = 0
    while l <= r:
        m = l+(r-l)//2
        xl = inf
        if m > 0:
            xl = get1(p,m-1)
        x =  get1(p,m)
        xr = get1(p,m+1)
        if x <= xl and x <= xr:
            return x
        if xl >= x >= xr:
            l = m+1
        else:
            r = m-1
    


    
def solve():

    # for _ in range(ii()):

    n,k = mi()
    a = li()
    mx = max(a)
    def check(mid):


        cnt,s = 0,0
        for i in range(n):
            s += a[i]
            if s == mid:
                cnt += 1
                s = 0
            elif s > mid:
                cnt += 1
                s = a[i]
        if s != 0:
            cnt += 1
        return cnt <= k
    

    l = mx
    r = int(1e18)
    while l <= r:
        m = l +(r-l)//2
        if check(m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)
            


    






        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()