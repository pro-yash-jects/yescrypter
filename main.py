#!/usr/bin/env python3

import argparse
from pyescrypt.pyescrypt import Yescrypt
import os
import time
from termcolor import colored

# 🔥 ASCII Art Banner
BANNER = r"""

                                                  __                
 ___.__. ____   ______ ___________ ___.__._______/  |_  ___________ 
<   |  |/ __ \ /  ___// ___\_  __ <   |  |\____ \   __\/ __ \_  __ \
 \___  \  ___/ \___ \\  \___|  | \/\___  ||  |_> >  | \  ___/|  | \/
 / ____|\___  >____  >\___  >__|   / ____||   __/|__|  \___  >__|   
 \/         \/     \/     \/       \/     |__|             \/       

"""

def hash_with_yescrypt(word, salt=None, N=16384, r=8, p=1, dkLen=64):
    if salt is None:
        salt = os.urandom(16)
    yescrypt = Yescrypt(n=N, r=r, p=p)
    hashed = yescrypt.digest(word.encode(), salt, dkLen)
    return hashed.hex(), salt.hex()

def main():
    parser = argparse.ArgumentParser(description="🛡️ Yescrypt CLI Hasher", epilog="🔐 Secure your passwords like a pro.")
    parser.add_argument("word", help="Word or password to hash")
    parser.add_argument("--salt", help="Optional salt (default: random 16 bytes)", default=None)
    parser.add_argument("--n", type=int, default=16384, help="CPU/memory cost parameter (default: 16384)")
    parser.add_argument("--r", type=int, default=8, help="Block size parameter (default: 8)")
    parser.add_argument("--p", type=int, default=1, help="Parallelism parameter (default: 1)")
    parser.add_argument("--dklen", type=int, default=64, help="Derived key length in bytes (default: 64)")

    args = parser.parse_args()


    print(colored(BANNER, "cyan"))

    if args.salt:
        try:
            salt = bytes.fromhex(args.salt)
        except ValueError:
            print(colored("[!] Invalid salt hex string. Using random salt instead.", "red"))
            salt = os.urandom(16)
    else:
        salt = os.urandom(16)

    start = time.time()
    hashed, salt_hex = hash_with_yescrypt(args.word, salt, args.n, args.r, args.p, args.dklen)
    end = time.time()

    print(colored(f"[+] Input       : ", "green") + f"{args.word}")
    print(colored(f"[+] Salt (hex)  : ", "green") + f"{salt_hex}")
    print(colored(f"[+] Hash        : ", "green") + f"{hashed}")
    print(colored(f"[i] Time taken  : ", "yellow") + f"{end - start:.4f} seconds")
    print(colored(f"[i] Memory cost : ", "yellow") + f"~{128 * args.n * args.r // 1024 // 1024} MB (approx)")

if __name__ == "__main__":
    main()
