hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
byte_string = bytes.fromhex(hex_string)

def xor_decrypt(byte_string, key):
    decrypted = b""
    for byte in byte_string:
        decrypted += bytes([byte ^ key])
    return decrypted

decryptions = []
for key in range(256):
    decrypted = xor_decrypt(byte_string, key)
    decryptions.append(decrypted)

def score(decryption):
    score = 0
    for byte in decryption:
        if byte in range(65, 91) or byte in range(97, 123):  # English letters
            score += 1
        elif byte == 32:  # Space
            score += 1
        elif byte in [9, 10, 13]:  # Tab, newline, carriage return
            score += 1
        elif decryption.count(b" the ") > 0:  # Common English word "the"
            score += 1
    return score

scores = [score(decryption) for decryption in decryptions]

best_decryption = decryptions[scores.index(max(scores))]

print("Decrypted message:", best_decryption.decode())