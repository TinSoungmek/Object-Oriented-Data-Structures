def encode_char(char, rotor_position):
    if not char.isalpha():
        return char, 0
    base = ord('A') if char.isupper() else ord('a')
    new_char = chr(base + (ord(char) - base + rotor_position) % 26)
    extra = 0
    if new_char == char:
        extra = 1
        new_char = chr(base + (ord(char) - base + rotor_position + 1) % 26)
    return new_char, extra

def decode_char(char, rotor_position):
    if not char.isalpha():
        return char, 0
    base = ord('A') if char.isupper() else ord('a')
    old_char = chr(base + (ord(char) - base - rotor_position) % 26)
    extra = 0
    if encode_char(old_char, rotor_position)[0] != char:
        extra = 1
        old_char = chr(base + (ord(char) - base - (rotor_position + 1)) % 26)
    return old_char, extra

def encode_message(message, rotor_position, index=0):
    if index >= len(message):
        return ""
    encoded_char, extra = encode_char(message[index], (rotor_position + index) % 26)
    return encoded_char + encode_message(message, rotor_position + extra, index + 1)

def decode_message(encoded_message, rotor_position, index=0):
    if index >= len(encoded_message):
        return ""
    decoded_char, extra = decode_char(encoded_message[index], (rotor_position + index) % 26)
    return decoded_char + decode_message(encoded_message, rotor_position + extra, index + 1)

print("This is Caesar cipher")
message, initial_rotor_position = input("Enter Input : ").split(',')
initial_rotor_position = int(initial_rotor_position)
encoded = encode_message(message, initial_rotor_position)
print("Encoded Message:", encoded)
decoded = decode_message(encoded, initial_rotor_position)
print("Decoded Message:", decoded)