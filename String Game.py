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
    n = len(s)
    t = si()
    a = li()
    
    def find(b,x):

        l = 0
        ans = -1
        r = len(b) - 1
        while l <= r:
            m = l+(r-l)//2
            if b[m] >= x:
                ans = b[m]
                r = m-1
            else:
                l = m+1
        return ans

    def check(x):
        st = [[] for i in range(26)]
        m = [0]*n

        for i in range(x+1):
            m[a[i] - 1] = 1

        for i in range(n):
            if m[i]:
                continue
            st[bo(s[i])].append(i)
        cur = 0
        for i in t:
            b = st[bo(i)]
            x = find(b,cur)
            if x == -1:
                return 0
            cur = x+1
        return 1


    

    l = 0
    r = n-1
    ans = -1
    while(l <= r):
        mid = l + (r-l)//2
        if check(mid):
            ans = mid
            l = mid + 1 
        else:
            r = mid - 1
    print(ans+1)

    

    

    
    
    


    



        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()