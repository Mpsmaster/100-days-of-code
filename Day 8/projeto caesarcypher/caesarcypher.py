logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def begin():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Please, type encode or decode")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        continue
    text = input("Type your message:\n").lower()
    
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Please, type a number")
    def caesar(original_text, shift_amount, encode_decode):
        cipher_text = ""
        if encode_decode == "decode":
                    shift_amount *= -1
        for letter in original_text:
            if letter in alphabet:  
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter
        print(f"Here is the {direction}d result: {cipher_text}")


    caesar(original_text=text, shift_amount=shift, encode_decode=direction)
begin()
while True:
    restart = input("Do you want to restart the cipher? Type 'yes' or 'no':\n").lower()
    if restart not in ["yes", "no"]:
        print("Please, type yes or no")
        continue
    else:
        if restart == "yes":
            begin()
        else:
            print("Goodbye")
            input("Press enter to exit")
            break        