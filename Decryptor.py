import threading
import time
import Encryptor

passwordDict = {}



def basePerebor(encryptHash, firstPart, chars="abcdefghijklmnopqrstuvwxyz"):
	count = 0
	for i in range(0, len(firstPart)):
		for j in range(0, len(chars)):
			for k in range(0, len(chars)):
				for m in range(0, len(chars)):
					for n in range(0, len(chars)):
						password = firstPart[i] + chars[j] + chars[k] + chars[m] + chars[n]
						count += 1
						hash = Encryptor.encrypt(password)
						passwordDict[hash] = password
						if Encryptor.encrypt(password) == encryptHash:
							print(password + " is correct")
							print(time.time())
							return
