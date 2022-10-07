#! /bin/env python3
import argparse, base64
from hashlib import blake2b

parser = argparse.ArgumentParser(description="Password Manager")
parser.add_argument('m',type=str,help='Master-Password')
parser.add_argument('t',type=str,help='Tag')

args = parser.parse_args()

def generate_passwd(mp, tag):
    passwd = bytes(mp, 'utf-8')
    salt = bytes(tag, 'utf-8')
    h = blake2b(digest_size=8)
    h.update(passwd+salt)
    gen = h.hexdigest()
    final = base64.b64encode(bytes( gen, 'utf-8'))
    
    return final

print(generate_passwd(args.m, args.t))
