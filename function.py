import string

def caesar_shift(char, shift, encrypt=True):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        shift = shift if encrypt else -shift
        return chr((ord(char) - base + shift) % 26 + base)
    elif char.isdigit():
        shift = shift if encrypt else -shift
        return str((int(char) + shift) % 10)
    return char

def vigenere_shift(char, key_char, encrypt=True):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        shift = (ord(key_char.lower()) - ord('a')) * (1 if encrypt else -1)
        return chr((ord(char) - base + shift) % 26 + base)
    elif char.isdigit():
        shift = (ord(key_char.lower()) - ord('a')) % 10 * (1 if encrypt else -1)
        return str((int(char) + shift) % 10)
    return char

def hybrid_transform(text, key="", caesar_shift_value=3, encrypt=True):
    key_length = len(key)
    transformed_text = ""
    key_index = 0
    
    for char in text:
        if char.isalnum():
            shifted_char = caesar_shift(char, caesar_shift_value, encrypt)
            transformed_text += vigenere_shift(shifted_char, key[key_index % key_length], encrypt)
            key_index += 1
        else:
            transformed_text += char
    
    return transformed_text

def encrypt(text):
    return hybrid_transform(text, encrypt=True)

def decrypt(text):
    return hybrid_transform(text, encrypt=False)

# Joyful Interface
print("🌟 Welcome to the Poseng Cipher! 🌟")
print("🔐 A fun and secret way to encode your messages! 🔐")
print("-------------------------------------------------")
option = input("🎭 Enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()
text = input("✍️ Enter your text: ")

if option == 'e':
    result = encrypt(text)
    print("✨ Encrypted message: ", result, " ✨")
elif option == 'd':
    result = decrypt(text)
    print("🔓 Decrypted message: ", result, " 🔓")
else:
    print("❌ Invalid option. Please enter 'e' or 'd'. ❌")

print("🎉 Thank you for using the Poseng Cipher! Keep your messages secret and fun! 🎉")
