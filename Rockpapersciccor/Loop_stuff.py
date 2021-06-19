'''
Created on Feb 3, 2021

@author: Balu
'''

rows = 5
for i in range(0, rows):
    for j in range(0,1):
        print("******", end=" ")
    print()
    

rows = 4
for i in range(0, rows):
    for j in range(0,1):
        print("***", end=" ")
    print()
    
    
rows = 4
for i in range(0, rows):
    for j in range(0, i + 3):
        print("*", end=" ")

    print()

extra = 1   
rows = 4
for i in range(0, rows):
    for j in range(0, 2 * i + 1):
        print("*", end=" ")
       
        
        
    print()   


rows = 4
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()     
   
    
count = 5
rows = 12
total = 1
print("*")
for i in range(2, rows):
    for j in range(2, i + 1):
        if (i%2 == 0):
            total = total + count
        elif (i%2 == 1):
            total = total - count 
        print("*"*abs(total))        
        break    
    count = count-1
print("*")


    