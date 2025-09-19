char = 'y'
code_point = ord(char)
hex_value = hex(code_point)

print(char)
print(code_point)
print(hex_value)

unicode_string = "Hello, world!"
bytes_object = unicode_string.encode('utf-8')
decoded_string = bytes_object.decode('utf-8')

print(bytes_object)
print(decoded_string)

bytes_42 = (42).to_bytes(1)
print(bytes_42)
integer_from_bytes = int.from_bytes(bytes_42)
print(integer_from_bytes)

rgb_example = '#964BDC'