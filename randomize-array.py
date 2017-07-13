import random

array = [i for i in xrange(10)]
print "initialized array: ", array
random.shuffle(array)
print "   shuffled array: ", array
