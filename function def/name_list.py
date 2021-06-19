'''
Created on Apr 26, 2021

@author: Balu
'''

def main():
    name_list = []
    name = "start"
    while name != "":
        name = input("enter a name here, to stop just hit enter without typing")
        name_list.append(name)
    file = open("names.txt", "w")   
    name_list.sort()
    
    count = -1 
    for elem in name_list:
        count = count + 1
        print(count, elem)
        variable = str(count) + " "+ elem
        variable = str(variable)   
        file.write(variable + '\n')  
    
main()