'''
Created on Jan 26, 2021

@author: Balu
'''
choice = input("do you want to know how many numbers are in your text? (enter yes or no)")
if choice == "no":
    print("okay see you later")
while choice == "yes":
    
     

    s = input("enter your text letters and numbers")
    digit = 0
    
    for c in s:
        numbers = sum(c.isdigit()for c in s)
    
        print("there are",numbers,"numbers in your text")
    choice = input("do you want to go again?(yes or no)")