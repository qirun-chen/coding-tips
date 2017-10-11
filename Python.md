## Python tips

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
## Data Science with Python
### Nmupy Array index & slice
for large amounts of calls to numpy function, the standard approcah to import package:

    imoprt numpy as np

serveral function:
`zeros()` is used to create an array of all zeros.
`ones()` similar to `zeros()`, however the values inside array are all 1.
`full()` create a  constant array. (below: an 2-rows,2-lows array with values=7)

    a = np.full((2,2), 10)

`eye()` to create the identity matrix.
an example to create random metrix:

    a = np.random.rando((2,1))

#### Fancy slice
See the example below, the output of this is `[1 4 5]`, which is a combination of the value in `(0,0)`, `(1,1)` and `(2,0)` position.

    x = np.array([[1,2], [3,4], [5,6]])
    x[[0,1,2],[0,1,0]]

---


