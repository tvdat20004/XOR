hex1 = input("Enter the first hexadecimal number: ")
hex2 = input("Enter the second hexadecimal number: ")

# convert the hexadecimal strings to integers
num1 = int(hex1, 16)
num2 = int(hex2, 16)

# perform the XOR operation
result = num1 ^ num2

# convert the result back to hexadecimal string
hex_result = hex(result)[2:]

# pad the result with leading zeroes if necessary
if len(hex_result) < len(hex1):
    hex_result = '0' * (len(hex1) - len(hex_result)) + hex_result

print("The XOR result is:", hex_result)
