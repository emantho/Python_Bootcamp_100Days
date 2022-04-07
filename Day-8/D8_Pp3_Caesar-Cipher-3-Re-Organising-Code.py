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

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(plain_text, shift_amount, action):
    final_text = ""
    for letter in plain_text:
        letter_alphabet_index = alphabet.index(letter)

        if action == "encode":
            new_alphabet_index = letter_alphabet_index + shift_amount
            if new_alphabet_index > 25:
                new_alphabet_index -= 25
            final_text += alphabet[new_alphabet_index]

        elif action == "decode":
            new_alphabet_index = letter_alphabet_index - shift_amount
            if new_alphabet_index > 25:
                new_alphabet_index += 25
            final_text += alphabet[new_alphabet_index]
    print(f"The encoded text is: {final_text}\n")


# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift, action=direction)
