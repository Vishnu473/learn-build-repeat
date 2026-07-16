def func():
    print("Hello")

func()

# Real functions can take parameters and return values. Here's an example of a function that takes two numbers as parameters and returns their sum:
def function_name (param1, param2):
    # statements can be exexuted here
    value = param1 + param2
    # return statement can be used to return a value from the function
    return value

# calling the function and storing the returned value in a variable
result = function_name(5, 10)
print(result)


# Functions can have default parameters, keyword parameters, and variable-length parameters. 
# During function calling, we can/must pass arguments to the functionin the same order as the functionparameters are defined.

# Difference between Parameters and Argumeters?
# Parameters - The variables that are defined in the function definition are called parameters. They are used to accept values when the function is called.
# Arguments - The values that are passed to the function when it is called are called arguments.

# Default parameters are parameters that have a default value, if no value is provided as an argument during function call.
# Ex: func_name() => func_name(param1=default_value1, param2=default_value2)

# Keyword parameters are parameters that are passed to the function using the parameter name, allowing us to specify the value for a specific parameter without following the order of parameters.
# Ex: func_name(param2=value2, param1=value1) => func_name(param1=value1, param2=value2)

# Variable-length parameters allow us to pass a variable number of arguments to a function. In Python, we can use *args for variable-length positional arguments and **kwargs for variable-length keyword arguments.
# Ex: func_name(*args) => func_name(arg1, arg2, arg3, ...)
# Ex: func_name(**kwargs) => func_name(param1=value1, param2=value2, ...)

# Note:
# The order of parameters in a function definition should be as: 
# required parameters, default parameters, variable-length positional & keyword parameters

# Let's see those examples in action with a practical example:

# See the order of parameters in the function definition below:
def add_numbers(a, b=0, *args, **kwargs):
    total = a + b
    for num in args:
        total += num
    for key, value in kwargs.items():
        total += value
    return total

def subtract_numbers(a,b,*args):
    result = a - b
    for num in args:
        result -= num
    return result

def multiply_numbers(*args):
    total =1
    for num in args:
        total *= num
    return total

def divide_numbers(*args):
    try:
        if not args:
            return 0
        total = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero.")
            total /= num
        return total
    except ValueError as e:
        print(e)
        return None

def power_numbers(base, exponent=1):
    return base ** exponent

# We can even pass function as an argument to another function. This is called higher-order functions.
# Ex: func_name(func1, func2,...) => func_name(func1(), func2(), ...)

def calculator(func, *args):
    return func(*args)

result = calculator(power_numbers, 2, 3)
print(result) # returns 8

# Now, Let's take the input from the user and pass them to calculator function.
# User will choose the operation too.

operation = int(input("Choose an operation: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power: "))
numbers_count = int(input("Enter the number of numbers you want to perform the operation on: "))

if numbers_count < 1:
    print("Number of numbers should be at least 1.")
    exit()

numbers = []
while numbers_count > 0:
    input_number = int(input("Enter the number: "))
    numbers.append(input_number)
    numbers_count -= 1

if operation == 1:
    result = calculator(add_numbers, *numbers)
    print(f"The sum of the numbers is: {result}")
elif operation == 2:
    result = calculator(subtract_numbers, *numbers)
    print(f"The difference of the numbers is: {result}")
elif operation == 3:
    result = calculator(multiply_numbers, *numbers)
    print(f"The product of the numbers is: {result}")
elif operation == 4:
    result = calculator(divide_numbers, *numbers)
    print(f"The quotient of the numbers is: {result}")
elif operation == 5:
    base = numbers[0]
    if len(numbers) == 1:
        print("For one number, the exponent will be considered as 1.")
        exponent = 1
    else:
        if len(numbers) > 1:
            exponent = numbers[1]

    result = calculator(power_numbers, base, exponent)
    print(f"The result of {base} raised to the power of {exponent} is: {result}")

print("Successfully completed the operation.")