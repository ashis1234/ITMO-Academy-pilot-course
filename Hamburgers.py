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
    n = li()
    p = li()
    r1 = ii()
    need = [0]*3
    for i in s:
        if i == 'B':
            need[0] += 1
        if i == 'S':
            need[1] += 1
        if i == 'C':
            need[2] += 1

    def check(mid):
        req = [0]*3
        for i in range(3):
            req[i] = max(mid*need[i] - n[i],0)

        cost = 0
        for i in range(3):
            cost += p[i]*req[i]
        return cost <= r1


    l = 0
    r = int(1e18)
    while l <= r:
        m = l +(r-l)//2
        if check(m):
            ans = m
            l = m + 1
        else:
            r = m - 1
    print(ans) 













        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()