import random
import string
from datetime import datetime

quantity = 100   # KAÇ ADET KOD ÜRETİLECEK
length = 11      # KOD UZUNLUĞU

def gen_ran_code(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Dosya adı: 25-08-2025_20-45_random-code.txt
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
filename = f"{timestamp}_random-code.txt"

with open(filename, "w", encoding="utf-8") as f:
    for _ in range(quantity):
        code = gen_ran_code(length)
        f.write(code + "\n")

print(f"{quantity} adet kod üretildi ve '{filename}' dosyasına yazıldı.")
