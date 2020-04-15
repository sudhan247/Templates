from math import log2
timer=0
def dfs(adj,u,p):
    global timer
    timer+=1
    tin[u]=timer
    eu[timer]=u
    up[u][0]=p
    for i in range(1,lg+1):
        up[u][i]=up[up[u][i-1]][i-1]
    for i in adj[u]:
        if i!=p:
            dfs(adj,i,u)
    timer+=1
    tout[u]=timer
    eu[timer]=u
def isanc(pa,u):
    return tin[pa]<=tin[u] and tout[pa]>=tout[u]
def lca(a,b):
    if isanc(a,b):
        return a;
    if isanc(b,a):
        return b
    for i in range(lg,0,-1):
        if not(isanc(up[a][i],b)):
            a=up[a][i]
    return up[a][0]
def addedge(adj,x,y):
    adj[x].append(y)
    adj[y].append(x)
from collections import *
n=int(input())
tin=[0]*(n+1)
tout=[0]*(n+1)
eu=[0]*(2*n+1)
lg=int(log2(n))
up=[[0 for i in range(lg+1)] for j in range(n+1)]
adj=defaultdict(list)
for _ in range(n-1):
    x,y=map(int,input().split())
    addedge(adj,x,y)
timer=0
dfs(adj,1,1)

