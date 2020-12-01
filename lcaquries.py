#LCA code with O(nlogn) for preprocess and O(1) for queries Euler walk
from collections import *
adj=defaultdict(list)
p2 = [1];sz=15;
log=defaultdict(int)
FAI=defaultdict(lambda:-1)
lev=defaultdict(int)
dp=[[-1 for i in range(18)] for j in range(sz)]
euler=[];depth=[]
def sparse(n):
	for i in range(1,n):
		dp[i-1][0] = i-1 if depth[i]>depth[i-1] else i
	for l in range(1,15):
		for i in range(n):
			if dp[i][l-1]!=-1 and dp[i+p2[l-1]][l-1]!=-1:
				dp[i][l] = dp[i+p2[l-1]][l-1] if depth[dp[i][l-1]]>depth[dp[i+p2[l-1]][l-1]] else dp[i][l-1]
			else:
				break
def query(l,r):
	d = r-l;
	dx = log[d];
	if (l==r):	return l;
	if depth[dp[l][dx]]>depth[dp[r+p2[dx]][dx]]:
		return dp[r-p2[dx]][dx]
	else:
		return dp[l][dx]
def preprocees():
	for i in range(1,20):
		p2.append(p2[i-1]*2)
	val=1;ptr2=0
	for i in range(1,sz):
		log[i]=ptr2-1
		if i==val:	val*=2;log[i]=ptr2;ptr2+=1
def dfs(cur,pre,dep):
	if FAI[cur]==-1: FAI[cur]=len(euler);
	lev[cur]=dep
	euler.append(cur)
	for x in adj[cur]:
		if x!=pre:
			dfs(x,cur,dep+1)
			euler.append(cur)
def addEdge(u,v):
	adj[u].append(v)
	adj[v].append(u)
def lca(u,v):
	if u==v:	return u
	if FAI[u]>FAI[v]:	u,v=v,u
	return euler[query(FAI[u], FAI[v])];
addEdge(1,2);
addEdge(1,3);
addEdge(2,4);
addEdge(2,5);
addEdge(2,6);
addEdge(3,7);
addEdge(3,8);
preprocees()
dfs(1,0,0);
depth = [lev[i] for i in euler]
sparse(len(depth))
print(lca(6,7))
print(lca(6,4))
#DP Array
# 0 0 0 0 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 1 1 1 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 3 3 3 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 3 3 3 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 5 5 8 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 5 5 8 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 7 8 8 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 8 8 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 8 8 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 9 9 9 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 11 11 14 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 11 11 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 13 14 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# 14 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
# -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
