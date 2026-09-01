import caesar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#def encrypt(original_text, shift_amount):
#    shift_amount = int(shift_amount)
#    encrypted_text = ""
#    for letter in original_text:
#        index = alphabet.index(letter)
#        shifted = index + shift_amount
#        encrypted_text += alphabet[shifted % len(alphabet)] # Pour vulgariser, cette ligne permet en quelque sorte de recommencer là liste   
#    print(encrypted_text)

#def decrypt(original_text, shift_amount):
#    shift_amount = int(shift_amount)
#    decrypted_text = ""
#    for letter in original_text:
#        index = alphabet.index(letter)
#        shifted = index - shift_amount
#        decrypted_text += alphabet[shifted % len(alphabet)]
#    print(decrypted_text)    


def caesar(direction, original_text, shift_amount):
    treated_text = ""
    if direction == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            shifted = letter_index + shift_amount
            treated_text += alphabet[shifted % len(alphabet)] # Pour vulgariser, cette ligne permet en quelque sorte de recommencer la liste
        else:
            treated_text += letter

    print(f"Le message {direction}é est : {treated_text}.")
        
    
print(caesar_art.logo)

# Boucle pour continuer le programme
program_loop = True

while program_loop == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    keep_programm_running = str(input("Type 'yes' if you want to go again. Otherwise, type 'no' : ")).lower()
    if keep_programm_running == "no":
        program_loop = False
