import numpy as np
from Interfaces import Queue
 
class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0 # number of elements in the queue
        self.j = 0 # index of the first element
        self.a = self.new_array(1) # a = new array of size 1
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        new_capacity = max(1, 2*self.n) # Step 1, create a new array of size 2n and then set b to be the new array
        b = self.new_array(new_capacity) 
        for k in range(0, self.n): # Step 2, copy the elements from the old array to the new array
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b # Step 3, set a to be the new array
        self.j = 0 # Step 4, set j (The head) to be 0
 
    
    def add(self, x: object):
        '''
            Add element x to the end of the queue
        '''
        if self.n == len(self.a): # Invariant also the precondition
            self.resize()
        end_index = (self.j + self.n) % len(self.a) # Step 1, get the index of the last element
        self.a[end_index] = x # Step 2, add the element to the end of the queue
        self.n += 1 # Step 3, Increment the number of elements by 1
        return True
 
            
 
    def remove(self) -> object :
        
        '''
            remove the first element in the queue
        '''
        if self.n <= 0: # Precondition
            raise IndexError("remove from empty queue")
        x = self.a[self.j % len(self.a)] # Step 1, get the first element by letting a be the value at index j
        # self.a[self.j] = None # For garbage collection
        self.j = (self.j + 1) % len(self.a) # Step 2, increment the index by 1
        self.n -= 1 # Step 3, decrement the number of elements
        if len(self.a) > 3*self.n: # Invariant, check if it holds
            self.resize()
        return x # Step 4
        
        
    def size(self) :
        return self.n
 
    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"
 
    def __iter__(self):
        self.iterator = 0
        return self
 
    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
