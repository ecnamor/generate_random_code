import random
import string
from datetime import datetime

quantity = 100   # How many codes will be generated
length = 11      # Length of each code

def gen_ran_code(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# File name format: 10-05-2021_12-00_random-code.txt
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
filename = f"{timestamp}_random-code.txt"

codes = set()
while len(codes) < quantity:
    codes.add(gen_ran_code(length))

# Calculate zero-padding length based on total quantity
pad_len = len(str(quantity))

with open(filename, "w", encoding="utf-8") as f:
    for idx, code in enumerate(codes, start=1):
        f.write(f"{str(idx).zfill(pad_len)}-{code}\n")

print(f"{len(codes)} adet benzersiz kod üretildi ve '{filename}' dosyasına yazıldı.")
