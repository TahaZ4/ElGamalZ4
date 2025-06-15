import random

# Configuration - CHANGE THESE VALUES
PRIME = 7919        # Prime modulus
BASE_G = 5          # Generator base

def calculate_inverse(a, m):
    """Calculate modular inverse using extended Euclidean algorithm"""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        quotient = a // m
        m, a = a % m, m
        x0, x1 = x1 - quotient * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    """Generate public and private keys"""
    x = random.randint(2, PRIME - 2)  # Private key
    y = pow(BASE_G, x, PRIME)         # Public key component
    return (PRIME, BASE_G, y), x

if __name__ == "__main__":
    # Test key generation
    public_key, private_key = generate_keys()
    print("Key Generation Module")
    print(f"Prime: {PRIME}, Base: {BASE_G}")
    print(f"Public Key (p,g,y): {public_key}")
    print(f"Private Key (x): {private_key}")