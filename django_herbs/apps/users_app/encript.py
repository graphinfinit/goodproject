from pyDes import *

secret_key = 'FE.1F.01.E0.FE.0E.01.F1w' #24 или 16 байтный ключ
def encript(text,secret_key):
    '''простой Triple DES шифратор для слабого уровня защиты'''
    ciphertext = triple_des(secret_key).encrypt(text, padmode=2)
    return ciphertext.hex()

def decripte(ciphertext,secret_key):
    '''простой Triple DES дешифратор'''
    ciphertext = bytes.fromhex(ciphertext)
    text = triple_des(secret_key).decrypt(ciphertext, padmode=2)
    return str(text)[2:-1]

