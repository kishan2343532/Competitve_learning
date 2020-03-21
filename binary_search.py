def binary_search(lis,i,low,high):

    while(low!=high):
        mid = low+(high-low)//2
        if lis[mid]>i:
            return binary_search(lis,i,low,mid)
        elif lis[mid]<i:
            return binary_search(lis,i,mid+1,high)
        else:
            return mid 

    return low

def main():

    lis = list(map(int,input().split()))
    element = int(input())
    print('after element ' + str(lis[binary_search(lis,element,0,len(lis)-1)-1]))

main()


