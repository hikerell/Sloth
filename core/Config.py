import os
import sys
import yaml
import logging
import logging.config
import hashlib
import hashlib
import binascii
from Crypto.Cipher import AES

config = None

def get(name):
    pass

def set(name, value):
    pass

def getGlobalConfig():
    global config
    return config

def setGlobalConfig(newConfig):
    global config
    config = newConfig

def _encrypt(key, text):
    key = key.encode('utf-8')
    key = hashlib.md5(key).digest()[:16]
    iv = hashlib.md5(key).digest()[:16]
    padding = lambda s: s if len(s)%16==0 else s+'\0'*(16-len(s)%16)
    text = padding(text).encode('utf-8')
    bs = AES.new(key, AES.MODE_CBC, iv).encrypt(text)
    return binascii.hexlify(bs).decode('utf-8')

def _decrypt(key, text):
    key = key.encode('utf-8')
    key = hashlib.md5(key).digest()[:16]
    iv = hashlib.md5(key).digest()[:16]
    text = binascii.unhexlify(text.encode('utf-8'))
    text = AES.new(key, AES.MODE_CBC, iv).decrypt(text).decode('utf-8')
    unpadding = lambda s: s.rstrip('\0')
    return unpadding(text)

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def setup_config(default_path='project.yaml'):
    secret = None
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        setGlobalConfig(config)
    else:
        setGlobalConfig({'X':'Y'})
    config = getGlobalConfig()
    for ckey in config.keys():
        c = config[ckey]
        if 'Secure' in c.keys() and c['Secure']:
            if not secret:
                secret = input('config secret:')
            for k in c.keys():
                if k!='Secure':
                    c[k] = _decrypt(secret, c[k])
                    print('decrypt c[k]: %s' % str(c[k]))
    print(getGlobalConfig())


if config == None:
    setup_config()
    setup_logging()
        