import random
import string

print('''
=====================
=== EC2 Generator ===
=====================
''')

names = int(input('How many EC2 instances would you like to create? '))
department = input('What department do you work for? ')

for nam in range(names):
    randomLetter = random.choice(string.ascii_letters)
    random_numbers = str(random.randint(100, 900))
    chars = (randomLetter + random_numbers)
    print(f'{department}-{chars}')