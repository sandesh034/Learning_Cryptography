import random

def check_prime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n,2):
        if n%i==0:
            return False
    return True

def generate_prime():
    n=random.randint(2,100)
    if(check_prime(n)):
        return n
    else:
        return generate_prime()

    
def calculate_gcd(n1,n2):
    if n2==0:
        return n1
    else:
        return calculate_gcd(n2,n1%n2)
    

def generate_keys():
    p=generate_prime()
    q=generate_prime()
    n=p*q
    m=(p-1)*(q-1)
    e=0
    d=0

    for i in range(2,m):
        if(calculate_gcd(i,m)==1):
            e=i
            break
    for i in range(2,m):
        if(m*i+1)%e ==0:
            d=(m*i+1)//e
            break

    return n,e,d

n, e, d = generate_keys()
encrypt_key = (e, n)
decrypt_key = (d, n)

def encrypt(message, encrypt_key):
    e, n = encrypt_key
    cipher = [pow(ord(char), e, n) for char in message]   # pow(a,b,c) = a^b % c
    return cipher

def decrypt(cipher, decrypt_key):
    d, n = decrypt_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return "".join(message)

encrypted_message = encrypt("Sandesh is a student", encrypt_key)
print("Encrypted Message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, decrypt_key)
print("Decrypted Message:", decrypted_message)






    



    
