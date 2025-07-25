# Introduction to Python, Variables and Data Types

## What is Programming?

The process of preparing an instructional program for a device (such as a computer).

## What are Programming Languages?

It acts as a middle-man or translator for translating a program into machine code.

## How do computers perform tasks?

- To perform any task, we need 2 things
  - **The language that computers understand**
  - **Programming Environment**

## Programming Environment➖

- A programming environment combines hardware and software and allows a developer to build applications.
- Developers typically work in **integrated development environments or IDEs**.
- These connect users with all the features necessary to write and test their code correctly.
- Different IDEs will offer other capabilities and advantages.
- Examples of IDEs ➖ **Visual Studio, NetBeans, Eclipse, IntelliJ**, etc.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

| Term              | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Interpreted       | Executes code line-by-line, no need to compile                |
| Object-Oriented   | Supports class and object-based program structure             |
| High-Level        | Easy to read/write, abstracted from hardware                  |
| Dynamic Semantics | Variables don’t need types declared, type checking at runtime |

Created by Guido van Rossum in 1991 at CWI (Centrum Wiskunde & Informatica), Netherlands.

## General-Purpose Language

Python can be used for:

AI & Machine Learning

Data Science (Most popular choice!)

Web Development (Django/Flask frameworks)

Automation and Scripting

Famous Companies Using Python + Django:
YouTube, Spotify, Pinterest, Instagram, Dropbox

## Why the name “Python”?

Inspired by the BBC comedy “Monty Python’s Flying Circus”.
Guido wanted a name that was short, unique, and mysterious.

## Why Learn Python?

- Simple & Easy to Learn
- Dynamic and Powerful
- Huge Library Ecosystem (130,000+ packages)
- Free and Open Source
- Platform Independent
- Interpreted (no need to compile)
- Robust Exception Handling

## Indentation in Python

Python uses indentation to define blocks of code instead of curly braces {}.

```
    if True:
    print("This is indented correctly")
    ❌ Indentation error if not properly aligned.

```

---

## Note => The extension used for Python files is .py.

## Printing Output in Python

Use the built-in print() function:

```
    print("Hello, world!")
```

You can print strings, numbers, and variables.

## Python Comments

Used to explain code and prevent execution.

### Single-line comment:

```
# This is a comment
```

### Multi-line comment:

```
'''
This is
a multi-line comment
'''

```

## What is a Variable?

A named container to store data.

```
name = "Alice"
age = 25
```

Think of variables as boxes with labels.
(CASE SENSITIVE)

## Check Variable Type

```
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

Python is a fantastic language that automatically identifies the type of data for us.

## Rules for Declaring Variables

### Valid Names:

1. Must start with a letter or \_ (underscore)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age, Age, and AGE are different)

## Data Types in Python

<img src="./dataType.png" width="60%"/>

Can you store milk in a basket or can you use a bottle to store fruits?

We are using different types of containers to store different things.

While the bottle can hold milk or water or juice, it will hold only liquids.

Similarly,

- A variable of type **_string_** (like the variable - *custName*), can store only strings.
- A variable of type **int** (like the variable - *custAge)* can store only integers.
- A variable of type **boolean** (like the variable - *custMaritalStatus)* can store either true or false.
- A variable of type **float** (like the variable - fruitWeight*)* can store only decimal values.

*The type of data a variable can hold is called its* **Data type**.
It may be **int**, **string, boolean, float,** etc. (A variable of type Boolean can either be *True* or *False).*

| Data Type | Example         | Description     |
| --------- | --------------- | --------------- |
| `str`     | `"Alice"`       | Text values     |
| `int`     | `25`            | Whole numbers   |
| `float`   | `3.14`          | Decimal numbers |
| `bool`    | `True`, `False` | Logical values  |

## Type **Casting in Python**

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

There can be two types of Type Casting in Python –

- Implicit Type Casting
- Explicit Type Casting

### Implicit Type Casting

In this, Python **converts the data type** into another data type **automatically**. In this process, users don’t have to involve in this process.

### Explicit Type Casting

In this, Python needs **user involvement to convert the variable data type** into a certain data type in order to the operation required.

Mainly type casting can be done with these data type functions:

- i**nt(): i**nt() function take float or string as an argument and return int type object.
- **float():** float() function takes int or string as an argument and returns float type object.
- **str():** str() function take float or int as an argument and return string type object.
- **bool():** bool() function take float, string or int as an argument and return a boolean-type object. Number other than 0 change into True. Empty String change into False.

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line.

Ex➖

```
x,y,z= "box", "pencil", "eraser"

print(x)    # box
print(z)    # pencil
print(y)    # eraser
# The number of variables matches the number of values, or else you will get an error
```

## One Value to Multiple Variables

Python allows you to assign the *same* value to multiple variables in one line.

Ex➖

```cpp
a=b=c="Maggi"
print(a)    # Maggi
print(b)    # Maggi
print(c)    # Maggi
```

## Mathematical Operators

The mathematical operators in Python are :

- **Addition Operator**
- **Subtraction Operator**
- **Multiplication Operator**
- **Division Operator**
- **Modulo Operator** => gives the remainder
- **Exponentiation Operator** => compute the power of any number

## String Concatenation

- Concatenation means a series of interconnected things.
- Use **+** to join two or more string

```
  a="Hii...."
  b="Sam...."
  print(a+b)          # Hii....Sam....
```

## Comparison Operators

Comparison operators are used for comparing two values.

- There are 6 comparison operators:
  - **> (Greater Than)**
  - **>= (Greater Than Equal To)**
  - **< (Less Than)**
  - **<= (Less Than Equal To)**
  - **== (Equal)**
  - **!= (not Equal)**
- The result of a comparison operator is always a boolean value.

## Logical Operators

A logical operator is a symbol or word used to connect two or more expressions.

## Types of Logical Operators

Python provides three logical operators:

1. and
2. or
3. not

## Conditional Statements

Conditional Statements in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false.

- Conditional statements are used **to decide the flow of execution based on different conditions**. If a condition is true, you can perform one action and if the condition is false, you can perform another action.
- Through Conditional Statements, we can control which code needs to run or which code will not run.

For Example: the traffic light controls the flow of vehicles on the road.

- Depending upon the color of the light, the actions happened.
- If the light is green, then it is a signal to move.
- If the light is red then it is a signal to stop.

## Different Types of Conditional Statements

There are four types of conditional statements in Python.

1. If statement
2. If…Else statement
3. If…Elif…Else statement
4. Nested If

## Ternary Operator

- Ternary operators also known as **conditional expressions** are operators that evaluate something based on a condition being true or false.
- It was added to Python in version **2.5.**
- It simply allows testing a condition in a **single line** replacing the multiline if-else making the code compact.
- Syntax➖
  ```
  [on_true] if [expression] else [on_false]
  ```
- For ex-

  ```
  # to check whether a number is odd or even
  a=10;
  print("Even Number") if(a%2==0) else print("Odd Number");

  x = 5
  result = "Greater" if x > 10 else "Equal" if x == 10 else "Less"
  print(result)
  ```

## WHILE LOOP

```
  starting_point  # called as initialization

  while(till_when_he_will_jump):     # condition to terminate the loop

	# operation that is to be performed

	how_many_jump_at_a_time          # Increment/decrement
```

### Break

- **Break** means to come out of the loop and stop the execution.

### Continue

- **Continue** is basically saying go back to the condition.

## The else Statement with While in Python

With the else statement we can run a block of code once when the condition no longer is true:

```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## FOR LOOP

## NESTED LOOP

## DATA TYPES

### 1. Primitive Data Types (also called basic or built-in types)

These are the most **basic types of data**, directly supported by the Python language.

| Data Type | Description                      | Example         |
| --------- | -------------------------------- | --------------- |
| `int`     | Integer numbers                  | `10`, `-5`, `0` |
| `float`   | Decimal (floating point) numbers | `3.14`, `-0.1`  |
| `bool`    | Boolean values (True or False)   | `True`, `False` |
| `str`     | Text (string of characters)      | `"Hello"`       |

> **Note:** These are immutable (cannot be changed after creation).

---

### 2. Non-Primitive Data Types (also called complex or user-defined types)

These are built using primitive types.
They can store **multiple values** and offer **more functionality**.

| Data Type         | Description                     | Example                 |
| ----------------- | ------------------------------- | ----------------------- |
| `list`            | Ordered, mutable collection     | `[1, 2, 3]`             |
| `tuple`           | Ordered, immutable collection   | `(1, 2, 3)`             |
| `set`             | Unordered, unique items         | `{1, 2, 3}`             |
| `dict`            | Key-value pairs                 | `{"name": "Sam"}`       |
| `array`           | Like lists, from `array` module | `array('i', [1, 2, 3])` |
| `class`, `object` | Custom types defined by user    | OOP structures          |
| `function`        | Callable object                 | `def greet(): ...`      |

## What are Mutability and Immutability

### Mutability

In Python, mutability means you can directly modify an object after the creation
. For example, a list is a mutable object. After creating a list, you can add, modify, or remove elements from it.

### Immutability

In Python, immutability means you cannot directly modify an object after the creation
. For example, Tuple is an immutable object. After creating a tuple, you cannot add, modify, or remove elements from it.

## Sets

- Sets are used to store multiple items in a single variable.
- Sets are declared using { } without a colon.
- Set items are unordered (which means that the items in a set do not have a defined order), unchangeable (meaning that we cannot change the items after the set has been created), and do not allow duplicate values.
- No fetching possible (No Indexing and Slicing)
- We can add or delete the data.
- Data within the sets are automatically sorted.
- They contain only unique data. (**Data Duplication not possible**)
- **Syntax ⇒ `{** item1,item2, item3, ... }`
- **Example➖**
  ```python
  s={1,3,4,5,8}
  print(s)           # {1, 3, 4, 5, 8}
  print(type(s))     # <class 'set'>
  ```
- Since Sets consist of sorted and unique data, searching for a particular element within the set is very quick.

## Tuples

- Sibling of List
- **Immutable Data Object** ➖ Once you create the tuple, you can’t manipulate it. (no addition, deletion, or replacement)
- We can
  - Create Tuple
  - Indexing and Slicing
  - Create a new tuple by merging two or more tuples.
- A safer option for data collection
  - **Example** ⇒ Students’ marks if stored in a list manipulation can be possible (as addition, deletion, and changes are applicable) but Tuple is **immutable** hence, safer than a list
- When the objective is to collect the data and has no further objective of editing it ⇒ **Use TUPLE**

## Dictionary

- Python dictionary is an **ordered collection of items**.
- As of Python version 3.7, dictionaries are *ordered*. In Python 3.6 and earlier, dictionaries are *unordered*.
- Dictionaries are **optimized to retrieve values when the key is known.**
- A dictionary is a collection that is **changeable** and **does not allow duplicates**.
- Dictionaries are written **with curly brackets** and **have keys and values.**
- Holds data as **`key-value`** pair
- No concept of an index system and hence they are unordered.
- To fetch the data we use keys.
- A dictionary can’t have two keys with the same name. [ **keys must be unique and values can repeat**]
- Dictionaries are mutable, so we can
  - add a new key-value pair
  - replace the value not a key
  - delete a key-value pair
- **Syntax**➖
  ```python
  dict={
  	"key1": value,
  	"key2": "value",
  }
  ```

While the values can be of any data type and can repeat, keys must be of **immutable type (string, number, or tuple with immutable elements) and must be unique**.

## Functions

A block of code designed to perform a particular task; they are very useful in making code simplified and manageable.

```
  def channel_1():
      x="Sam";
      print(x);

  channel_1()
  channel_1()
  channel_1()
  channel_1()
```

### Default Arguments

### Variable-Length Arguments

### Keyworded Arguments => Arguments passed as name=value.

## Scope of Variables

### Local Scope

```
def greet():
    message = "Hello"
    print(message)  # message is local to this function

greet()
# print(message)  # Error: message is not defined
```

### Enclosing Scope (Nonlocal)

An enclosing scope refers to the scope of a function that contains another nested function.
Variables in this outer function are not local to the inner function, but they are not global either — they’re in the enclosing scope.

To access and modify a variable from an enclosing scope inside a nested function, we use the nonlocal keyword.
Without nonlocal, Python would treat message in inner() as a new local variable.

```
	def outer():
    msg = "Hello"

    def inner():
        nonlocal msg
        msg = "Hi"
        print("Inner:", msg)

    inner()
    print("Outer:", msg)

	outer()

```

### Global Scope

```
x = 10  # Global variable

def print_x():
    print(x)

print_x()
```

If modifying global:

```
x = 5

def change():
    global x
    x = 10

change()
print(x)  # Output: 10
```

### Built-in Scope

The built-in scope contains the names of all built-in functions, exceptions, and objects provided by Python. These are always available unless shadowed.

These come from the **builtins** module, and examples include:

```
  len()

  type()

  print()

  max(), min()

  sum()
```

Exception, ValueError, etc.

Python looks for a variable in this order: Local → Enclosing → Global → Built-in
print(len("Python")) # 'len' is a built-in function

## File Handling

### Files

- Files are a way to store data permanently on your computer.
- Python can open files, read their contents, write new information, and close them when done.
- Files can be text-based (like `.txt`), or more structured formats like `.csv`.

**Key Concepts:**

- **Opening a file:**
  Before reading or writing, we must open a file.
- **Closing a file:**
  After finishing with file operations, we close it, so the system knows we’re done and all changes are saved.
- **File Modes:**
  Determine how we interact with the file (read-only, write-new, append, etc.)

---

### Need of Files

If you need to store large amounts of data, user preferences, or logs, relying on variables isn’t enough. Files let you:

- Preserve data after the program ends.
- Share data between different runs of your program.
- Process bigger data sets that you can’t hard-code into variables.

```
  file = open("data.txt", "r")  # opens data.txt in read mode
  print(file)


  file.close()  # close the file after finishing
```

```
  with open("data.txt", "r") as f:
    content = f.read()
    print(content)
  # File is automatically closed after the with-block ends
```

## Multi Dimensional List

## OOPS

OOP is a programming paradigm that organizes code into **objects** that combine **data (attributes)** and **functions (methods)**.

Python supports OOP fully using the `class` keyword.

- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class containing data and behavior.

```python
class Person:
    def speak(self):
        print("Hello!")

p1 = Person()  # Object
p1.speak()

```

```
# Class => blue print  # Object => instance of the class
# Person => name , age  ,city fun => print all the things


class Person:
    # Class variables
    name = "Sam"

    def fun(self):
        print("Hi!...User", f"Bye...{self.name}")


#  Creating Object of Person class (instance of the class)
x = Person()
Y = Person()
x.fun()
Y.fun()


class Person:
    # Class variables
    city = "NewYork"

    def __init__(self, name):
        self.name = name  # Instance Variables
        print(f"Hi!....{name}, Welcome to {self.city}")

    def fun(self):
        print("Hi!...User", f"Bye...{self.name}")


#  Creating Object of Person class (instance of the class)
x = Person("SAM")
x.fun()

```

---
