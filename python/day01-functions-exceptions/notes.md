# Day 1 - Functions & Parameters

## Objective

Learn how to write reusable code using functions and understand different ways of passing data to them.

---

## Concepts Learned

### 1. Functions

Functions allow us to group reusable logic and avoid writing the same code multiple times.

```python
def greet():
    print("Hello")
```

Functions can be called whenever needed.

---

### 2. Parameters vs Arguments

**Parameters** are variables defined in the function definition.

```python
def add(a, b):
```

`a` and `b` are parameters.

**Arguments** are the actual values passed to the function.

```python
add(5, 10)
```

`5` and `10` are arguments.

---

### 3. Return Values

Instead of printing results inside a function, a function should usually return the result.

```python
def add(a, b):
    return a + b
```

This makes the function reusable in different places.

---

### 4. Default Parameters

A parameter can have a default value.

```python
def power(base, exponent=1):
    return base ** exponent
```

If no exponent is passed, it defaults to `1`.

---

### 5. Variable-Length Arguments (`*args`)

`*args` allows passing any number of positional arguments.

```python
def multiply(*args):
```

Example:

```python
multiply(2, 3, 4)
```

Inside the function, `args` behaves like a tuple.

---

### 6. Keyword Arguments (`**kwargs`)

`**kwargs` accepts a variable number of keyword arguments.

```python
def add(**kwargs):
```

Example:

```python
add(a=10, b=20)
```

Inside the function, `kwargs` behaves like a dictionary.

---

### 7. Higher-Order Functions

Functions can be passed as arguments to other functions.

```python
def calculator(func, *args):
    return func(*args)
```

Example:

```python
calculator(add_numbers, 5, 10)
```

This makes programs more flexible and reusable.

---

### 8. Exception Handling

Used `raise` to stop invalid operations.

```python
if num == 0:
    raise ValueError("Cannot divide by zero.")
```

Also experimented with:

* `try`
* `except`

---

## Biggest Learning Today

An exception should usually be **raised inside the function** and **handled by the caller**, instead of catching it immediately inside the same function.

Instead of:

```python
def divide():
    try:
        ...
    except ValueError:
        ...
```

A better approach is:

```python
def divide():
    raise ValueError(...)
```

and let `main.py` or the calling function decide how to handle it.

This keeps the function focused on its responsibility.

---

## Mini Project

Built a command-line calculator supporting:

* Addition
* Subtraction
* Multiplication
* Division
* Power

Practiced:

* Functions
* Parameters
* `*args`
* `**kwargs`
* Default parameters
* Higher-order functions
* User input
* Lists
* Loops
* Basic exception handling

---

## Things to Improve Tomorrow

* Move exception handling to the caller instead of inside the function.
* Handle invalid user input using `try` and `except`.
* Separate business logic from user interaction (`calculator.py` and `main.py`).
* Improve validation for invalid operations.

---

## Key Takeaways

* Write functions that do one thing well.
* Return values instead of printing inside helper functions.
* Use meaningful function names.
* `*args` is useful when the number of inputs is unknown.
* `**kwargs` allows flexible keyword-based inputs.
* Higher-order functions make code reusable.
* Exceptions should be raised where the problem occurs and handled where the application decides how to respond.

