def water_flow(row, col, height):

    if row < 0 or row >= maxR or col < 0 or col >= maxC:
        return None
    
    if grid[row][col] > height or grid[row][col] == 0:
        return None
    
    height = grid[row][col]
    grid[row][col] = 0

    water_flow(row-1, col, height)  
    water_flow(row+1, col, height)  
    water_flow(row, col-1, height)  
    water_flow(row, col+1, height)

print(" *** Water Flow ***")
size, data, start = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")
maxR, maxC = map(int, size.split(","))
grid = [[int(char) for char in row] for row in data.split(",")]
start_row, start_col = map(int, start.split(","))


if maxR <= 0 or maxC <= 0:
    print("Error: Rows and columns must be between 1 and 9")
elif start_row >= maxR or start_col >= maxC:
    print("Error: Start coordinates are out of grid bounds") 
else:
    water_flow(start_row, start_col, grid[start_row][start_col])

    for row in grid:
        print("".join(str(char) for char in row))