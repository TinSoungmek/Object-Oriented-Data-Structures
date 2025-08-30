def expo(base,n):

    if n == 0:
        return 1
    if n % 2 == 0:
        return expo(base,n/2) * expo(base,n/2)
    else:
        return base * expo(base,(n-1)/2) * expo(base,(n-1)/2)
    
base,n = input().split()
print(expo(float(base),float(n)))
