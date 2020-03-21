from collections import defaultdict as dd

def inorder(tree,i):

	if i == 0:
		return

	inorder(tree,tree[i][0])
	print(i,end=' ')																
	inorder(tree,tree[i][1])

def preorder(tree,i):

	if i == 0:
		return

	print(i,end=' ')
	preorder(tree,tree[i][0])
	preorder(tree,tree[i][1])

def postorder(tree,i):

	if i == 0:
		return

	postorder(tree,tree[i][0])
	postorder(tree,tree[i][1])
	print(i,end=' ')


def main():
	n,e = map(int,input().split())
	tree = dd(list)
	for i in range(1,n+1):
		tree[i] = [0]*(2)
	for i in range(e):
		s,a,b = map(str,input().split())
		if s == 'l':
			tree[int(a)][0] = int(b)
		else:
			tree[int(a)][1] = int(b)
	print(tree)
	print('inorder --> ',end='')
	inorder(tree,1)
	print()
	print('preorder --> ',end='')
	preorder(tree,1)
	print()
	print('postorder --> ',end='')
	postorder(tree,1)

main()

