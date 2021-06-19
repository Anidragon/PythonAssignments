'''
Created on Mar 8, 2021

@author: Balu
'''

def main():    
    space1 = 'x'    
    space2 = 'o'    
    space3 = 'o'    
    space4 = 'o'    
    space5 = 'x'    
    space6 = 'o'    
    space7 = 'x'    
    space8 = 'x'    
    space9 = 'o'
    print(checkwin(space9, space3, space4))
    print(checkwin(space1, space5, space8))
    print(checkwin(space1, space3, space4))
def checkwin(s1, s2, s3):
    if s1 == "o" and s2 == "o" and s3 == "o":
        result = "O"
    if s1 == "x" and s2 == "x" and s3 == "x":
        result = "X"   
    if s1 != s2 or s2 != s3 or s1 != s3:
        result = "N" 
    return result
main()       
    
    