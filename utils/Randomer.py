import random
import hashlib
import binascii
from Crypto.Cipher import AES

def rnd(s, e):
	return random.randint(s, e-1)

def choice(objects):
	if type(objects)==set:
		objects = list(objects)
	return random.choice(objects)

def weighted(wlist):
	wl = []
	for wo in wlist:
		w = 0.0
		while w<wo['w'] and w<1.1:
			w += 0.1
			wl.append(wo['v'])
	return wl


	