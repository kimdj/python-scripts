import time

def powerOfTwo(n):
	if n == 0:
		return 1
	else:
		return powerOfTwo(n - 1) + powerOfTwo(n - 1)

def fasterPowerOfTwo(n):
	return 1 << n
	
t = time.time()
print "2^2: ", powerOfTwo(2)
print "2^3: ", powerOfTwo(3)
print "2^4: ", powerOfTwo(4)
print "2^5: ", powerOfTwo(5)
print time.time() - t

t = time.time()
print "2^2: ", fasterPowerOfTwo(2)
print "2^3: ", fasterPowerOfTwo(3)
print "2^4: ", fasterPowerOfTwo(4)
print "2^5: ", fasterPowerOfTwo(5)
print time.time() - t