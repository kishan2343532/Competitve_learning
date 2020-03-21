from collections import defaultdict as dd

def dfs(visited,tree,i):
	visited[i] = True
	print(i,end = ' ')
	for k in tree[i]:
		if visited[k] == False:
			dfs(visited,tree,k)

def dfsutil(tree):
	visited = [False]*(len(tree)+1)
	for i in tree:
		if visited[i] == False:
			dfs(visited,tree,i)
		
def main():
	dic = dd(list)
	n,e = map(int,input().split())
	for i in range(e):
		a,b = map(int,input().split())
		dic[a].append(b)
		dic[b].append(a)
	dfsutil(dic)

main()