alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and Type 'decode' to decrypt or 'exit to stop':\n")
def cipher(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            each_letter = alphabet.index(char)
            new_position = each_letter + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f"The {cipher_direction}d text is {cipher_text}")




def cipher_direction(shift_dir):
    while not shift_dir == "exit":
        if shift_dir == "encode":
            text = input("Type your message ").lower()
            shift = int(input("How much shift you want? "))
            cipher(text, shift, shift_dir)
        else:
            text = input("Type your message ").lower()
            shift = int(input("How much shift you want? "))
            cipher(text, shift, shift_dir)
        shift_dir = input("Type 'encode' to encrypt and Type 'decode' to decrypt or 'exit to stop':\n")
cipher_direction(direction)
