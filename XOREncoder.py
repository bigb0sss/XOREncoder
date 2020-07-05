#!/usr/bin/python
# Version         : 1.0
# Created date    : 07/03/2020
# Last update     : 07/03/2020
# Author          : bigb0ss
# Description     : XOR Encoder for shellcode
# Example         : ./XOREncoder.py -s "\x41\x42\x43" -k "0xAA"

import sys
import argparse

""" Setup Argument Parameters """
parser = argparse.ArgumentParser(description='[+] XOR Encoder')
parser.add_argument('-s', '--shellcode', help='\tInput shellcode')
parser.add_argument('-k', '--key', help='\tXOR Key')
args = parser.parse_args()

def banner():
    print(" ")
    print("    _  ______  ____     ______                     __          ")   
    print("   | |/ / __ \/ __ \   / ____/___  _________  ____/ /__  _____ ")
    print("   |   / / / / /_/ /  / __/ / __ \/ ___/ __ \/ __  / _ \/ ___/ ")
    print("  /   / /_/ / _, _/  / /___/ / / / /__/ /_/ / /_/ /  __/ /     ") 
    print(" /_/|_\____/_/ |_|  /_____/_/ /_/\___/\____/\__,_/\___/_/      ")
    print("                                             [bigb0ss] v1.0    ")
    print(" ")

def error():
    parser.print_help()
    exit(1)

# Shellcode Format
def encodeFormat1(a, b):
    print "[+] Shellcode Format: "
    encode = ""
    for i in a:
        i = int(i, 16)
        
        xorKey = i^b
        encode+= "\\x"
        encode+= "%02x" % xorKey
    print encode
    length = len(encode)/4
    print "Length: %d \n" % length

# NASM Format
def encodeFormat2(a, b):
    print "[+] NASM Format: "
    encode = ""
    for i in a:
        i = int(i, 16)

        xorKey = i^b
        encode+= "0x"
        encode+= "%02x, " % xorKey
    print encode
    length = len(encode)/6
    print "Length: %d \n" % length


if __name__ == '__main__':
    # Banner
    banner()
    
    shellcode = args.shellcode if args.shellcode != None else error()
    shellcode = shellcode[2:]
    shellcode = shellcode.split("\\x")

    key = args.key if args.key != None else error()
    key = int(key, 16)

    encodeFormat1(shellcode, key)
    encodeFormat2(shellcode, key)
