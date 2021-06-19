'''
Created on Mar 19, 2021

@author: Balu
'''

def main():
    first = test(12,5)
    second = quiz(4,3)
    third = answer(first,second)
    print(third)
    
def test(a,b):
    answer = a-b
    answer += 1
    return answer
def quiz(a,b):
    answer = a + b
    return answer
def answer(a,b):
    answer = test(a,b) + quiz(a,b)
    return answer
main()