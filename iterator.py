import sys
L = [x for x in range(1, 100000)]
print(sys.getsizeof(L)/1024)
print(type(L))
x = range(1, 100000) #iterator, not consuming memory, takes variable, performs operation, removes it frm the memory
print(sys.getsizeof(x)/1024)
print(type(x))