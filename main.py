from data import logo, dict

def encode():
    morse = ""
    user_input_text = input("Please enter your message here. ").upper()
    for char in user_input_text:
        morse += dict[char]+" "

    print(morse)

def decode():
    morse_code = input("Please enter your morse cade here: ")
    message = ""
    code = ""
    for i in morse_code:
        if i != ' ':
            code += i
        elif i == ' ':
            message += list(dict.keys())[list(dict.values()).index(code)]
            code = ""

    message += list(dict.keys())[list(dict.values()).index(code)]
    print(message)

print(logo)
print("Wecome to Morse Code Converter")
choose = input("Please enter '1' for Encode or '2' for Decode: ")
if choose == "1":
    encode()
elif choose == "2":
    decode()
else:
    print("you entered wrong key")
