import random
import string

def generate_password(len):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(len))
    return password
