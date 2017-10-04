## python tips


### File directory character in different operational systems
use `os.sep` instead of '/' in OS X or '\\' in Windows.


### List comprehension

    e**2 for e in a_list if type(e) == types.Int`

output: expression `e**2`  

variable: `e`   

predicate: `if type(e) == types.Int`          

Eg
use list comprehension to deal with dictionay objects

    eg_dict = {k: v for k, v in eg_dict.iteritems() if v == 4}
use ':' operator to add a pair of (key,value) into a dictionary

This syntaxtic sugar looks like a sentence in English. A pythonic way.


### Formularize print

    sale.statement = '{} bought a cuppa tea.'   
    sale.record = {'person':'Ryan'}     
    print (sale.statement.format(sale.record['person']))    
  
It turns out `Ryan bought a cuppa tea.`   


### String variable
String objects are immutable. 
We can use StringVar() to initialize a String variable which is more flexible. It provides accessible methods like set() and get().

    string_variable = StringVar()
    
### Start a local server
Cd your target directory, and then `python -m http.server 8082`.
Open your broswer, input http://localhost:8082/, and now you get access to files in the directory.
Use when your program has to get access to the local files. For example, Js code in html needs to open the local csv files.
 

