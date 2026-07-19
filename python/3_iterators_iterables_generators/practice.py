# Iterables

from typing import Iterable

names = ["Alice", "Bob"] #list
marks = (10, 20) #tuple
numbers = {1, 2, 3} #set
student = {"name": "Vishnu"} #dictionary
laptop = "Dell" #string

it_names = iter(names)
it_marks = iter(marks)
it_numbers = iter(numbers)
it_student = iter(student)
it_laptop = iter(laptop)

print(type(it_names)) #<class 'list_iterator'>
print(type(it_marks)) #<class 'tuple_iterator'>

# print(next(it_marks)) #10
print(type(it_numbers)) #<class 'set_iterator'>
print(type(it_student)) #<class 'dict_keyiterator'>
print(type(it_laptop)) #<class 'str_ascii_iterator'>
# print(next(it_laptop)) #D

# Iterators
# Let's experiment with the iterators.

numbers = [11, 22, 33]

iterator1 = iter(numbers)
iterator2 = iter(numbers) 

# iterator1 and iterator2 are two different iterators for the same iterable.
# When we call next() on both iterator1 and iterator2, they are same, but maintaing their own state but same value. Confused?
# Think of a teacher explaining a concept to a group of students. Every student will have their own way of understanding and imagining, but the concept is same.
# So, When we call next() on both iterators they return same value but maintain their own state. Let;s see this in action:

a = next(iterator1)
print(a == next(iterator2), a) #True,11
b = next(iterator1)
print(b == next(iterator2), b) #True,22
c = next(iterator1)
print(c == next(iterator2), c) #True,33

print(type(iterator1), type(iterator2)) #<class 'list_iterator'> <class 'list_iterator'>
print(iterator1, iterator2) #<list_iterator object at 0x000001E4C7AC6890> <list_iterator object at 0x000001E4C7AC68C0>
# You can clearly see that both iterators are of same type and they are different objects in memory. So, they maintain their own state but return same value when we call next() on them.

# Example of using iterators using set and tuple and dictionary
# it_marks = iter(marks) using tuple
print(next(it_marks)) #10
print(next(it_marks)) #20

# it_numbers = iter(numbers) using set
print(next(it_numbers)) #1
print(next(it_numbers)) #2
print(next(it_numbers)) #3

# it_student = iter(student) using dictionary
print(next(it_student)) #name
# print(next(it_student)) #StopIteration error because there is only one key in the dictionary.

# it_laptop = iter(laptop) using string
print(next(it_laptop)) #D
print(next(it_laptop)) #e
print(next(it_laptop)) #l
print(next(it_laptop)) #l
# print(next(it_laptop)) #StopIteration error because there are only 4 characters in the string.

# Let's test whether we can perform same operations with zip and range ?
zip_numbers = zip([1, 2, 3], [4, 5, 6])
range_numbers = range(1, 4)

zip_iterator = iter(zip_numbers)
range_iterator = iter(range_numbers)

print(next(zip_iterator)) #(1, 4)
print(next(zip_iterator)) #(2, 5)
print(next(zip_iterator)) #(3, 6)
print(next(range_iterator)) #1
print(next(range_iterator)) #2
print(next(range_iterator)) #3
# print(next(range_iterator)) #StopIteration error because there are only 3 numbers in the range object.
# print(next(zip_iterator)) #StopIteration error because there are only 3 tuples in the zip object.

print(type(zip_numbers))
print(type(range_numbers))
# So, from this we can conclude that zip, range and enumerate also considered iterables 100% as they implement __iter__().
#An iterable is any object that implements __iter__() (or the sequence protocol). Collections are iterables, but not all iterables are collections.


# Build own Iterator

# Created an iterator that mimics the sqaures of the sequence
class MySquare:
    def __init__(self,limit):
        self.current = 1 #counter
        self.limit = limit

    def __iter__(self):
        return self  #iterator must return self as discussed.
    
    def __next__(self):
        if self.current < self.limit:
            val = self.current*self.current
            self.current += 1  #increasing the counter to move to the next item
            return val
        
        # calls when the sequence has ended
        raise StopIteration
    
squares = MySquare(4)
for sq in squares:
    print(sq)

class oddNumbers:
    def __init__(self,oddnumber:Iterable):
        self.current = 0
        self.oddnumber = oddnumber

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current < len(self.oddnumber):
            val = self.oddnumber[self.current]
            self.current += 1
            
            if val%2 != 0:
                return val

        raise StopIteration

my_list = [10,11,0,20,21,30,40]
for num in oddNumbers(my_list):
    print(num)

my_tuple = (10,21,32,43)
for t in oddNumbers(my_tuple):
    print(t)


# Create own enumerate:

class my_enumerate:

    def __init__(self,iterable:Iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.iterable):
            val = self.iterable[self.index]
            idx = self.index
            self.index += 1
            return idx, val #replace return with yield
        
        raise StopIteration
    
nums = [11,22,33,44,55]
for i,e in my_enumerate(nums):
    print(i,e)