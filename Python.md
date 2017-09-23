## python tips


### File directory character in different operational systems
use `os.sep` instead of '/' in OS X or '\\' in windows.

### List comprehension

    e**2 for e in a_list if type(e) == types.Int`

output: expression `e**2`  

variable: `e`   

predicate: `if type(e) == types.Int`          



### Formularize print

    sale.statement = '{} bought a cuppa tea.'   
    sale.record = {'person':'Ryan'}     
    print (sale.statement.format(sale.record['person']))    
  
It turns out `Ryan bought a cuppa tea.`   
