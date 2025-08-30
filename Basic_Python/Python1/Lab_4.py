print("*** Fun with Drawing ***")
n = int(input("Enter input : "))

size = 4 * n - 3
n = n * 2 - 1 
matrix = [['.' for _ in range(size)] for _ in range(size)]

for layer in range(n):
    char = '#' if layer % 2 == 0 else '.'
    for i in range(layer, size - layer):
        matrix[layer][i] = char
        matrix[size - layer - 1][i] = char
        matrix[i][layer] = char
        matrix[i][size - layer - 1] = char

for row in matrix:
    print(''.join(row))



