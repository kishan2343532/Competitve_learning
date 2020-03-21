
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

n = int(input())
lis = []
for i in range(n):
    a = int(input())
    lis.append(a)

temp = []
parent = [-1]*len(lis)
for i in range(len(lis)):
    if len(temp) == 0:
        temp.append(lis[i])
    else:
        if temp[-1] < lis[i]:
            temp.append(lis[i])
            #parent[i] = temp[-2]
        elif temp[-1] > lis[i]:
            index = binary_search(temp,lis[i],0,len(temp)-1)
            temp[index] = i

        else:
            continue
print(len(temp))
#print(parent)


