def decryptCipher(k,Cipher,mode):
    C=""
    for i in range(len(Cipher)):
        char=Cipher[i]
        if(Cipher[i].isupper()):
            C+=chr((ord(char)-k-65)%26+65)

        else:
             C+=chr((ord(char)-k-97)%26+97)

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f'The {mode}ed form is {C}\n')