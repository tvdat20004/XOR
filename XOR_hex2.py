hex1 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# convert the hexadecimal strings to integers
hex1 = bytes.fromhex(hex1)
for key in range(256):
    result = bytes([byte ^ key for byte in hex1])
    ascii_str = result.decode(errors='ignore')
    print(f"key={key}, ascii_str={ascii_str}")
# perform the XOR operation
# for num2 in range(255):
#     result = num1 ^ num2
#     hex_result = hex(result)[2:]
#     if len(hex_result) < len(hex1):
#         hex_result = '0' * (len(hex1) - len(hex_result)) + hex_result
#     print(hex_result)

# convert the result back to hexadecimal string

# pad the result with leading zeroes if necessary


