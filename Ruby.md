## Ruby tips

### Assign multiple variables
	a, b, c = row[0], row[1], row[2]

### Global variable

Should avoid using it.
Global variables begin with $. Uninitialized global variables have the value nil.
		
	$global_variable = 10

	class Class1
	   def print_global
	      puts "Global variable in Class1 is #$global_variable"
	   end
	end

	class1obj = Class1.new
	class1obj.print_global

NOTE − In Ruby, CAN access value of any variable or constant by putting a hash (#) character just before that variable or constant.

	Global variable in Class1 is 10
	Global variable in Class2 is 10

### The relationship between Ruby Variables

((((a_val ) @b ) @@c ) $d)
scope: 
	a_val -> local
	@b    -> within instance
	@@c   -> within class
	$d    -> application wide
	
-------------------------------------------------------------------------------------------------------------------------------------------

### Array frequently used functions
	
	
	foo = ["a", "b", "a1", "c", "b", "b", "c", "a"]

#### uniq

	>> foo.uniq
	=> ["a", "b", "a1", "c"]
	>> foo
	=> ["a", "b", "a1", "c", "b", "b", "c", "a"]

	>> foo.uniq!
	=> ["a", "b", "a1", "c"]
	>> foo
	=> ["a", "b", "a1", "c"]

	It turns out `uniq` does not change the original array, but `uniq!` does.	

#### join

Join taking a parameter can join all array elements with the parameter to a string.

	>> foo.join(" ")
	=> "a b a1 c"

#### inject

	>> foo
	=> ["a", "b", "a1", "c"]
	>> foo.inject {|a,b| a + b}
	=> "aba1c"
	>> [1,2,3,4,5].inject {|a,b| a + b}
	=> 15
	>> foo.inject {|a,b| [a,b]}
	=> [[["a", "b"], "a1"], "c"]

Inject applies a block to an array, take pair-wise elements, evaluates them and then passes the value as the 1st part of the next pair-wise comparison.

#### combining arrays
The simplest way is using '+', but '+' can only add two objects with the same class, and it cannot do assignment as well.
Use '<<' is flexible, it can add an object into an array and do assignment.

	>> arr = ["foo", "bar"]
	>> arr << "ff"
	=> ["foo", "bar", "ff"]
	>> arr
	=> ["foo", "bar", "ff"]

But.....if
	
	>> arr << ["jj"]
	=> ["foo", "bar", "ff", ["jj"]]

-------------------------------------------------------------------------------------------------------------------------------------------

#### ObjectSpace

Use objectSpace to inspect objects during runtime.
	
	>> ObjectSpace.each_object(foo)
	=> #<Enumerator: ObjectSpace:each_object(["a", "b", "a1", "c"])>

-------------------------------------------------------------------------------------------------------------------------------------------
### String frequently used functions

#### chomp 

Chomp takes care of control characters at the end, like `\n`. Eg. `"abc\n".chomp`. Chomp could eat the `\n` at the end of the string.

#### concat
Use concat to append a substring to the end of the string, and it will do assignment. In other languages, it is also an elegant way.

	>> str = "foo"
	>> str.concat("bar")
	=> "foobar"
	>> str
	=> "foobar"

#### Split
If split takes '//', it will split every single character into an array.

	>> "abcd".split(//)
	=> ["a", "b", "c", "d"]

-------------------------------------------------------------------------------------------------------------------------------------------
### Blocks
#### each
	>> foo = ["qi", "qa", "quo"]
	>> foo.each {|ele| puts ele+"e"}

#### select
It is like a filter.
	
	>> foo.select {|elo| elo.include?("a")}
	=> ["qa"]


-------------------------------------------------------------------------------------------------------------------------------------------
### def methods
#### splat `*`
Splat gathers all elements into an array. `*`

	def method_1(*sausages)
		puts sausages
	end

	method_1(saus1, saus2, saus3)

-------------------------------------------------------------------------------------------------------------------------------------------
### I/O
#### Loading CSV
	CSV.foreach("Titanic.csv") do |row|
		p row
	end

#### Assign parameters in command-line interface
ARGV is like an I/O splat

	$ ruby reader.rb a.csv b.csv c.csv
	# ARGV = ["a.csv", "b.csv", "c.csv"] 
