import binascii 
print("Enter path to your input file:")
directory = str(input())
with open(directory, 'rb') as file:
    file_read = file.read()
    text_write = str(binascii.b2a_base64(file_read))
    text_write = text_write[2:-3]

print("Enter name of the output txt file:")
name = str(input())
with open(name + ".txt", 'w') as output_text:
    output_text.write(text_write)