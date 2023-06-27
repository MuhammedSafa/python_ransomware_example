#!/usr/bin/env python3


import os 
from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("type", type=str, help='Please type "enc" or "dec" key', choices={"enc", "dec"})
args = parser.parse_args()


secret_key=""

def write_key_to_file():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key_from_file():
    return open("secret.key", "rb").read()

if not os.path.isfile("secret.key"):
    write_key_to_file()

if os.path.isfile("secret.key"):
    secret_key = load_key_from_file()

fernet_key = Fernet(secret_key)

def enc_dec_files(choice):
    for file in list_files:
        with open(file, "rb") as fl:
            content = fl.read()
        if choice == "enc":
           content_encrypted = fernet_key.encrypt(content)
        elif choice == "dec":
           content_encrypted = fernet_key.decrypt(content)
        with open(file, "wb") as fl:
           fl.write(content_encrypted)


#def encrypte_files():
#    for file in list_files:
#        with open(file, "rb") as fl:
#            content = fl.read()
#        content_encrypted = fernet_key.encrypt(content)
#        with open(file, "wb") as fl:
#            fl.write(content_encrypted)

#def decrypte_files():
#    for file in list_files:
#        with open(file, "rb") as fl:
#            content = fl.read()
#        content_encrypted = fernet_key.decrypt(content)
#        with open(file, "wb") as fl:
#            fl.write(content_encrypted)

list_files = []

for file in os.listdir():
    if file.endswith(".txt") & os.path.isfile(file):
        list_files.append(file)

#if args.type == "enc":
#    encrypte_files()
#elif args.type == "dec":
#    decrypte_files()

enc_dec_files(args.type)
