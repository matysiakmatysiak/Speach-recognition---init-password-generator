
import random
import string
def Password():
    total = string.ascii_letters + string.digits + string.punctuation
    length = 16
    password = "".join(random.sample(total, length))
    print(password)