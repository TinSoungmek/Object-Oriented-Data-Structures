def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

def find_total_weight(purify, weight):
    if purify == 1:
        return weight
    
    ck = fibo(purify - 1)

    total_ab = 2 * weight + 1 - ck

    if total_ab < 2:
        return -1
    
    a = total_ab // 2
    b = total_ab - a
    
    return find_total_weight(purify - 1, a) + find_total_weight(purify - 1, b)

purify, weight = input("Purity and Weight needed: ").split()
result = find_total_weight(int(purify), int(weight))
print(f"Total weight of used minerals with Purity 1 : {result}")