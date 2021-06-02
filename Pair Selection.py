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
    a = []
    mx1 = 0
    for i in range(n):
        a.append(li())
        mx1 = max(mx1,a[-1][0])

    def check(mx):

       
        b = []
        for i in range(n):
            b.append(a[i][0] - mx*a[i][1])

        b.sort(reverse = True)
        cnt = 0
        for i in range(d):
            cnt += b[i]
        return cnt >= 0

    
    l = 0
    r = mx1
    while r - l > 10**-6:
        m = l+(r-l)/2
        
        if check(m):
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