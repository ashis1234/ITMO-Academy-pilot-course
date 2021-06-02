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

    
    k = ii()
    n = ii()
    a = []
    for i in range(n):
        a.append(ii())

    def fun(mid):
        cnt = 0
        s = 0
        for i in a:
            if i >=mid:
                cnt += 1
            else:
                s += i
        cnt += (s//mid)
        return cnt >= k

    l = 0
    r = int(1e18)
    while l <= r:
        m = l+(r-l)//2
        if fun(m):
            ans = m
            l = m+1
        else:
            r = m-1
    print(ans)
    






        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()