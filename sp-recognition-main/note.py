
import random
import string
import datetime
import requests

def Password():
    total = string.ascii_letters + string.digits + string.punctuation
    length = 16
    password = "".join(random.sample(total, length))
    f = open('pass.txt', mode='a', encoding='UTF8')
    f.write(f'password = {password}\n')
    f.close


