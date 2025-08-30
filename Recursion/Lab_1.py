def Fac(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Fac(num-1)

num = int(input("Enter Number : "))
print(f"{num}! = {Fac(num)}")