#vigenere cipher function
def vigenere_cipher(plaintext, keyword):
#convert plaintext to uppercase and no spaces
    plaintext = plaintext.upper().replace(' ', '')
#convert keyword to uppercase
    keyword = keyword.upper()
#checking if input are in the alphabet
    if not plaintext.isalpha() or not keyword.isalpha():
        print('Invalid input! Please enter letters only and preferably in uppercase and no spaces')
        return '' 
#convert keyword to number
    keyword_convert_to_num = [ord(keyword[i]) - 65 for i in range(len(keyword))]
#variable for ciphered text
    ciphered_text = ''
#convert plaintext to number, get modulo value of whole message using keyword
    for i in range(len(plaintext)):
        modulo_value = (ord(plaintext[i]) - 65 + keyword_convert_to_num[i % len(keyword)]) % 26
        ciphered_text += chr(modulo_value + 65)
#return value of ciphered text
    return ciphered_text

#try again function
def try_again():
    again = None
#asking for user input and checking it
    while again is None:
        answer = input('Would you like to try and use the VIGENERE CIPHER again? ')
#if yes program runs again
        if answer in ["Y", "YES", "yes", "Yes", "y"]:
            again = True
            continue
#if no prints a message
        elif answer in ["N", "NO", "no", "No", "n"]:
            again = False
            print('Thank you for using the Vigenere Cipher!')
            break
#if answer is invalid asks user again
        else:
            print('Try answering either YES or NO')

#while loop for the vigenere cipher and try again function
while True:
#ask user for input of plaintext and keyword
    plaintext = input('Write the message you wanted to cipher using Vigenere Cipher: ')
    keyword = input('Enter the keyword: ')
#encryption of plaintext
    ciphered_text = vigenere_cipher(plaintext, keyword)
#print output
    print(f'\033[96m{ciphered_text}')
#call try again function
    try_again()
    if not again:
        break

#MESSAGE: THISISTHELASTTASKHOORDAY
#KEYWORD: KNIGHTS