import secrets

random = secrets.SystemRandom()

r_range = random.randrange(10,20) # (inicio,fim,step)
print(r_range)

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))