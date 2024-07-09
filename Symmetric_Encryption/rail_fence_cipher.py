def encrypt(text, depth):
    if depth == 1:
        return text
    
    text = text.replace(' ', '')
    text = text.upper()
    fence = [[] for _ in range(depth)]
    rail = 0
    sign = 1

    for char in text:
        fence[rail].append(char)
        rail += sign
        
        if rail == depth - 1 or rail == 0:
            sign = -sign

    encrypted_text = ''.join(''.join(rail) for rail in fence) 
    return encrypted_text


def decrypt(cipher, depth):
    if depth == 1:
        return cipher
    
    cipher = cipher.replace(' ', '')
    cipher = cipher.upper()
    text_length = len(cipher)

    fence = [[] for _ in range(depth)]
    rail = 0
    sign = 1

    # Create placeholders in the fence
    for _ in range(text_length):
        fence[rail].append(None)
        rail += sign

        if rail == depth - 1 or rail == 0:
            sign = -sign

    # Fill the fence with the cipher text
    index = 0
    for rail in range(depth):
        for i in range(len(fence[rail])):
            fence[rail][i] = cipher[index]
            index += 1

    # Read the fence to get the decrypted text
    rail = 0
    sign = 1
    decrypted_text = ''
    for _ in range(text_length):
        decrypted_text += fence[rail].pop(0)
        rail += sign

        if rail == depth - 1 or rail == 0:
            sign = -sign

    return decrypted_text

def brute_force_decrypt(cipher):
    cipher = cipher.replace(' ', '')
    cipher = cipher.upper()
    for i in range(1, len(cipher) + 1):
        try:
            print(f'Key: {i} => {decrypt(cipher, i)}')
        except IndexError:
            print(f'Error with key {i}, possibly invalid depth.')
    return 'Brute Force Decryption Completed'
    

print(encrypt('I am Sandesh Dhital', 3))
print(decrypt('IASIASNEHHTLMDDA', 3))
print(brute_force_decrypt('IASIASNEHHTLMDDA'))
