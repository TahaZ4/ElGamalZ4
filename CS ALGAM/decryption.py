#  calculate the modular inverse of a number 'a' with respect to 'm'
def calculate_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        quotient = a // m
        m, a = a % m, m
        x0, x1 = x1 - quotient * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# to decrypt the message using the private key
def decrypt_message(p, x, c1, c2_list):
    # Step 1: Calculate 's' = c1^x % p using the private key 'x'
    s = pow(c1, x, p)
    
    # Step 2: Calculate the modular inverse of 's' (this undoes the encryption)
    s_inv = calculate_inverse(s, p)
    
    # Step 3: Decrypt each part of the ciphertext (c2) using s_inv
    decrypted_ascii = [(c2 * s_inv) % p for c2 in c2_list]
    
    # Step 4: Convert the decrypted ASCII values back to characters
    decrypted_message = ''.join(chr(m) for m in decrypted_ascii)
    
    return decrypted_message

# Main function to decrypt a message
if __name__ == "__main__":
    p = 7919  # Prime number used for encryption
    x = 1234  # Private key obtained from key generation
    
    # Encrypted message parts (c1, c2_list)
    c1 = 12345  # value (should match what was encrypted)
    c2_list = [23456, 23457, 23458]  # values (should match the encrypted message)
    
    # Decrypt the message
    decrypted_message = decrypt_message(p, x, c1, c2_list)
    
    # Print the decrypted message
    print("Decrypted Message:", decrypted_message)
