'''
Created on Jun 4, 2021

@author: Balu
'''


print("lets play tic tac toe")

rowsandcolumns = [[" "," "," "],[" "," "," "],[" "," "," "]]

win = False

turncount = 0

def rowwincondition():
    for rowwin in rowsandcolumns:
        if rowwin == ["X", "X", "X"] or rowwin == ["O","O","O"]:
            win = True
            return win 
            
def diagonolwincondition1():
    first = rowsandcolumns[0]
    var = first[0]
    second = rowsandcolumns[1]
    var1 = second[1]
    third = rowsandcolumns[2]
    var2 = third[2]
    if var == "O" and var1 == "O" and var2 == "O":
        win = True
        return win
    elif var == "X" and var1 == "X" and var2 == "X":
        win = True
        return win
def diagonolwincondition2():
    first = rowsandcolumns[0]
    var = first[2]
    second = rowsandcolumns[1]
    var1 = second[1]
    third = rowsandcolumns[2]
    var2 = third[0]
    if var == "O" and var1 == "O" and var2 == "O":
        win = True
        return win
    elif var == "X" and var1 == "X" and var2 == "X":
        win = True
        return win    

def columnwincondition1():
    first = rowsandcolumns[0]
    var = first[0]
    second = rowsandcolumns[1]
    var1 = second[0]
    third = rowsandcolumns[2]
    var2 = third[0]
    if var == "O" and var1 == "O" and var2 == "O":
        win = True
        return win
    elif var == "X" and var1 == "X" and var2 == "X":
        win = True
        return win
def columnwincondition2():
    first = rowsandcolumns[0]
    var = first[1]
    second = rowsandcolumns[1]
    var1 = second[1]
    third = rowsandcolumns[2]
    var2 = third[1]
    if var == "O" and var1 == "O" and var2 == "O":
        win = True
        return win
    elif var == "X" and var1 == "X" and var2 == "X":
        win = True
        return win
def columnwincondition3():
    first = rowsandcolumns[0]
    var = first[2]
    second = rowsandcolumns[1]
    var1 = second[2]
    third = rowsandcolumns[2]
    var2 = third[2]
    if var == "O" and var1 == "O" and var2 == "O":
        win = True
        return win
    elif var == "X" and var1 == "X" and var2 == "X":
        win = True
        return win        

while win == False:
    
    turncount += 1 
    if turncount == 1 or turncount == 3 or turncount == 5 or turncount == 7 or turncount == 9:
        print("its player X's turn")
        player_marker = "X"
    elif turncount == 2 or turncount == 4 or turncount == 6 or turncount == 8:
        print("its player O's turn")
        player_marker = "O" 
    else:
        print("its a tie!")
        break       
    
   
    print("choose where to put your marker, if you put it in an already occupied spot you lose your turn!")
    whichrow = int(input("type which row you would like your marker in rows are counted from top to bottom make sure to type a number between 1 and 3!"))
   
    
    whichcolumn = int(input("type which column you would like your marker, columns are counted from left to right make sure to type a number between 1 and 3!"))
        
    print(rowsandcolumns)
    
    count = 0
    
   
    for row in rowsandcolumns:
        count = count+1
        if count == whichrow:
            columnindex = whichcolumn -1
            if row[columnindex] == "X" or row[columnindex] == "O":
                print("that square was already occupied you lose a turn!")
            else:
                    
                row[columnindex] = player_marker

        

    for rows in rowsandcolumns:
        
                   
        print(rows[0],  " | " ,rows[1], "|",rows[2])
    
        print("------------")
    if rowwincondition() == True:
        print("A player won with 3 in a row!")
        break    
    if diagonolwincondition1() == True:
        print("A player won with 3 in a diagonal!")
        break    
    if diagonolwincondition2() == True:
        print("A player won with 3 in a diagonal!")
        break    
    if columnwincondition1() == True:
        print("A player won with 3 in a column!")
        break
    if columnwincondition2() == True:
        print("A player won with 3 in a column!")
        break
    if columnwincondition3() == True:
        print("A player won with 3 in a column!")
        break
    
    
                    
                