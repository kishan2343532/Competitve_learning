import math
import sys
input = sys.stdin.readline
vax = pow(2,32)-1

'''some points to consider

1) pos = tells you at which level you are at example 0 signifies root
2) low,high = tells you the range of the level you are at, 
   ex a pos 0 with low,high - (0,9) means it is telling ans on range [0,3] of original array index
3) qlow,qhigh = simply the query range of index of original array 
   [0,3] means tell me the ans for range array[0:3]
'''

def build_tree(seg_tree,input_array,low,high,pos):
    # leaf node 
    if low == high:
        seg_tree[pos] = input_array[low]
        return

    mid = (low+high)//2
    left =  build_tree(seg_tree,input_array,low,mid,2*pos+1)
    right = build_tree(seg_tree,input_array,mid+1,high,2*pos+2)

    seg_tree[pos] = min(seg_tree[2*pos+1],seg_tree[2*pos+2])

def query(seg_tree,lazy_array,qlow,qhigh,low,high,pos): 
    if lazy_array[pos]!=vax:
        seg_tree[pos]&=lazy_array[pos]
        if low!=high:
            lazy_array[2*pos+1]&= lazy_array[pos]
            lazy_array[2*pos+2]&= lazy_array[pos]
        lazy_array[pos] = vax   
        
        
    #total overlap
    if (qlow <= low and qhigh >= high):
        return seg_tree[pos]
    #no overlap
    if(qlow > high or qhigh < low):
        return sys.maxsize

    #partial overlap
    mid = (low + high)//2

    return min(query(seg_tree,lazy_array,qlow,qhigh,low,mid,2*pos+1),query(seg_tree,lazy_array,qlow,qhigh,mid+1,high,2*pos+2))

def lazy_update(seg_tree,lazy_array,qlow,qhigh,low,high,change,pos):
    if low>high:
        return
    
    # pehle make sure root pe jo pressure hai use settled and transfer the burden to child ,
    # phir child ka apan agle recursion mein dekh lenge 
    if lazy_array[pos]!=vax:
        seg_tree[pos]&=lazy_array[pos]
        if low!=high:
            lazy_array[2*pos+1]&= lazy_array[pos]
            lazy_array[2*pos+2]&= lazy_array[pos]
        lazy_array[pos] = vax
         
    #non-overlapping conditions
    if (qhigh<low) or (qlow>high):
        return
    
    #complete overlap
    if (high<=qhigh) and (low>=qlow):
        seg_tree[pos]&=change
        if low!=high:
            lazy_array[2*pos+1]&= change
            lazy_array[2*pos+2]&= change
        return
    
    #partial overlap
    mid = (low+high)//2
    lazy_update(seg_tree,lazy_array,qlow,qhigh,low,mid,change,2*pos+1)
    lazy_update(seg_tree,lazy_array,qlow,qhigh,mid+1,high,change,2*pos+2)

    seg_tree[pos] = min(seg_tree[2*pos+1],seg_tree[2*pos+2])

def update(seg_tree,qlow,qhigh,low,high,change,pos):

    if qhigh<low or qlow>high:
        return
    if low == high:
        seg_tree[pos]+=change
        return
    else:
        mid = (low+high)//2
        update(seg_tree,qlow,qhigh,low,mid,change,2*pos+1)
        update(seg_tree,qlow,qhigh,mid+1,high,change,2*pos+2)
        seg_tree[pos] = min(seg_tree[2*pos+1],seg_tree[2*pos+2])

def main():

    n,queries = map(int,input().split())
    input_array = list(map(int,input().split()))
    seg_tree = [0]*(pow(2,math.ceil(math.log2(len(input_array)))+1))
    lazy_array = [vax]*len(seg_tree)
    build_tree(seg_tree,input_array,0,len(input_array)-1,0)
    #print(seg_tree)

    for i in range(queries):
        inp = list(map(int,input().split()))
        #print(inp)
        if inp[0] == 0:
            sys.stdout.write(str(query(seg_tree,lazy_array,inp[1]-1,inp[2]-1,0,len(input_array)-1,0))+'\n')
            #print(seg_tree)

        else:
            lazy_update(seg_tree,lazy_array,inp[1]-1,inp[2]-1,0,len(input_array)-1,inp[3],0)
            #print(lazy_array)
            #print(seg_tree)


main()













