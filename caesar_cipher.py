import string

# Enter only alphabets 
input_text = input("Enter text to encrypt:").lower()
shift_value = int(input("Enter a shift value:"))

alphabet = string.ascii_lowercase
alphabet = list(alphabet)



def encrypt(input_text,shift_value):
    """
    Shifts all the characters present in the input text by a fixed value(encrypting) and returns the encrypted text.
    """
    
    encrypted_text = ""
    for ch in input_text:
        index = alphabet.index(ch)
        if index + shift_value >=26:
            encrypted_text+="".join(alphabet[index + shift_value - 26])
        else:
            encrypted_text +="".join(alphabet[index + shift_value])
    
    return encrypted_text

encrypted_text = encrypt(input_text, shift_value)
print("Encrypted text:",encrypted_text)

def decrypt(encrypted_text):
    """
    Brute forces through all the shift values and decrypts the given encrypted text.
    Uses the method encrypt() but the shift value passed is negative, inorder to decrypt. 
    """
    print("All possible messages:")
    for shift in range(1,27):
        decrypted_text = encrypt(encrypted_text,-shift)
        print(decrypted_text, shift)
      

decrypt(encrypted_text)