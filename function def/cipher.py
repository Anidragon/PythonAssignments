'''
Created on May 17, 2021

@author: Balu
'''

    
#Task 1       
       
alphabet = "abcdefghijklmnopqrstuvwxyz"
#defines the original alphabet
encrypted_alphabet = ""

key = 3
#hard-codes the key

file = input("what file would you like to encrypt")
file_name = open(file, 'r')
#asks for the file to encrypt, and opens in read mode
filename_ENC = file[:-4] + "_ENC" + file[-4:]
#splices the file to add an "_ENC"
for letter in alphabet:
    index = alphabet.index(letter)+key
    if len(alphabet) - 1 < index:
        index = index % 26
    encrypted_alphabet += alphabet[index]
#creates the Encrypted alphabet    

ENC = ""
for line in file_name:
    #sorts through each line
    for character in line:
        #sorts through each letter
        if character.lower() in alphabet:
            new_index = alphabet.index(character.lower())
            encrypted_letter = encrypted_alphabet[new_index]
            #finds if the character is a letter or not 
            if character.isupper():
                #finds if the letter is a capitol or not
                encrypted_letter = encrypted_letter.upper()
            ENC = ENC + encrypted_letter
            #writes the letter to ENC  
        else:
            ENC = ENC + character
            #tells the computer to write the same character if it is not a letter   
    open_ENC = open(filename_ENC, "w")
    open_ENC.write(ENC)
    #writes the encrypted text to a _ENC.txt file
            
    
