import string
import random
import time

target = "hello world"
letters = string.ascii_letters +" "
result = ""

for letter in target:
    while True:
        l = random.choice(letters)
        print(result + l)
        if l == letter:
            result += l
            break
        time.sleep(0.1)

print("found",target,"!!!!")