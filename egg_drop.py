#import numpy as np
import sys
print('hi')
grid = [[0 for i in range(501)] for j in range(501)]
print('hi')

for i in range(1,501):
	grid[1][i]  = i
for i in range(1,501):
    grid[i][1] = 1

#print(grid)
for i in range(2,501):
	for j in range(2,501):
		grid[i][j] = sys.maxsize
		for x in range(1,j+1):
			res = 1 + max(grid[i-1][x-1],grid[i][j-x]) #x is the intermediate floor
			if res < grid[i][j]:
				grid[i][j] = res

for _ in range(int(input())):
    floor,eggs = map(int,input().split())
    print(grid[eggs][floor])
