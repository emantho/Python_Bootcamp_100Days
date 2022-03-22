from os import system ; system("clear")
from D8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ' ']

# Function start
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
# Function ends

# Program start

print(logo)

go_again = "yes"
while go_again == "yes":
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(plain_text = text, shift_amount = shift, action = direction)
        
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
   
# Program ends