import Decryptor
from threading import Thread
import textwrap
import time

chars = "abcdefghijklmnopqrstuvwxyz"


# Decryptor.basePerebor('1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad', chars)
# Decryptor.basePerebor('3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', chars)
# Decryptor.basePerebor('74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f', chars)


def multithreadedSearch(threadCount, hash):
	print(threadCount, time.time())
	splittedChars = split_alphabet(threadCount)
	for i in range(0, len(splittedChars)):
		Thread(target=Decryptor.basePerebor, args=(hash, splittedChars[i])).start()


def split_alphabet(threadCount):
	countInOne = int(len(chars) / threadCount)
	return textwrap.wrap(chars, countInOne)


start_time = time.time()
multithreadedSearch(5, '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad')
print(time.time()-start_time)

# multithreadedSearch(1, '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b')
# multithreadedSearch(1, '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f')
