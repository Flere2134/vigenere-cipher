#vigenere cipher function
def vigenere_cipher(plaintext, keyword):
#convert plaintext to uppercase and no spaces
    plaintext = plaintext.upper().replace(' ', '')
#convert keyword to uppercase
    keyword = keyword.upper()
##convert keyword to number
    keyword_convert_to_num = [ord(keyword[i]) - 65 for i in range(len(keyword))]
#variable for ciphered text
    ciphered_text = ''
#convert plaintext to number, get modulo value of whole message using keyword
    for i in range(len(plaintext)):
        modulo_value = (ord(plaintext[i]) - 65 + keyword_convert_to_num[i % len(keyword)]) % 26
        ciphered_text += chr(modulo_value + 65)
#return value of ciphered text
    return ciphered_text
#ask user for input of plaintext and keyword
plaintext = input('Write the message you wanted to cipher using Vigenere Cipher: ')
keyword = input('Enter the keyword: ')
#encryption of plaintext
#print output
