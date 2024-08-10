#This program demonstrates Caesar Cipher Algorithm in simple manner.
from encrypt import encryptPlaintext
from decrypt import decryptCipher

def displayCaesar():
    mode=input("Type encrypt for encryption or decrypt for decryption as required.Press 0 for exit.?  ")

    if(mode=='encrypt'):
        k=int(input("Enter the shift value? "))
        plainText=input('Enter the plaintext? ')
        encryptPlaintext(k,plainText,mode)
        displayCaesar()

    elif(mode=='decrypt'):
        k=int(input("Enter the shift value? "))
        Cipher=input('Enter the Cipher text to decrypt? ')
        decryptCipher(k,Cipher,mode)
        displayCaesar()

    elif(mode=='0'):
        exit()
    else:
        print("Please enter required supported commands.")
        exit()


if __name__=="__main__":

    displayCaesar()
   