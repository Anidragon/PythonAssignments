'''
Created on May 17, 2021

@author: Balu
'''
file = input("what file do you want to encrypt")
data = open(file, "r")
text = data.readline().rstrip('\n')

key = int(data.readline())

print(text)

def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

ex= open("output_file.txt","w")
ex.write(encrypt(text,key))
print(encrypt(text , key))