'''
Created on Jan 26, 2021

@author: Balu
'''

num = int(input("input a positive number")) 

while 0 >= num:
    print ("you did not enter a negative number try to enter it again")    
    num = int(input(""))

factorial = 1



for i in range(1,num + 1):
    factorial = factorial*i 

print("The factorial of",num,"is",factorial)