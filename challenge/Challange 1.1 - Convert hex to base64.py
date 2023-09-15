import base64

decoded_content = bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d").decode()
print(decoded_content)
sample_string_bytes = decoded_content.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
print(base64_string)