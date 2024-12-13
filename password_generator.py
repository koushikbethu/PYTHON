import random
import string

password_length=7

characters=string.ascii_letters+string.digits+string.punctuation

password=''.join(random.choice(characters) for i in range(password_length))

print(f"Your generated password is :{password}")
