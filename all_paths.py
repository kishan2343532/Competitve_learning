from collections import defaultdict as dd

def like_dfs(tree,visited,stack,i):
	visited[i] = True
	stack.append(i)

	for k in tree[i]:
		if visited[k] == False:
			like_dfs(tree,visited,stack,k)
	if len(tree[i]) == 1 and i!=1:
		print(stack)
	stack.pop()

def main():
	n,e = map(int,input().split())
	tree = dd(list)
	for i in range(e):
		a,b = map(int,input().split())
		tree[a].append(b)
		tree[b].append(a)
	visited = [False]*(n+1)
	for i in range(1,n+1):
		stack = []
		if visited[i] == False:
			like_dfs(tree,visited,stack,i)
main()



