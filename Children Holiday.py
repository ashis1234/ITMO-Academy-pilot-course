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

    
    m,n= mi()
    op = []
    for i in range(n):
        op.append(li())

    def fun(ti):

        cnt = 0

        for i in range(n):
            t,z,y = op[i][0],op[i][1],op[i][2]
            rem = ti

            while(rem > 0 and rem//t > z):
                cnt += z
                rem -= (t*z)
                rem -= y
            if rem > 0:
                cnt += (rem//t)

        return cnt >= m


    


    l,r = 0,1000000
    while(l <= r):
        mid = l + (r-l)//2
        if fun(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1


    print(ans)
    cnt = 0 
    for i in range(n):
        t,z,y = op[i][0],op[i][1],op[i][2]
        rem = ans
        c = 0
        while(rem > 0 and rem//t > z):
            c += z
            rem -= (t*z)
            rem -= y
        if rem > 0:
            c += (rem//t)
        c = min(c,m)
        print(c,end=" ")
        m -= c    

    
    
    


    



        
if __name__ =="__main__":

    
    if path.exists('input.txt'):
        sys.stdin=open('input.txt', 'r')
        sys.stdout=open('output.txt','w')
    else:
        input=sys.stdin.readline
    solve()