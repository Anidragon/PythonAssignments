'''
Created on May 21, 2021

@author: Balu
'''
phonebook = {"boom" : "1234567890", "snap" : "0987654321", "crackle" : "0908070605", "pop" : "1944619",}

name = ""
while name != "done":

    name = input("enter a name or 'done' to exit")

    if name in phonebook:
        print("this is the number for that name:","\n", name,":", "    ",phonebook[name])
    elif name == "done":
        print("thanks")    
    else:
        print("that name is not on the list you may try again")

