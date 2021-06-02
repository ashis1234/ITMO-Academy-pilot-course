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

    
    
    
    n = ii()
    a = li()
    a.sort()
    for i in range(ii()):
        x,y = mi()
        if x > a[-1] or y < a[0]:
            print(0,end=" ")
            continue

        ans1,l,r = 0,0,n-1
        while(l <= r):
            m = l +(r-l)//2
            if a[m] >= x:
                ans1 = m+1
                r = m-1
            else:
                l = m+1

        ans2,l,r = -1,0,n-1
        while(l <= r):
            m = l +(r-l)//2
            if a[m] <= y:
                ans2 = m+1
                l = m+1
            else:
                r = m-1

        print(ans2-ans1+1,end=" ")


        






        













    



        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()