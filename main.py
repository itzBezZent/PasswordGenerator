import random



def generate_password(length):
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(length):
        password += random.choice(characters)
    return password

password = generate_password(8)
print(password)
