# Built-in functions:

# print("Hello, World") #prints Hello world to the console
# username = input("Enter username:") #takes input from the user and stores it in the variable username
# user_name_type = type(username) #gets the type of the variable username and stores it in the variable username_type
# random_guid = id(username) #gets the unique identifier of the variable username and stores it in the variable random_guid
# length_of_username = len(username) #gets the length of the variable username and stores it in the variable length_of_username
# There is another function 'help()' which can be used to get help about any function or module in python. For example, help(len) will give you information about the len() function.

# print("Username:", username)
# print(f"Type:{user_name_type.__name__}, ID: {random_guid}, length: {length_of_username}") 

# -------------------------------------
# Collections:

num_list = range(0,11) #range() function returns a sequence of numbers starting from 0 and increments by 1 (by default) and stops before a specified number. In this case, it will return numbers from 0 to 10.
num_list_even = range(0,11,2)
num_list_reverse = range(10,-1,-1)

num_list_enum = list(enumerate(num_list)) #enumerate() function adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using the list() method.

num_list_zip = list(zip(num_list, num_list_even)) #zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it. This function is used to combine two or more iterables (lists, tuples, etc.) element-wise.

# print("Number list:", list(num_list))
# print("Even number list:", list(num_list_even))
# print("Reverse number list:", list(num_list_reverse))
# print("Enumerated number list:", num_list_enum)
# print("Zipped number lists:", num_list_zip)
# -------------------------------------
# Aggregate functions:

num_list = [23, 1, 56]

num_list_sum = sum(num_list)
num_list_max = max(num_list)
num_list_min = min(num_list)
num_list_sorted = sorted(num_list)
num_list_reversed = reversed(num_list)

# print("Number list:", num_list )
# print(f"Sum: {num_list_sum}, Max: {num_list_max}, Min: {num_list_min}, Sorted: {list(num_list_sorted)}, Reversed: {list(num_list_reversed)}")
# -------------------------------------
# Truthy Functions:

list_bool = [True, False, True ]
list_random = [1, 0, True, False, "Hello", "", None, [], {}, (1,2)]
list_false = [False, 0, "", None, [], {}, ()]
list_true = [True, 1, "Hello", [1,2], {1:2}, (1,2)]

list_bool_all = all(list_bool)
list_bool_any = any(list_bool)

list_random_all = all(list_random)
list_random_any = any(list_random)

list_false_all = all(list_false)
list_false_any = any(list_false)
list_true_all = all(list_true)
list_true_any = any(list_true)

print(f"List: {list_bool}, All: {list_bool_all}, Any: {list_bool_any}")
print(f"List: {list_random}, All: {list_random_all}, Any: {list_random_any}")
print(f"List: {list_false}, All: {list_false_all}, Any: {list_false_any}")
print(f"List: {list_true}, All: {list_true_all}, Any: {list_true_any}")
