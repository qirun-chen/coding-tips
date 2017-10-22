## Python tips based on Python 3.3 or later 

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
^`iterable` : list, tuple, dictionary^
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
    # or we can easily get a line by the number
    f = open('data.txt', 'r')
    d = dict(enumerate(f))
    print(d[1])
    

--- 
## data science with python

### get intersection between sets, and get union of set
should initialize a set with a list
    
    set_1 = set(list_1)
    set_2 = set(list_2)
    set_1 & set_2 # intersection
    set_1 | set_2 # union

