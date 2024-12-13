import random

# Encrypt message using the public key
def encrypt_message(p, g, y, message):
    # Convert message to ASCII values
    message_ascii = [ord(char) for char in message]
    
    # Generate a random value k for encryption
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)  # Compute g^k % p
    
    # Encrypt the message using y^k
    c2_list = [(m * pow(y, k, p)) % p for m in message_ascii]
    
    return c1, c2_list


# test cases
def test_encrypt_message():
    # Test 1: Single-character message
    random.seed(42)  # Fix randomness for reproducibility
    p, g, y, message = 23, 5, 10, "A"
    c1, c2_list = encrypt_message(p, g, y, message)
    print("Test 1: Single-character message")
    print(f"Inputs: p={p}, g={g}, y={y}, message='{message}'")
    print(f"Outputs: c1={c1}, c2_list={c2_list}\n")
    
    # Test 2: Multi-character message
    random.seed(42)  # Reset randomness to get the same k
    p, g, y, message = 31, 3, 17, "Hi"
    c1, c2_list = encrypt_message(p, g, y, message)
    print("Test 2: Multi-character message")
    print(f"Inputs: p={p}, g={g}, y={y}, message='{message}'")
    print(f"Outputs: c1={c1}, c2_list={c2_list}\n")


# Run the tests
test_encrypt_message()