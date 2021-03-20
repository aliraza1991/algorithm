import time
import math
def is_prime(num):
	if num == 1:
		return False
	maxdivisior = math.floor(math.sqrt(num))
	for d in range(2, num):
		if num % d == 0:
			return False
	return True

t0 = time.time()
for n in range(1, 30000):
	# print(n, is_prime(n))
	is_prime(n)
t1 = time.time()
print(t1 - t0)
