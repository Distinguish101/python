number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])# first square bracket is row number(1 4 7 0), second is column number(1 2 3)

for row in number_grid:
    print(row)
    
for row in number_grid:
    for col in row:
        print (col)
    