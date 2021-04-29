import random
import string

i=0 #VARIABLE
quantity=100 #QUANTITY
length=11 #LENGTH OF RANDOM CODE
def gen_ran_code(length):
    set = string.ascii_letters + string.digits
    result = ''.join(random.choice(set) for i in range(length))
    return result
while True:
    if i<quantity:
        print(gen_ran_code(length))
        i+=1
        continue
    else:
        break
