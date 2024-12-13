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

# Function to encrypt a message using the public key
def encrypt_message(p, g, y, message):
    # Convert message into ASCII values
    message_ascii = [ord(char) for char in message]
    
    k = random.randint(2, p - 2)  # Random value for uniqueness
    c1 = pow(g, k, p)  # Calculate c1 = g^k % p
    
    # Encrypt the message using y^k
    c2_list = [(m * pow(y, k, p)) % p for m in message_ascii]
    
    # Return encrypted message as tuple (c1, c2_list)
    return c1, c2_list

# Main function to encrypt a message
if __name__ == "__main__":
    p = 7919  # Prime number used for encryption
    g = 5  # Base used in encryption (could vary)
    y = 2341  # Public key part, y = g^x % p (as obtained from key generation)
    
    message = "Hello, ElGamal!"  # Message to encrypt
    
    # Encrypt the message
    c1, c2_list = encrypt_message(p, g, y, message)
    
    # Print the encrypted message (c1, c2_list)
    print("Encrypted Message (c1, c2_list):", c1, c2_list)
