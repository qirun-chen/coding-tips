
## The ways to write better Python

-- A Summary From Effective Python By Brett Slatkin

### Know the Differences Between bytes, str, and unicode
In python 3, there are two types that represent sequences of characters: *bytes* and *str*.
Instance of bytes contain raw 8-bit values.
Instance of str contain Unicode characters.

The most common way to represent Unicode characters as binary data (raw 8-bit values) is encoding UTF-8.
Importantly, *str* instances in Python 3 do not have an associated with binary encoding. 
To convert Unicode characters to binary data, you must use the encode method.
To convert binary data to Unicode characters, you must use the decode method.

The core of your program should use Unicode character types (*str*) and should not assume anything about character encodings.

In Python 3, you'll need one helper method that takes a *str* or *bytes* and always returns a *str*.

	def to_str(bytes_or_str):
		if isinstance(bytes_or_str, bytes):
			value = bytes_or_str.decode('utf-8')
		else:
			value = bytes_or_str
		return value  # Instance of str

You'll need another helper method that takes a *str* or *bytes* and always returns a *bytes*.

	def to_bytes(bytes_or_str):
		if isinstance(bytes_or_str, str):
			value = bytes_or_str.encode('utf-8')
		else:
			value = bytes_or_str
		return value  # Instance of bytes

There is one big gotcha when dealing with  raw 8-bit values and Unicode characters in Python 3.
Operations involving file handles (returned by the *open* built-in function) default to UTF-8 encoding. For example, say you want to write some random binary data to a file. This breaks.
You must indicate that the data is being opened in write binary mode **('wb')** instead of write character mode **('w')**.

	with open('tmp/random.bin', 'wb') as f:
		f.write(os.urandom(10))

This problem also exists for reading data from files. The solution is the same: Indicate binary mode by using **'rb'** instead of **'r'** when opening a file.

### Write Helper Functions Instead of Complex Expressions

	my_values = {'red': ['5'], 'green': [''], 'blue': ['0']}

	## version_1
	my_values.get('red')  # => ['5']
	my_values.get('green')  # => ['']
	my_values.get('opacity')  # => None

	## version_2
	## using 'or' expression to deal with the empty string like ''
	## the empty string implicitly evaluates to False, causing the 'or' expression to evaluate to 0
	red = my_values.get('red', [''])[0] or 0
	green = my_values.get('green', ['']) or 0
	opacity = my_values.get('opacity', ['']) or 0
	>>> 
	red: '5'
	green: 0
	opacity: 0

	## version_3
	## want to ensure that all the parameter values are integers so you can use them in mathematical expressions.
	red = int(my_values.get('red', [''])[0] or 0)
	## this is now extremely hard to read. there are so much visual nosie.

	## version_4
	red = my_values.get('red', [''])
	red = int(red[0]) if red[0] else 0
	## but if/else statement over multiple lines

	## version_5
	## Writing a helper function is the way to go, especially if you need to use this logic repeatedly.
	def get_first_int(values, key, default=0):
		found = values.get(key, [''])
		if found[0]:
			found = int(found[0])
		else:
			found = default
		return found

	green = get_first_int(my_values, 'green')

As soon as your expressions get complicated, it's time to consider splitting them into smaller pieces and moving logic into helper functions. What you gain in readability always outweighs what brevity may have afforded you.

### Slice Sequences
`somelist[start:end]`, where `start` is inclusive and `end` is exclusinve

Slicing deals properly with `start` and `end` indexes that are beyond the boundaries of the list. That makes it easy for your code to establish a maximum length to consider for an input sequence.

	first_tweenty_items = a[:20]
	last_tweenty_items = a[-20:]

The result of slicing a list is a whole new list. References to the objects from the orignial list are maintained. Modifying the result of slicing won't affect the original list.

`somelist[start:end:stride]`. take every *n*th item when slicing a sequence. For example, the stride makes it easy to group by even and odd indexes in a list.

`::2` means select every second item starting at the beginning.
`::-2` means select every second item starting at the end and moving backwards.

Specifying `start`, `end`, and `stride` in a slice can be extremely confusing.
Prefer using positive `stride` values in slices without `start` or `end` indexes.
Avoiding using `start`, `end`, and `stride` together in a single slice. If you need all three parameters, consider doing two assignments (one to slice, another to stride)

### Avoid More Than Two Expressions in List Comprehensions
	squared = [[x**2 for x in row] for row in matrix]
	print(squared)
	>>>
	[[1, 4, 9], [16, 25, 36], [49, 64, 81]]

The rule of thumb is to avoid using more than two expressions in a list comprehension. This could be two conditions, two loops, or one condition and one loop.

### Consider Generator Expressions for Large Comprehensions
For example, say you want to read a file and return the number of characters on each line. Doing this with a list comprehension would require holding the length of every line of the file in memory. If the file is absolutely enormous or perhaps a never-ending network socket, list comprehension are problematic.
To solve this, Python provides `generator` expressions, a generalization of list comprehensions and generators. 
Syntax between `()`

	it = (len(x) for x in open('/tmp/my_file.txt'))

The returned iterator can be advanced one step at a time to produce the next output from the generator expression as needed (using the next built-in function)

	print(next(it))
	>>>
	100

When you are looking for a way to compose functionality that's operating on a large stream of input, generator expressions are the best tool for the job. The only gotcha is that the iterators returned by generator expressions are stateful.

### Prefer enumerate Over range

The range built-in function is useful for loops that iterate over a set of integers.
	
	# using range to get index of list is hard to read.
	flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
	for i in range(len(flavor_list)):
		flavor = flavor_list[i]
		print('%d: %s' % (i + 1, flavor))

The `enumerate` built-in function for addressing this situation. `enumerate` wraps any iterator with a lazy generator. This generator yields pairs of the loop index and the next value from the iterator.
	
	for i, flavor in enumerate(flavor_list):
		print('%d: %s' % (i + 1, flavor))

	>>>
	1: vanilla
	2: chocolate
	3: pecan
	4: strawberry

You can make this even shorter by specifying the number from which `enumerate` should begin counting (1 in this case).

	for i, flavor in enumerate(flavor_list, 1):
		print('%d: %s' % (i + 1, flavor))

### Use zip to Process Iterators in Parallel
	names = ['Cecilia', 'Lise', 'Marie']
	letters = [len(n) for n in names]

The items in the derived list are related to the items in the source list by their indexes.

`zip` built-in function wraps two or more iterators with a lazy generator. 
	
	longest_name = None
	max_letters = 0
	for name, count in zip(names, letters):
		if count > max_letters:
			longest_name = name
			max_letters = count

But `zip` behaves strangely if the input iterators are of different lengths.
	
	names.append('Rosalind')
	for name, count in zip(names, letters):
		print(name)
	>>>
	Cecilia
	Lise
	Marie

It keeps yielding tuples until a wrapped iterator is exhausted.


### Take Advantage of Each Block in try/except/else/finally
#### Finally Blocks
One common usage of try/finally is for reliably closing file handles.

	handle = open('/tmp/random_data.txt')	# May raise IOError
	try:
		data = handle.read()	# May raise UnicodeDecodeError
	finally:
		handle.close()	# Always runs after try:

#### Else Blocks
The `else` block helps you minimize the amount of code in the `try` block and improves readability.

	def load_json_key(data, key):
		try:
			result_dict = json.loads(data)	# May raise ValueError
		except ValueError as e:
			raise KeyError from e:
		else:
			return result_dict[key]		# May raise KeyError

#### Everything Together
Use `try/except/else/finally` when you want to do it all in one compound statement.
	
	UNDEFINED = object()

	def divide_json(path):
		handle = open(path, 'r+')	# May raise IOError
		try:
			data = handle.read()	# May raise UnicodeDecodeError
			op = json.loads(data)	# May raise ValueError
			value = (
				op['numerator'] /
				op['denominator'])	# May raise ZeroDivisionError
		except ZeroDivisionError as e:
			return UNDEFINED
		else:
			op['result'] = value
			result = json.dumps(op)
			handle.seek(0)
			handle.write(result)	# May raise IOError
			return value
		finally:
			handle.close()			# Always runs

This layout is especially useful because all of the blocks work together in intuitive ways. For example, if an exception gets raised in the `else` block while rewriting the result data, the `finally` block will still run and close the file handle.

1. The `try/finally` compound statement lets you run **cleanup** code regardless of whether exceptions were raised in the `try` block.
2. The `else` block helps you *minimize the amount of code in `try` blocks* and *visually distinguish the success case* from the `try/except` blocks.
3. An `else` block can be used to perform additional actions after a successful `try` block but before common cleanup in a `finally`blcok.











