from math import log2
timer=0
def dfs(adj,u,p):
    global timer
    timer+=1
    tin[u]=timer
    up[u][0]=p
    for i in range(1,lg+1):
        up[u][i]=up[up[u][i-1]][i-1]
    for i in adj[u]:
        if i!=p:
            dfs(adj,i,u)
    timer+=1
    tout[u]=timer
def isanc(pa,u):
    return tin[pa]<=tin[u] and tout[pa]>=tout[u]
def lca(a,b):
    if isanc(a,b):
        return a;
    if isanc(b,a):
        return b
    for i in range(lg,-1,-1):
        if not(isanc(up[a][i],b)):
            a=up[a][i]
    return up[a][0]
def addedge(adj,x,y):
    adj[x].append(y)
from collections import *
n=int(input())
tin=[0]*(n+1)
tout=[0]*(n+1)
lg=int(log2(n))
up=[[0 for i in range(n+1)] for j in range(n+1)]
adj=defaultdict(list)
par=[int(i) for i in input().split()]
for i in range(n-1):
    x,y=par[i],i+1
    addedge(adj,x,y)
timer=0
dfs(adj,0,0)
group=int(input())
tree=[]
group=[int(i) for i in input().split()]
intim=tin[group[0]]
outim=tout[group[0]]
ch1=group[0];ch2=group[0]
for i in group[1:]:
    if intim>tin[i]:
        intim=tin[i]
        ch1=i
    if outim<tout[i]:
        outim=tout[i]
        ch2=i
print(lca(ch1,ch2))

