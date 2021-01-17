
b = [[],["", " ", " ", " "], [""," ", " ", " "], ["", " ", " ", " "]]

print("---------")
print("| {} {} {} |".format(b[1][1], b[1][2], b[1][3]))
print("| {} {} {} |".format(b[2][1], b[2][2], b[2][3]))
print("| {} {} {} |".format(b[3][1], b[3][2], b[3][3]))
print("---------")
count = 1
start = " "
while count <= 9:
    coordinate = input('Enter the coordinates: ').split()
    if coordinate[0].isnumeric() != True or coordinate[1].isnumeric() != True:
        print('You should enter numbers!')
    elif int(coordinate[0]) > 3 or int(coordinate[0]) == 0 or int(coordinate[1]) > 3 or int(coordinate[1]) == 0:
        print('Coordinates should be from 1 to 3!')

    elif b[int(coordinate[0])][int(coordinate[1])] == "X" or b[int(coordinate[0])][int(coordinate[1])] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if count % 2 != 0:    
            b[int(coordinate[0])][int(coordinate[1])]  = "X"
            count += 1
        else:
            b[int(coordinate[0])][int(coordinate[1])]  = "O"
            count += 1


        print("---------")
        print("| {} {} {} |".format(b[1][1], b[1][2], b[1][3]))
        print("| {} {} {} |".format(b[2][1], b[2][2], b[2][3]))
        print("| {} {} {} |".format(b[3][1], b[3][2], b[3][3]))
        print("---------")
    
    columb_row = [any([b[1][n] == b[2][n] == b[3][n] == "X" or b[1][n] == b[2][n] == b[3][n] == "O" or b[n][1] == b[n][2] == b[n][3] == "X" or b[1][n] == b[2][n] == b[3][n] == "O"]) for n in range(1, 4)]

    cross = [b[1][1] == b[2][2] == b[3][3] == 'X' or b[1][1] == b[2][2] == b[3][3] == 'O' or b[1][3] == b[2][2] == b[3][1] == "X" or b[1][3] == b[2][2] == b[3][1] == "O"]

    if any(columb_row):
        start = "finish"
        break
    elif any(cross):
        start = "finish"
        break
            
if start == "finish":
    print(f"{b[int(coordinate[0])][int(coordinate[1])]} wins")
else:
    print('Draw')    
