def myOwnForLoop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print() #to move to next line so next customised for loop begins
            break
        
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = {1,2,3,4,5}
d = {0:1, 1:2}
e = range(1,6)
myOwnForLoop(a)
myOwnForLoop(b)
myOwnForLoop(c)
myOwnForLoop(d)
myOwnForLoop(e)        
