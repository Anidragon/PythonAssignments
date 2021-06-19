'''
Created on Feb 24, 2021

@author: Balu
'''

def main():
    initials("Kavitha", "Akula")
    initials("Anirudh", "Akula")
    initials("Shirisha", "Rapole")


def initials(firstname, lastname):
    initial1 = firstname[0] 
    initial2 = lastname[0]
    final = print(initial1,".",initial2)
    return final

main()