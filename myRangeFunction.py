'''
a program, having

'''
#iterable
class myRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return myRangeIterator(self)
    
#iterator
class myRangeIterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start +=1
        return current


x = myRange(1,11)
for i in x:
    print(i)
        
print(type(x))
    
