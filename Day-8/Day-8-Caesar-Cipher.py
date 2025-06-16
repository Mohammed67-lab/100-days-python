from art import logo
print(logo)

def caesar(direction, original_text, shift_amount):

    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for x in original_text:

        if x not in alphabet:
            output_text = output_text + x
        
        else:
            shifted_position = alphabet.index(x) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            output_text += alphabet[shifted_position]        
    
    print(f"Here is the {direction}d result :{output_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

silently_continue = True
while silently_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction, original_text=text, shift_amount=shift)
    
    restart = input("Type 'Yes' to restart else 'No' to stop:\n").lower()

    if restart == 'no':
        silently_continue = False
        print("GoodBye")


