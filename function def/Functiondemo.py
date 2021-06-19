'''
Created on Feb 23, 2021

@author: Balu
'''
def main():
    print(average3(67, 48, 67))
    print(average3(45, 78, 98))
    print(average3(56, 67, 90))


def average3(num, num1, num2):
    total = num + num1 + num2
    avg = total/3 
    return avg

main()