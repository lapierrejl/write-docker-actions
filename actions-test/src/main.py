
from random import seed
from random import randint

seed(1)
value = randint(0, 100)
with open('README.md', 'w') as f:
    f.write(f"# {value}")
