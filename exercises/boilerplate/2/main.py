import hashlib
from itertools import product
import time
from datetime import datetime

lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = nums + lower_chars + upper_chars


def find_password_by_hash(hash, min, max):
    for length in range(min, max + 1):
        for charComb in product(chars, repeat=length):
            inputStr = ''.join(charComb)
            result = hashlib.sha1(inputStr.encode())
            generatedHash = result.hexdigest()
            if generatedHash == hash:
                return inputStr


def main():
    print(f"[{datetime.now()}] Started...")
    start = time.time()
    password = find_password_by_hash(
        "5aea476328379d3bff2204501bb57aa8b4268fac", 5, 5)
    end = time.time()
    print(f"[{datetime.now()}] Finished!")
    print(f"[{datetime.now()}] Password: {password}")
    print(f"[{datetime.now()}] Time elapsed: {end - start}s")


if __name__ == "__main__":
    main()
