## Python tips based on Python 3.3 or later 

## `*arg, **kwargs`
`*args` is used to send a non-keyworded variable length of argument list to the function. 
`**kwargs` allows you to pass keyworded variable length arguments to a function. (keyword variables => list, dict)

    def greet_me(**kwargs):
        if kwargs is not None:   
            for key, value in kwargs.iteritems():
                print "%s == %s" %(key,value)
    >>> greet_me(name="yasoob")
    name == yasoob

    def test_args_kwargs(arg1, arg2, arg3):
        print "arg1:", arg1
        print "arg2:", arg2
        print "arg3:", arg3    

    # first with *args
    >>> args = ("two", 3,5)
    >>> test_args_kwargs(*args)
    arg1: two
    arg2: 3
    arg3: 5

    # now with **kwargs:
    >>> kwargs = {"arg3": 3, "arg2": "two","arg1":5}
    >>> test_args_kwargs(**kwargs)
    arg1: 5
    arg2: two
    arg3: 3     

So if you want to use all three of these in functions then the order is

    some_func(fargs,*args,**kwargs)

---
## List 
### List comprehension

    e**2 for e in a_list if type(e) == types.Int`

output: expression `e**2`

variable: `e`

predicate: `if type(e) == types.Int`

### List to String
	list = ['1', '2', '3']
	str1 = ''.join(list1)
	str1 = ''.join(str(e) for e in list1)

---
## String
### Formularize print

    sale.statement = '{} bought a cuppa tea.'
    sale.record = {'person':'Ryan'}
    print (sale.statement.format(sale.record['person']))

It turns out `Ryan bought a cuppa tea.`
#### format to take certain number of characters
    print("%s" % (format('x', '^20')
It means `x` takes space of 20 characters.
`^` can make it centered. `<` => align left. `>` => align right.

### String variable
String objects are immutable.
We can use StringVar() to initialize a String variable which is more flexible. It provides accessible methods like set() and get().

    string_variable = StringVar()

### Start a local server
Cd your target directory, and then `python -m http.server 8082`.
Open your broswer, input http://localhost:8082/, and now you get access to files in the directory.
Use when your program has to get access to the local files. For example, Js code in html needs to open the local csv files.

### Accuracy of float
	float（'%.4f' % float_variable）

---
## Dictionary
The dict() constructor can accept an iterator that returns a finite stream of (key, value) tuples:

    L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
    dict(iter(L))  
### dictionary comprehension

like list comprehension
    
    eg_dict = {k: v for k, v in eg_dict.iteritems() if v == 4}
use `:` operator to add a pair of (key,value) into a dictionary

This syntaxtic sugar looks like a sentence in English. A pythonic way.

### has_key() or in
Python 3 has removed `has_key()` of the dictionary object. Use `in` instead.

### find the key with the maximum
    mydict = {'A':4,'B':10,'C':0,'D':87}
    maximum = max(mydict, key=mydict.get)  # Just use 'min' instead of 'max' for minimum.
    print(maximum, mydict[maximum])
    # D 87

---
## I/O operations
### File directory character in different operational systems
use `os.sep` instead of `/` in OS X or `\\` in Windows.
`os.getcwd()` to get current directory

When reading a file, it may lead to some encodeing problems.
The best way to avoid this problem is to assign encodeing parameter with specific value like 'utf-8' when opening the file.

    raw_text = open(os.getcwd() + os.sep + file_name, encoding='utf-8').read()

---
## iterator
^`iterator` : list, tuple, dictionary^
---
## Generator
    line_list = ['  line 1\n', 'line 2  \n', ...]
    # Generator expression -- returns iterator
    stripped_iter = (line.strip() for line in line_list)
Generator expressions are surrounded by parentheses (“()”) and list comprehensions are surrounded by square brackets (“[]”).
### yield
The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved.

    def generate_ints(N):
       for i in range(N):
           yield i

    >>> gen = generate_ints(3)
    >>> gen  
    <generator object generate_ints at ...>
    >>> next(gen)
    0
    >>> next(gen)
    1
    >>> next(gen)
    2
    >>> next(gen)
---
## Lambda
sometimes using lambda to write a formula is an elegant way.

    sum = lambda x,y : x+y
    print sum(2)

### lambda with high order functions, filter, map, and reduce
#### filter ---- return a list with values satisfying filter conditions
after filtering, need to change the result(filter object) into an list object

    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    even_numbers = list(filter(lambda x: x % 2 == 0, foo))

#### map ---- return a list with values processed by the function
change the result into an list object as well.

    result = list(map(lambda x:x**2, foo))

#### reduce ---- continually apply the function to a list, and return a single value 
since python3 has dropped reduce, we need to `from functools import reduce`
    
    f = lambda a,b: a if (a>b) else b
    reduce(f, [47,11,42,102,13])
    # get 102
        
    reduce(lambda x,y: x+y, [47,11,42,13])
    # get 113

#### enumerate
`enumerate(iter, start=0)` counts off the elements in the iterable returning 2-tuples containing the count (from start) and each element.

    >>> for item in enumerate(['subject', 'verb', 'object']):
    ...     print(item)
    (0, 'subject')
    (1, 'verb')
    (2, 'object')

`enumerate()` is often used when looping through a list and recording the indexes at which certain conditions are met:

    f = open('data.txt', 'r')
    for i, line in enumerate(f):
        if line.strip() == '':
            print('Blank line at line #%i' % i)
    # or we can easily get a line according the index
    f = open('data.txt', 'r')
    d = dict(enumerate(f))
    print(d[1])
    
#### sum
    total = sum(b for a,b in items)

## iter()
The iter() method returns iterator object for the given object that loops through each element in the object.
How iter() works for custom objects?

    class PrintNumber:
        def __init__(self, max):
            self.max = max

        def __iter__(self):
            self.num = 0
            return self

        def __next__(self):
            if(self.num >= self.max):
                raise StopIteration
            self.num += 1
            return self.num

    printNum = PrintNumber(3)
    printNumIter = iter(printNum)

    # print '1'
    print(next(printNumIter))

    # print '2'
    print(next(printNumIter))

    # print '3'
    print(next(printNumIter))
---
## Decorators
We will use the `*args` and `**kwargs` notation to write decorators which can cope with functions with an arbitrary number of positional and keyword parameters.

    def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper
    
    @call_counter   # @ must on the line before the definition of the function 
    def succ(x):
        return x + 1
    
    @call_counter
    def mul1(x, y=1):
        return x*y + 1
    
    print(succ.calls)
    for i in range(10):
        succ(i)
    mul1(3, 4)
    mul1(4)
    mul1(y=3, x=2)
        
    print(succ.calls)
    print(mul1.calls)

    output: 
    0
    10
    3

or decorate build-in functions:

from random import random, randint, choice

    def our_decorator(func):
        def function_wrapper(*args, **kwargs):
            print("Before calling " + func.__name__)
            res = func(*args, **kwargs)
            print(res)
            print("After calling " + func.__name__)
        return function_wrapper

    random = our_decorator(random)            # cannot use @, its a build-in functions
    randint = our_decorator(randint)
    choice = our_decorator(choice)

    random()
    randint(3, 8)
    choice([4, 5, 6])    

The result looks as expected:    

    Before calling random
    0.16420183945821654
    After calling random
    Before calling randint
    8
    After calling randint
    Before calling choice
    5
    After calling choice
--- 
## data science with python

### get intersection between sets, and get union of set
should initialize a set with a list
    
    set_1 = set(list_1)
    set_2 = set(list_2)
    set_1 & set_2 # intersection
    set_1 | set_2 # union

