alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
        

def caesar(direction, original_text, shift_amount):

    output_text = ""

    for x in original_text:

        if direction == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(x) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        output_text += alphabet[shifted_position]        
    
    print(f"Here is the {direction}d text :{output_text}")

caesar(direction=direction, original_text=text, shift_amount=shift)

