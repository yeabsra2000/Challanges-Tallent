def xor_buffers(buffer1, buffer2):
    bytes1 = bytes.fromhex(buffer1)
    bytes2 = bytes.fromhex(buffer2)

    result = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    hex_result = result.hex()

    return hex_result

hex_1 = "1c0111001f010100061a024b53535009181c"
hex_2 = "686974207468652062756c6c277320657965"

print(xor_buffers(hex_1, hex_2))
