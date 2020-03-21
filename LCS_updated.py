from collections import defaultdict as dd
def resolve(parent_tree,grid,a,b,s1,s2,root):

    if (grid[a][b] == 0):
        return
    if s1[b-1] == s2[a-1]:
        parent_tree[root].append(s1[b-1])
        resolve(parent_tree,grid,a-1,b-1,s1,s2,s2[b-1])
    if grid[a][b-1] == grid[a][b]:
        resolve(parent_tree,grid,a,b-1,s1,s2,root)
    if grid[a-1][b] == grid[a][b]:
        resolve(parent_tree,grid,a-1,b,s1,s2,root)


n,m = map(int,input().split())

grid = [[0 for i in range(n+1)] for j in range(m+1)]

s1 = list(map(str,input().split()))
s2 = list(map(str,input().split()))

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            grid[i][j] = grid[i-1][j-1] + 1
        else:
            grid[i][j] = max(grid[i-1][j],grid[i][j-1])
#print(grid)
length = grid[m][n]
a = m
b = n
parent_tree = dd(list)

resolve(parent_tree,grid,a,b,s1,s2,0)
print(parent_tree)
    


