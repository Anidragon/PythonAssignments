'''
Created on Mar 8, 2021

@author: Balu
'''
def main():
    print(letter_count("supercalifragilisticexpealidocius","e"))
    print(vowel_count("booaertu"))
def letter_count(string, letter):
    count = 0
  
    for i in string: 
        if i == letter: 
            count = count + 1
    return count

def vowel_count(string2):
    count = 0
  
    for j in string2: 
        if (j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U'):
            count = count+1
    return count
main()
