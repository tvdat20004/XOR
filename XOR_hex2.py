hex1 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# convert the hexadecimal strings to integers
hex1 = bytes.fromhex(hex1)
for key in range(256):
    result = bytes([byte ^ key for byte in hex1])
    # convert the result back to hexadecimal string
    ascii_str = result.decode(errors='ignore')
    print(f"key={key}, ascii_str={ascii_str}")
