val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]


class translator:

    def deciToRoman(self, num):
        Roman = []
        i = 0
        while num > 0:
            while num >= val[i]:   
                num -= val[i]
                Roman.append(syms[i])
            i += 1         
        return "".join(Roman) 
            

    def romanToDeci(self, s):
        s = list(s)
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and "".join(s[i:i+2]) in syms:
                index = syms.index("".join(s[i:i+2]))
                result += val[index]
                i += 2
            else:
                index = syms.index(s[i])
                result += val[index]
                i += 1
        return result

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))