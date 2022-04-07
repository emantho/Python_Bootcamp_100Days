from os import system

system("clear")

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for l in plain_text:
        l_alphabet_index = alphabet.index(l)
        n_alphabet_index = l_alphabet_index + shift_amount
        # Creating a loop between end and start avoiding index error
        if n_alphabet_index > 25:
            n_alphabet_index -= 25
        encoded_text += alphabet[n_alphabet_index]
    print(f"The encoded text is: {encoded_text}\n")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encoded_text, shift_amount):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    decoded_text = ""
    for l in encoded_text:
        l_alphabet_index = alphabet.index(l)
        n_alphabet_index = l_alphabet_index - shift_amount
        # Creating a loop between end and start avoiding index error
        if n_alphabet_index > 25:
            n_alphabet_index += 25
        decoded_text += alphabet[n_alphabet_index]
    print(f"The decoded text is: {decoded_text}\n")


# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction != "encode" and direction != "decode":
    print(f"{direction} is not a valid option")
elif direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encoded_text=text, shift_amount=shift)
