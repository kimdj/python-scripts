import random, time

############################################################

# merge function implementation

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

############################################################

# merge sort implementation

def mergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) / 2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a, b)
	
############################################################
	
# generate unsorted lists

list_1 = [i for i in xrange(1000)]  # create an array
random.shuffle(list_1)  # shuffle the array

list_2 = [i for i in xrange(2000)]  # create an array
random.shuffle(list_2)  # shuffle the array

list_3 = [i for i in xrange(3000)]  # create an array
random.shuffle(list_3)  # shuffle the array

list_4 = [i for i in xrange(4000)]  # create an array
random.shuffle(list_4)  # shuffle the array

list_5 = [i for i in xrange(5000)]  # create an array
random.shuffle(list_5)  # shuffle the array

list_6 = [i for i in xrange(6000)]  # create an array
random.shuffle(list_6)  # shuffle the array

list_7 = [i for i in xrange(7000)]  # create an array
random.shuffle(list_7)  # shuffle the array

list_8 = [i for i in xrange(8000)]  # create an array
random.shuffle(list_8)  # shuffle the array

list_9 = [i for i in xrange(9000)]  # create an array
random.shuffle(list_9)  # shuffle the array

list_10 = [i for i in xrange(10000)]  # create an array
random.shuffle(list_10)  # shuffle the array
			
############################################################
	
# run the merge sort algorithm on the unsorted lists

print "running merge sort on unsorted lists"

t1 = time.time()
mergeSort(list_1)
print("%s" % (time.time() - t1))

t2 = time.time()
mergeSort(list_2)
print("%s" % (time.time() - t2))

t3 = time.time()
mergeSort(list_3)
print("%s" % (time.time() - t3))

t4 = time.time()
mergeSort(list_4)
print("%s" % (time.time() - t4))

t5 = time.time()
mergeSort(list_5)
print("%s" % (time.time() - t5))

t6 = time.time()
mergeSort(list_6)
print("%s" % (time.time() - t6))

t7 = time.time()
mergeSort(list_7)
print("%s" % (time.time() - t7))

t8 = time.time()
mergeSort(list_8)
print("%s" % (time.time() - t8))

t9 = time.time()
mergeSort(list_9)
print("%s" % (time.time() - t9))

t10 = time.time()
mergeSort(list_10)
print("%s" % (time.time() - t10))

############################################################

# generate sorted lists

u_list_1 = [i for i in xrange(1000)]  # create an array
u_list_2 = [i for i in xrange(2000)]  # create an array
u_list_3 = [i for i in xrange(3000)]  # create an array
u_list_4 = [i for i in xrange(4000)]  # create an array
u_list_5 = [i for i in xrange(5000)]  # create an array
u_list_6 = [i for i in xrange(6000)]  # create an array
u_list_7 = [i for i in xrange(7000)]  # create an array
u_list_8 = [i for i in xrange(8000)]  # create an array
u_list_9 = [i for i in xrange(9000)]  # create an array
u_list_10 = [i for i in xrange(10000)]  # create an array

############################################################

# run the merge sort algorithm on the sorted lists
	
print "\nrunning merge sort on sorted lists"
	
t1 = time.time()
mergeSort(u_list_1)
print("%s" % (time.time() - t1))

t2 = time.time()
mergeSort(u_list_2)
print("%s" % (time.time() - t2))

t3 = time.time()
mergeSort(u_list_3)
print("%s" % (time.time() - t3))

t4 = time.time()
mergeSort(u_list_4)
print("%s" % (time.time() - t4))

t5 = time.time()
mergeSort(u_list_5)
print("%s" % (time.time() - t5))

t6 = time.time()
mergeSort(u_list_6)
print("%s" % (time.time() - t6))

t7 = time.time()
mergeSort(u_list_7)
print("%s" % (time.time() - t7))

t8 = time.time()
mergeSort(u_list_8)
print("%s" % (time.time() - t8))

t9 = time.time()
mergeSort(u_list_9)
print("%s" % (time.time() - t9))

t10 = time.time()
mergeSort(u_list_10)
print("%s" % (time.time() - t10))

