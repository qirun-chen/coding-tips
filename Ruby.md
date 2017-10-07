## Ruby tips

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

### ObjectSpace

Use objectSpace to inspect objects during runtime.
	
	>> ObjectSpace.each_object(foo)
	=> #<Enumerator: ObjectSpace:each_object(["a", "b", "a1", "c"])>

### chomp 
Chomp takes care of control characters at the end, like '\n'. Eg. `"abc\n".chomp`. Chomp could eat the `\n` at the end of the string.