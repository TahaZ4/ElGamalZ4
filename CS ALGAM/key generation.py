import random

# Function to calculate the modular inverse of a number 'a' with respect to 'm'
def calculate_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        quotient = a // m
        m, a = a % m, m
        x0, x1 = x1 - quotient * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to generate public and private keys for ElGamal encryption
def generate_keys(p):
    g = 5  # A fixed base (primitive root). It could vary in practice.
    x = random.randint(2, p - 2)  # Random private key 'x'.
    y = pow(g, x, p)  # Calculate the public key part y = g^x % p.

    # Return the public key (p, g, y) and the private key 'x'
    return (p, g, y), x

# Main function to run the key generation
if __name__ == "__main__":
    p = 7919  # A large prime number used for key generation.
    
    # Generate public and private keys
    public_key, private_key = generate_keys(p)
    
    # Print out the keys
    print("Public Key:", public_key)
    print("Private Key:", private_key)
