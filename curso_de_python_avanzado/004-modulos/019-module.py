import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 123 465 7890, el codigo del pais es 54 =, mi numero de la suerte es el 3'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)