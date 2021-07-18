#!/usr/bin/python

import random
import string

alphabet = string.ascii_letters + string.digits 

result_string = ''
i = 0
MAX_STR_SIZE = 8
while i < MAX_STR_SIZE:
	result_string += random.choice(alphabet)
	i += 1
print result_string