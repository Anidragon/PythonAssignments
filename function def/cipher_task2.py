'''
Created on May 18, 2021

@author: Balu
'''
#Task 2
alphabet = "abcdefghijklmnopqrstuvwxyz"       
ENC_DEC = input("would you like to encrypt or decrypt your file?")
key = int(input("what is the key that was used/ what is the key you would like to use"))
file = input("what file would you like to encrypt/decrypt")

if ENC_DEC == "decrypt":

    def decryptfunction(key, file):       
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        #defines the original alphabet
        encrypted_alphabet = ""
        
        key = -key
        
        
        file_name = open(file, 'r')
        #asks for the file to encrypt, and opens in read mode
        filename_ENC = file[:-8] + "_DEC" + file[-4:]
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
    decryptfunction(key, file)
    filename_ENC = file[:-8] + "_DEC" + file[-4:]    
    print("result was printed to :",filename_ENC,)

if ENC_DEC == "encrypt":
    def encryptfunction(key, file):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        #defines the original alphabet
        encrypted_alphabet = ""
        
       
        
        
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
    encryptfunction(key, file)
    filename_ENC = file[:-4] + "_ENC" + file[-4:]    
    print("result was printed to :",filename_ENC,)



    
   
 
         