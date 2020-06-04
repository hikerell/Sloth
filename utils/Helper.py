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

def encrypt(key, text):
	key = key.encode('utf-8')
	key = hashlib.md5(key).digest()[:16]
	iv = hashlib.md5(key).digest()[:16]
	padding = lambda s: s if len(s)%16==0 else s+'\0'*(16-len(s)%16)
	text = padding(text).encode('utf-8')
	bs = AES.new(key, AES.MODE_CBC, iv).encrypt(text)
	return binascii.hexlify(bs).decode('utf-8')

def decrypt(key, text):
	key = key.encode('utf-8')
	key = hashlib.md5(key).digest()[:16]
	iv = hashlib.md5(key).digest()[:16]
	text = binascii.unhexlify(text.encode('utf-8'))
	text = AES.new(key, AES.MODE_CBC, iv).decrypt(text).decode('utf-8')
	unpadding = lambda s: s.rstrip('\0')
	return unpadding(text)
	