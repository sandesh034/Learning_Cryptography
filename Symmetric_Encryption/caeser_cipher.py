def encrypt(text,shift):
    encrypted_text=""
    for char in text:
        if char.isupper():
            encrypted_text+=chr((ord(char)+shift-65)%26+65)
        elif char.islower():
            encrypted_text+=chr((ord(char)+shift-97)%26+97)
        else:
            encrypted_text+=char
    
    print(encrypted_text)

encrypt('I am Sandesh Dhital',5)

def bruteforce_decrypt(text): 
    for shift in range(1,27):
        decrypted_text=""
        for char in text:
            if char.isupper():
                decrypted_text+=chr((ord(char)-shift-65)%26+65)
            elif char.islower():
                decrypted_text+=chr((ord(char)-shift-97)%26+97)
            else:
               decrypted_text+=char 
        print(f"SHIFT {shift}: {decrypted_text}")

            
bruteforce_decrypt('N fr Xfsijxm Imnyfq')
