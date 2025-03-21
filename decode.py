import binascii 
print("Enter path to your txt file with base64 string:")
directory = str(input())
with open(directory, 'r') as file:
    file_read = file.read()
    text_write = binascii.a2b_base64(file_read)

print("Enter output file name:")
name = str(input())
with open(name, 'wb') as output_text:
    output_text.write(text_write)