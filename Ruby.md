## Ruby tips

### Global variable

Global variables begin with $. Uninitialized global variables have the value nil.
		
	$global_variable = 10

	class Class1
	   def print_global
	      puts "Global variable in Class1 is #$global_variable"
	   end
	end

	class1obj = Class1.new
	class1obj.print_global

NOTE − In Ruby, you CAN access value of any variable or constant by putting a hash (#) character just before that variable or constant.

	Global variable in Class1 is 10
	Global variable in Class2 is 10