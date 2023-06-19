"""
Program: Message Encoder v0.1
Author: Brock Kjelden
Website: https://bkinfosecurity.com
Date: June 18, 2023

Description:
This program is built to encrypt and encode messages to be sent publicly, this program
is by no means a secure way to send sensitive information, just a fun way to send messages
that others can't immediately decipher.

Disclaimer:
This program is provided for educational purposes only. You are allowed to use it as a learning
resource, experiment with it, and modify it for personal use. However, you are strictly prohibited
from using this program to steal or plagiarize someone else's work and claim it as your own.
The author and contributors of this program hold no responsibility for any misuse or unethical
use of this code.

"""
def xor(msg, key = 'default', encode = False, decode = False):
	if encode:
		encrypted = ""
		key_index = 0
		for char in msg:
			#convert character to ascii code
			char_code = ord(char)
			#get the corresponding key char
			key_char = key[key_index % len(key)]
			#convert key char to ascii code
			key_code = ord(key_char)
			#XOR with key
			encrypted_char = char_code ^ key_code
			#convert enc ascci back to char
			encrypted += chr(encrypted_char)
		return encrypted
	if decode:
		decrypted = ""
		key_index = 0
		for char in msg:
			#convert char to ascii
			char_code = ord(char)
			#get the corresponding key char
			key_char = key[key_index % len(key)]
			#convert key char to ascii code
			key_code = ord(key_char)
			#XOR with key
			decrypted_char = char_code ^ key_code
			#convert dec ascii back to char
			decrypted += chr(decrypted_char)
		return decrypted

super_secret = "This is a secret message"
encrypted_data = xor(super_secret, "password", encode = True)
decrypted_data = xor(encrypted_data, "password", decode = True)

f = open("output.txt", "a")
f.write(encrypted_data)


print("the cipher text is: ")
print(encrypted_data)
print("The plain text is: ")
print(decrypted_data)
