from key_generation import calculate_inverse

def decrypt_message(private_key, public_key, ciphertext):
    """
    Decrypt message using private key
    private_key: integer x
    public_key: tuple (p, g, y)
    ciphertext: tuple (c1, c2_list)
    Returns: decrypted string
    """
    p, g, y = public_key
    x = private_key
    c1, c2_list = ciphertext
    
    # Recover the shared secret
    s = pow(c1, x, p)
    s_inv = calculate_inverse(s, p)
    
    # Decrypt each component
    decrypted_vals = [(c2 * s_inv) % p for c2 in c2_list]
    return ''.join(chr(v) for v in decrypted_vals)

if __name__ == "__main__":
    # Test decryption
    private_key = 1234           # Sample private key
    public_key = (7919, 5, 2341) # Sample public key
    ciphertext = (5678, [3456, 7890, 1234, 5678, 9012])  # Sample ciphertext
    
    decrypted = decrypt_message(private_key, public_key, ciphertext)
    
    print("\nDecryption Module")
    print(f"Ciphertext (c1): {ciphertext[0]}")
    print(f"Ciphertext (c2): {ciphertext[1][:5]}...")
    print(f"Decrypted message: '{decrypted}'")