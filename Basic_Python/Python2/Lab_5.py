def bon(w):
    for i in range (len(w)):
        for j in range (len(w)):
            if i == j :
                continue
            elif w[i] == w[j]:
                return ord(w[i]) - 96
            
secretCode = input("Enter secret code : ")
print(bon(secretCode)*4)
