# Built-in-functions;
Learned and practiced some built-in-functions.

list = [10,20,30]

**1. aggregation functions:**

- *sum*: adds all the values in an iterable list.
ex: sum(list) #60

- *min*: returns minimum value from list.
ex: min(list) #10

- *max*: returns maximum value from list.
ex: min(list) #30

- *sorted*: sorts the list. ex: sorted(list) #[10,20,30] It also takes a key: reverse = True gives us descending order. ex: sorted(list, reverse=True) #[30,20,10]

- *reversed*: We also have a direct function that reverses the list or sorted one too. ex: reversed(sorted(list)) == sorted(list, reverse=True)

**2. Normal functions**
- print() = prints the values or displays output to console.
- len() = returns the length of the collection.
- help() = used in providing the help in python language.
- input() = used for taking the input from user.
- type() = gives us the type of the object like int, str, iterable
- id() = used to create an unique identifier for the given value.
 ex: x= 12 and id(x) gives the identifier to x.

**3. Collections:**
- range() = returns the sequence of numbers from start(inclusive) to end(exclusive) with the default step as 1, else we can use that too. ex: range(0,11,2) #0,2,4,6,8,10
-enumerate() = useful when we need both index and value at a time, best used instead of range() and accessing as list[i] from i in list. ex: for index,val in enumerate(list): #(0,10) (1,20) (2,30)
-zip() = takes iterables (can be zero or more), aggregates them in a tuple, and returns it. This function is used to combine two or more iterables (lists, tuples, etc.) element-wise. 

**4. Truthy Functions:**

-all() - checks for all the values in iterable evaluates to truthy value or not. if all are truthy values then true, else false.

ex: all(True, 'hello',1,1234.6,[]) #True

*Note:* Here [] also results in True as it doesn't contain non-truthy value.

-any() - similar to all() but it checks if any one value evaluates to true, if ues any() results True, else false.

ex: any(0,False,'',100) #True as 100 is Truthy value.

**5. Type conversions:**
These convert the type from one datatype to other.
ex: input() gives us the value entered by user as type-'str', so inorder to get integer values, we use int(input())

You can also take a lok at main.py file in this parent folder for the student_mark_analyzer practiced using built-in-functions.