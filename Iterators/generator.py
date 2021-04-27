import hashlib
from Decorators.logger import first_logging


@first_logging
def super_hash(file):
    start = 0
    with open(file, 'r') as text:
        lines = text.readlines()
    while start < len(lines):
        result = hashlib.md5(lines[start].encode())
        yield result.hexdigest()
        start += 1


for count in super_hash('wiki.txt'):
    print(count)
