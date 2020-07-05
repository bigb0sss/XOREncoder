# XOREncoder
XOR Encoder for shellcode using a choice of XOR key.

## Installation
```bash
git clone https://github.com/bigb0sss/XOREncoder.git
```
## Usage & Example
```bash
$ ./XOREncoder.py
 
    _  ______  ____     ______                     __          
   | |/ / __ \/ __ \   / ____/___  _________  ____/ /__  _____ 
   |   / / / / /_/ /  / __/ / __ \/ ___/ __ \/ __  / _ \/ ___/ 
  /   / /_/ / _, _/  / /___/ / / / /__/ /_/ / /_/ /  __/ /     
 /_/|_\____/_/ |_|  /_____/_/ /_/\___/\____/\__,_/\___/_/      
                                             [bigb0ss] v1.0    
 
usage: XOREncoder.py [-h] [-s SHELLCODE] [-k KEY]

[+] XOR Encoder

optional arguments:
  -h, --help            show this help message and exit
  -s SHELLCODE, --shellcode SHELLCODE
                        Input shellcode
  -k KEY, --key KEY     XOR Key

```
<br>
```bash
./XOREncoder.py -s "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" -k "0xaa"
 
    _  ______  ____     ______                     __          
   | |/ / __ \/ __ \   / ____/___  _________  ____/ /__  _____ 
   |   / / / / /_/ /  / __/ / __ \/ ___/ __ \/ __  / _ \/ ___/ 
  /   / /_/ / _, _/  / /___/ / / / /__/ /_/ / /_/ /  __/ /     
 /_/|_\____/_/ |_|  /_____/_/ /_/\___/\____/\__,_/\___/_/      
                                             [bigb0ss] v1.0    
 
[+] Shellcode Format: 
\x9b\x6a\xfa\xc2\x85\x85\xd9\xc2\xc2\x85\xc8\xc3\xc4\x23\x49\xfa\x23\x48\xf9\x23\x4b\x1a\xa1\x67\x2a
Length: 25 

[+] NASM Format: 
0x9b, 0x6a, 0xfa, 0xc2, 0x85, 0x85, 0xd9, 0xc2, 0xc2, 0x85, 0xc8, 0xc3, 0xc4, 0x23, 0x49, 0xfa, 0x23, 0x48, 0xf9, 0x23, 0x4b, 0x1a, 0xa1, 0x67, 0x2a, 
Length: 25 
```
