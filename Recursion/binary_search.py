def BS(low,high,value):
    mid = (low+high) // 2
    if high < low:
        return "Not Found"
    if lis[mid] == value:
        return mid
    elif lis[mid] < value:
        return BS(mid+1,high,value)
    else:
        return BS(low,mid-1,value)


lis = input().split(", ")
lis = list(map(int,lis))
value = int(input())
print(BS(0,len(lis)-1,value))