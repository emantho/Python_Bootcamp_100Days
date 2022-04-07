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
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", " "]

# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"


def caesar(plain_text, shift_amount, action):
    final_text = ""
    for letter in plain_text:
        if letter in alphabet:
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

        else:
            if letter in numbers:
                letter_number_index = numbers.index(letter)

                if action == "encode":
                    new_number_index = letter_number_index + shift_amount
                    if new_number_index > 9:
                        new_number_index -= 9
                    final_text += numbers[new_number_index]

                if action == "decode":
                    new_number_index = letter_number_index - shift_amount
                    if new_number_index > 9:
                        new_number_index += 9
                    final_text += numbers[new_number_index]

            else:
                final_text += " "

    print(f"The encoded text is: {final_text}\n")


# TODO-1: Import and print the logo from art.py when the program starts.
from D8_art import logo

print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

go_again = "yes"

while go_again == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, action=direction)

    go_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
