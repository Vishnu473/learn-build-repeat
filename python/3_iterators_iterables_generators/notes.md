# Iterables:
Iterables are the objects that can give python an Iterator when iter() is called and using this, they are looped. 
- All collections mostly we use are iterables - list, set, tuple, dictionary, string. Simply all the data types that can be looped are iterables with a small note. 
- An iterable is any object that implements __iter__() (or the sequence protocol). Collections are iterables, but not all iterables are collections.
- We can check that by using type() built-in function we learned on day-2.

- check the practice.py for more clarity.
- When we check the type of iterator using below, we can see how the iterables are looped on. Like in dictionaries, iterables are looped on keys and for strings based on unicode characters.

# Iterators:
Iterator is the object that follows the Iteration protocol and is with which the standard for loop is run in python behind scenes. Iterators maintains internally current state and position. Iterators can represent finite or infinite sequences.

**Iterator Protocol:** Any object to be considered as an iterator, it must implement the two methods - __iter()__ and __next()__

- __iter()__: This is needed so iterators can be used in loops. This returns the iterator object itself slightly different like dict_keyiterator and str_ascii_iterator as we saw in practice.py

- __next()__: This returns the next value/item in the sequence lazily(only when required/asked for). With this special dunder method only the iterators can reprsent the infinite sequences without system crash and not allocating the memory at start.

*Use of Iterators:*
- Memory Effecient
- Infinite sequences

Built-in-Iterators are used to extract the iterators from the built-in-iterables using iterator protocol.

*Why Iterables doesn't have Iterators features(from Iterators perspective)?*
- Iterables are the objects that can be looped, Iterators are the actual objects that performs the looping(traversal).
- Iterables must implement __iter()__ whereas iterators must implement both __iter()__ and __next()__.
- Iterables doesn't track the position, Iterations track both state and position.
- Iterable is passed to iter() to get iterator, Iterator is passed to next() to get the next item.

```
Ex: nums = [10,20,30] #iterable

it = iter(nums) # ierable is passed to iter() to create an iterator "it"

print(next(it)) #10
print(next(it)) #20
print(next(it)) #30

print(next(it)) #No value 
As the values/data in iterator are consumed/exhausted raising stopIteration exception 
```

Due to the above reason, the for loops never crash as stopIteration exception will be called when next() has no value to return.

Note: Remeber that next() gives the value or allocates memory only when needed dynamically not at the first.

# Yield:
Yield pauses the function execution, gives the value to the caller and saves the current state. When next call is called, it picks up from where it left off using the state.

This is due to which, the infinite mathematical sequence doesn't effect the system's memory. Allocates the memory for only one value/item at a time.

A function containing yield returns a generator object.

# Return:
Return desctroys the function's local state, gives the value and exits from the function permanently.
If we try to call list(range(100000)), the memory will have the impact as it needs to allocate space for total 100000 values in memeory.

Think of the return as the food you cook at home, it will be done once and it will be served the same(pre-heating) to you, mother and father when all three of you comes to eat different time. Yield is like a pizza house, where if you order pizza, it is cooked then at that time and serves you hot every time you order for a new one. Not like cooking all at once as return.