import random

def encrypt_message(public_key, message):
    """
    Encrypt message using public key
    public_key: tuple (p, g, y)
    message: string to encrypt
    Returns: (c1, c2_list) tuple
    """
    p, g, y = public_key
    ascii_vals = [ord(char) for char in message]
    
    k = random.randint(2, p - 2)  # Random session key
    c1 = pow(g, k, p)  # First component
    
    # Encrypt each character
    c2_list = [(m * pow(y, k, p)) % p for m in ascii_vals]
    
    return (c1, c2_list)

if __name__ == "__main__":
    # Test encryption
    public_key = (7919, 5, 2341)  # Sample public key
    message = "Test Message"
    c1, c2_list = encrypt_message(public_key, message)
    
    print("\nEncryption Module")
    print(f"Message: '{message}'")
    print(f"Ciphertext (c1): {c1}")
    print(f"Ciphertext (c2 first 5 values): {c2_list[:5]}")
