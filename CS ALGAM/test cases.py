def decrypt_message(p, x, c1, c2_list):
    """Decrypt message using private key"""
    # Recover shared secret
    s = pow(c1, x, p)
    
    # Calculate modular inverse
    s_inv = pow(s, p-2, p)  # Using Fermat's for prime modulus
    
    # Decrypt each character
    decrypted_ascii = [(c2 * s_inv) % p for c2 in c2_list]
    
    # Convert to text
    return ''.join(chr(m) for m in decrypted_ascii)

# Test cases
def test_decrypt_message():
    """Validation protocol for decryption module"""
    # Test 1: Known value verification
    p, x, c1 = 23, 6, 8
    c2_list = [5]
    decrypted = decrypt_message(p, x, c1, c2_list)
    print("Test 1: Known Value Verification")
    print(f"Inputs: p={p}, x={x}, c1={c1}, c2_list={c2_list}")
    print(f"Output: '{decrypted}'")
    print(f"Validation: {'PASSED' if decrypted == 'A' else 'FAILED'}\n")
    
    # Test 2: Multi-character decryption
    p, x, c1 = 31, 17, 29
    c2_list = [19, 15]
    decrypted = decrypt_message(p, x, c1, c2_list)
    print("Test 2: Multi-character Validation")
    print(f"Inputs: p={p}, x={x}, c1={c1}, c2_list={c2_list}")
    print(f"Output: '{decrypted}'")
    print(f"Validation: {'PASSED' if decrypted == 'Hi' else 'FAILED'}")

if __name__ == "__main__":
    test_decrypt_message()