
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ' ', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ' ', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alphabet[9])
letter_list = []
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        each_letter = alphabet.index(letter)
        new_position = each_letter + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The cipher text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        each_letter = alphabet.index(letter)
        new_position = each_letter - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The cipher text is {cipher_text}")

def cipher_direction():

    direction = input("Type 'encode' to encrypt and Type 'decode' to decrypt or 'exit to stop':\n")
    while not direction == "exit":
        if direction == "encode":
            text = input("Type your message ").lower()
            shift = int(input("How much shift you want? "))
            encrypt(text, shift)
        else:
            text = input("Type your message ").lower()
            shift = int(input("How much shift you want? "))
            decrypt(text, shift)
        direction = input("Type 'encode' to encrypt and Type 'decode' to decrypt or 'exit to stop':\n")
cipher_direction()




