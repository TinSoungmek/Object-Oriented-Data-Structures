def hbd(age):
    num = 0
    if age%2 == 0:
        num = 20
    else:
        num = 21
    age //= 2

    return f"saimai is just {num}, in base {age}!"

year = input("Enter year : ")

print(hbd(int(year)))