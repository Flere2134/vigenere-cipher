#vigenere cipher function
#def vigenere_cipher(plaintext, keyword):
#convert plaintext to uppercase and no spaces
    #plaintext = plaintext.upper().replace(' ', '')
#convert keyword to uppercase
    #keyword = keyword.upper()
##convert keyword to number
#variable for ciphered text
#convert plaintext to number, get modulo value of whole message using keyword
#return value of ciphered text

#ask user for input of plaintext and keyword
plaintext = input('Write the message you wanted to cipher using Vigenere Cipher: ')
keyword = input('Enter the keyword: ')
#encryption of plaintext
#print output

plaintext = plaintext.upper().replace(' ', '')
keyword = keyword.upper()

print(plaintext, keyword)
