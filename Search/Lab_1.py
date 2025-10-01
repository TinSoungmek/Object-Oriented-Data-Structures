def calculate_percentile(list,tarket):
    if tarket < list[0]:
        return -1,0
    elif tarket > list[-1]:
        return 999,100
    else:
        index = binary_search(list,tarket)
        percentile = (index+1)*100/len(list)
        if percentile == 100:
            percentile = int(percentile)
        return float(index),percentile

def binary_search(list,tarket):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high)//2
        if tarket > list[mid]:
            low = mid + 1
        elif tarket < list[mid]:
            high = mid - 1
        else:
            return mid
    return (low - high) * 0.5 + high

inp,tarket = input("Enter Input : ").split("/")
inp = [float(i) for i in inp.strip().split(' ')]
index,percentile = calculate_percentile(inp,float(tarket))
print(f"\nindex      :   {index}")
print(f"percentile :   {percentile}")