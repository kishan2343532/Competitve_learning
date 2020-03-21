#import numpy as np
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
ans = []
while length!=0:
    if s2[a-1] == s1[b-1]:
        ans.append(s2[a-1])
        a = a-1
        b = b-1       
        length-=1
    else:
        if grid[a][b-1] >= grid[a-1][b]:
            b = b-1
        else:
            a = a-1
for i in range(m+1):
    for j in range(n+1):
        print(grid[i][j],end=' ')
    print()
for i in range(len(ans)-1,-1,-1):
    print(ans[i],end=' ')
    
    


