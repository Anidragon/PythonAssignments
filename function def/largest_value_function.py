'''
Created on Mar 1, 2021

@author: Balu
'''


def main():
    print(large_value(23,56,78))
    print(large_value(794,45,68))
    print(large_value(56,45,90))
def large_value(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
        
    elif num2 > num1 and num2 > num3:
        return num2
        
    elif num3 > num1 and num3 > num2:
        return num3
    
        
main()  
 