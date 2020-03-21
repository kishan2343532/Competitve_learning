from collections import defaultdict as dd
from collections import deque as deq


def bfs(tree,visited,i,que):
	print(i,end=' ')
	que.append(i)
	visited[i] = True
	while(len(que)!=0):		
		for k in tree[que[0]]:
			if visited[k] == False:
				visited[k] = True
				print(k,end=' ')
				que.append(k)
		que.popleft()

def bfsutil(tree):

	visited = [False]*(len(tree)+1)
	que = deq()
	for i in tree:
		if visited[i] == False:
			bfs(tree,visited,i,que)


def main():
	n,e = map(int,input().split())
	dic = dd(list)
	for i in range(e):
		a,b = map(int,input().split())
		dic[a].append(b)
		dic[b].append(a)
	bfsutil(dic)

main()
