def caesar(message, offset):
    """
    Encrypts/decrypts a message using the Caesar cipher with a given offset.

    Args:
        message (str): The message to be encrypted/decrypted.
        offset (int): The number of positions to shift each character.

    Returns:
        str: The encrypted/decrypted message.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char  # Keep spaces unchanged
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

text = 'Hello Zaira'
shift = 3
caesar(text, shift)
caesar(text, 13)

def vigenere(message, key, direction=1):
    """
    Encrypts/decrypts a message using the Vigenère cipher with a given key.

    Args:
        message (str): The message to be encrypted/decrypted.
        key (str): The key to be used for encryption/decryption.
        direction (int): 1 for encryption, -1 for decryption. Defaults to 1.

    Returns:
        str: The encrypted/decrypted message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    """
    Encrypts a message using the Vigenère cipher with a given key.

    Args:
        message (str): The message to be encrypted.
        key (str): The key to be used for encryption.

    Returns:
        str: The encrypted message.
    """
    return vigenere(message, key)
    
def decrypt(message, key):
    """
    Decrypts a message using the Vigenère cipher with a given key.

    Args:
        message (str): The message to be decrypted.
        key (str): The key to be used for decryption.

    Returns:
        str: The decrypted message.
    """
    return vigenere(message, key, -1)

text = 'Hello, How are you?'
custom_key = 'python'

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
