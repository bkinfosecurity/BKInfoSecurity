"""
Program: Message Encoder v0.2
Author: Brock Kjelden
Website: https://bkinfosecurity.com
Date: June 19, 2023

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
import getpass as gp

def xor(msg, key = 'default', encode = False, decode = False):
	import base64
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
			key_index += 1
		return base64.b64encode(encrypted.encode()).decode()
	elif decode:
		msg = base64.b64decode(msg).decode()
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
			key_index += 1
		return decrypted
	else:
		print("Please Enter a valid number")



def menu():
	#Initial decision, type of encoding
	print("MESSAGE ENCODER V0.2")
	print("Choose an option (number):")
	print("\t1 - XOR")

	choice = int(input("-> "))

	#choose XOR for encoding/decoding
	if choice == 1:
		print("Choose an option (number):")
		print("\t1 - encode")
		print("\t2 - decode")

		choice2 = int(input("-> "))

		if choice2 == 1:	#encode
			msg = input("Write a message to encode:\n\t-> ")
			p = gp.getpass(prompt="Enter a key (no echo):\n\t-> ")
			print("Your encoded message is: " + xor(msg, p, encode = True) + "\n\n")
			menu()
		elif choice2 == 2:	#decode
			msg = input("Write a message to decode:\n-> ")
			p = gp.getpass(prompt="Enter a key (no echo):\n->")
			print("Your decoded message is: " + xor(msg, p, decode = True) + "\n\n")
			menu()
		else:	#invalid option
			print("Choose a valid number\n\n")
			menu()

menu()
