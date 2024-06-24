def caesar_cipher_encrypt(text, shift):
    """Encrypt the given text using Caesar cipher with the specified shift."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')  # Determine the ASCII base value
            # Shift the character and wrap around using modulo 26
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetical characters are not changed
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypt the given text using Caesar cipher with the specified shift."""
    # Decryption is just encryption with the negative of the shift value
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    print("This program allows you to encrypt or decrypt messages using the Caesar cipher.")
    print("The Caesar cipher works by shifting each letter in the message by a certain number of positions in the alphabet.")
    print("You will need to provide the message and the shift value (a whole number).")
    print()
    
    # Prompt the user to choose encryption or decryption
    choice = input("Do you want to encrypt or decrypt the message? (Type 'e' for encryption or 'd' for decryption): ").lower()
    
    # Validate the user's choice
    if choice not in ['e', 'd']:
        print("Invalid choice! Please type 'e' for encryption or 'd' for decryption.")
        return
    
    # Prompt the user for the message
    message = input("Enter your message: ")
    
    # Prompt the user for the shift value
    try:
        shift = int(input("Enter the shift value (a whole number, e.g., 3): "))
    except ValueError:
        print("Invalid shift value! Please enter a valid integer.")
        return

    # Perform encryption or decryption based on the user's choice
    if choice == 'e':
        result = caesar_cipher_encrypt(message, shift)
        print("\nEncryption successful!")
        print("Original message: ", message)
        print("Shift value: ", shift)
        print("Encrypted message: ", result)
    elif choice == 'd':
        result = caesar_cipher_decrypt(message, shift)
        print("\nDecryption successful!")
        print("Original message: ", message)
        print("Shift value: ", shift)
        print("Decrypted message: ", result)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
