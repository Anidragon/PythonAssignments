'''
Created on Mar 17, 2021

@author: Balu
'''


    
    
def mintosec(min, sec):
    minsec = min * 60
    final = minsec + sec
    return final


    
    
def main():
    name_compile("first", "middle", "last")
    name_compile("Anirudh", "Reddy", "Akula")
    print("""--------------------------------
minutes to seconds below:   
    """)
    print(mintosec(6, 59))
    print(mintosec(3, 4))

def name_compile(first, middle, last):
    initial = middle[0]
    name = print(first, initial,".", last)
    return name  

if __name__ == '__main__':
    main()