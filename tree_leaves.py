from collections import defaultdict as dd

def count_leaf(tree,degree,visited,i):
	#print(degree)
	visited[i] = True
	for k in tree[i]:
		if visited[k] == False:
			degree[i]+=1
			degree[k]+=1
			count_leaf(tree,degree,visited,k)



def main():
	n,e = map(int,input().split())
	tree = dd(list)
    
	degree = [0]*(n+1)
	visited = [False]*(n+1)
	for i in range(e):
		a,b = map(int,input().split())
		tree[a].append(b)
		tree[b].append(a)
    
	count_leaf(tree,degree,visited,1)
	for i in range(len(degree)):
		if degree[i] == 1:
			print(i,end= ' ')
		

main()