__________________________________________________________PYTHON CODING TUTORIAL_________________________________________________________
                                                            --RISHABH SOOD--

Date Created: 23/07/2019
_________________________________________________________________________________________________________________________________________

Note: Indentation is very important in python. Indentation can be considered equally important to semicolon and curly braces in C++, Java.
-> Comments start with a # in python
-> Multi Line comments can be written by starting and ending with triple quotes: """ This is a..
                                                                                                 multi-line comment """
_________________________________________________________________________________________________________________________________________

variables:

-> Unlike other programming languages, Python has no command for declaring a variable. 
          # A variable is created the moment you first assign a value to it.
-> variables can change data types even after being assigned a value.
-> multiple variables can be assigned values in one go by seperating with commas. Example:
   
                               var_1,var_2,var_3 = val_1,val_2,val_3
-> The type of the variable can however be accesed by printing type(var_name).
-> inter-numeric data type conversion can be acheived like this:
                                                #convert from int to float:
                                                      a = float(x)
 
                                                #convert from float to int:
                                                      b = int(y)

                                                #convert from int to complex:
                                                      c = complex(x)
                                                #convert from int to string:
                                                      c = str(x)
_________________________________________________________________________________________________________________________________________

Output:

-> Output can be acheived by using the method print:  print("text")
-> also, variable values can also be printed: print(var_1)
-> further multiple variables and text can be linked up: print("text " , var_1 , "some more text" , var_2)

_________________________________________________________________________________________________________________________________________

Strings:

-> String literals can be defined by wrapping text in either double quotes ("") or single quotes ('').
-> multi-line strings can be defined by wrapping in triple double/single quotes ((""" """) or (''' ''')).
-> Strings in python too are arrays.
-> any character at index i, can be accessed : str_name[i].
-> or, a section of string from index i to k can be accessed: str_name[i:k].
-> Methods:
            -> len() method: len(str_name) returns length of the string str_name.
            -> lower()/upper() methods: lower(str_name)/upper(str_name) returns strings in upper/lower case respectively.
            -> replace() method: str_name.replace("old substring","new substring") replaces old substring in the string with the new 
               substring.
          # -> split() method: str_name.split(",") splits the string on instances of separator, that is a comma or space, etc.
            -> format() method: In order to combine numerals and strings, we use the format() method.
               working: The format() method takes the passed arguments, formats them, and places them in the string where the 
               placeholders {} are.

               This is how it is applied:
               >string = "whatever you want to type {2} {1} {0}"    #the numbers inside the placeholders define the index.
               >print(string.format(num_0,num_1,num_2)); 
               The output now will be:                           (say num_0 = 0 , num_1 = 1 , num_2 = 2)
               >whatever you want to type 2 1 0 
-> we can also specify number of decimals, by using :.2f in the curly braces.

_________________________________________________________________________________________________________________________________________

Opertaors:

-> Note: Basic operators like addition have been excluded from this tutorial.
-> Exponentiation operator: **, Example: x**y is equivalent to x^y.
-> Membership operators:
     ----------------------------------------------------------------------------
    | Operator	|             Description	                     |     Example   |
     ----------------------------------------------------------------------------
    |           |                                                |               |
    |   in 	    |Returns True if a sequence having the specified |               |
    |           |value is present in the object	                 |     x in y	 |
    |           |                                                |               |
    |  not in	|Returns True if a sequence having the specified |               |
    |           |value is not present in the object	             |   x not in y  |
     ----------------------------------------------------------------------------

_________________________________________________________________________________________________________________________________________

Collections (arrays):

-> Python namingly has four Collections:
            1. List is a collection which is ordered and changeable. Allows duplicate members.
            2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
            3. Set is a collection which is unordered and unindexed. No duplicate members.
            4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

-----------------------------------------------------------------------------------

List:

-> A list in python is defined in square brackets. Here is the basic syntax: list_name = ["item_1","item_2","item_3"]
-> List items can be accessed by their index number.
-> Here is how to loop through list items:
   > for x in list_name:
   >   print(x)
-> item_name in list_name, checks wether item belongs to the list.
-> len(list_name) returns the length of the list.
-> adding items to the list and removing items from the list:
            -> append(): This method appends an item to the end of the list. Syntax : > list_name.append(item_name)
            -> insert(): This method inserts an item to the list at an specified index. Syntax : > list_name.insert(index , item_name) 
            -> remove(): This method removes the specified item from the list. Syntax : > list_name.remove(item_name)
            -> pop(): This method removes the last item of the list or, if index specified, the corresponding item. Syntax : > list_name.pop(index)
            -> del: This keyword is used to delete the item corresponding to the specified index, or if not specified, the entire list. 
               Syntax : del list_name[index]
            -> clear():This method empties the list. Syntax : > list_name.clear()
-> Copying a list to another one:
            -> copy(): > list_new = list_old.copy()
            -> list(): > list_new = list(list_old)
-> additional built in methods: 
            -> count(): This function returns the number of elements with the specified value. list_name.count(item_name).
            -> extend(): This method adds the elements of a list (or any iterable), to the end of the current list.
               Syntax: list_current.extend(list_other) #The other list is appended to end of the current list.
            -> index(): Returns indes of the first element with the specified value. Syntax : list_name.index(item_name)
            -> reverse(): Reverses the order of the list. Syntax : list_name.reverse()
            -> sort(): Sorts the list. Syntax : list_name.sort()

-----------------------------------------------------------------------------------

Tuple:

-> Used for constant collections, which aren't going to change throughout the programme execution.
-> A Tuple in python is defined in circle brackets. Here is the basic syntax : tuple_name = ("item_1","item_2","item_3")
-> Tuple items can be accessed by their index number.
-> Here is how to loop through Tuple items:
   > for x in tuple_name:
   >   print(x)
-> item_name in tuple_name, checks whether item belongs to the Tuple. 
-> len(tuple_name) returns the length of the Tuple.
-> del : This keyword is used to delete the entire Tuple. 
               Syntax : del tuple_name[]
-> additional built in methods: 
            -> count(): This function returns the number of elements with the specified value. tuple_name.count(item_name).
            -> index(): Returns indes of the first element with the specified value. Syntax : tuple_name.index(item_name)

-----------------------------------------------------------------------------------

Sets:

-> A set in python is defined by placing the items in curly braces. Here is how to define a set: set_name = {"item_1","item_2","item_3"}
-> As sets are unordered, when printed their output order is random.
-> As elements are unindexed and unordered, we cannot access elements directly.
-> However we can loop through them:
    > for x in set_name:
    >   print(x)
-> Or, check if the element belongs to the set: item_name in set_name
-> adding items to the set and removing items from the set:
            -> add(): This method may be used to add a single element to the set. Syntax : set_name.add(item_name)
            -> update(): This method may be used to add multiple elements to the set. Syntax : set_name.update(["item_1","item_2","item_3"])
            -> remove()/discard(): Syntax : set_name.remove(item_name)/discard(item_name)
               difference in the two: If the specified element does not exist in the set, the method remove  generates an error, while discard()
               does not.
            -> pop(): Removes the last element of the set. However, the set being unordered, the deleted element is random. The method however,
               does return the value of the deleted element. Syntax : set_name.pop()
            -> clear(): Clears the set of its elements. Syntax : set_name.clear()
-> del : This keyword deletes the set itself. Syntax : del set_name
-> additional built in methods: 
            -> copy(): Returns a shallow copy of the set. Syntax : set_name.copy()
            -> difference(): Returns a set containing the difference of two or more sets. Syntax : set_primary.difference(set_secondary)
            -> difference_update(): Updates the primary set removing elements common with the secondary set.
               Syntax : set_primary.difference_update(set_secondary)
            -> intersection(): Returns a set which is intersection of the two or more sets. Syntax : set_1.intersection(set_2,set_3..)
            -> intersection_update(): Removes the items in this set that are not present in other, specified set(s). 
               Syntax : set_1.intersection_update(set_2,set_3..)
            -> isdisjoint(): Returns whether two sets have a intersection or not. Syntax : set_1.isdisjoint(set_2)
            -> issubset(): Returns whether another set contains this set or not. Syntax : set_1.issubset(set_2)
            -> issuperset(): Returns whether this set contains another set or not. Syntax : set_1.issuperset(set_2)
            -> union(): Returns a union of the two specified sets. Syntax : set_1.union(set_2,set_3,...)

-----------------------------------------------------------------------------------

Dictionaries:

-> A dictionary in python is defined by placing the colon seperated key and value groups inside curly braces. Example:
   dict_name = {
           key_1:value_1,
           key_2:value_2,
           ...
   }
-> As indexing is defined by the user itself, elements are easily accesible. Example:
   dict_name[key_name] or dict_name.get(key_name)
-> Values pertaining to keys can be changed.
-> Here is how to loop through Dictionary items:
   KeyNames:
   > for x in dict_name:
   >   print(x)
   Values:
   > for x in dict_name:
   >   print(dict_name[x])
   Both:
   > for x,y in dict_name.items():
   >   print(x,y)
-> key_name in dict_name, checks whether key belongs to the Dictionary.
-> adding items to the dictionary and removing items from the dictionary:
            -> adding items: dict_name[new_key] = new_value 
            -> update(): dict_name.update({key_name:item_name})
            -> pop(): The pop() method removes the item with the specified key name: Syntax : dict_name.pop(key_name)
            -> popitem(): Removes the last inserted item. Syntax : dict_name.popitem()
            -> clear(): Empties the dictionary completely. Syntax : dict_name.clear()
-> del : This keyword is used to delete the item corresponding to the specified index, or if not specified, the entire dictionary. 
               Syntax : del dict_name[index]
-> additional built in methods: 
            -> copy(): Returns a shallow copy of the dictionary. Syntax : dict_name.copy()
            -> fromkeys(): Returns a dictionary with specified keys and values. Example:
               > x = ('key_1', 'key_2', 'key_3')
               > y = (val_1 , val_2 , val_3)
               > thisdict = dict.fromkeys(x, y)
            # other methods may be referenced on-line. They haven't been stated here, due to their little or no use.

_________________________________________________________________________________________________________________________________________
   
If ... Else

-> These are condition based statements
-> Namely, there are three: > if: initial condition
                            > elif: if specified condition in previous case is not true.
                            > else: if none of the specified conditions are true.
-> Syntax: >if condition...:
           > code block...
           >elif condition...:
           > code block...
           >else:
           > code block...
-> Short hand:
           -> if-else: action_true if condition else action_other if condition else action_other2
           -> if: if condition: action_true
-> And,Or:
           -> unlike c++, we do not use && and || for # and, or
           -> We simply use and & or

_________________________________________________________________________________________________________________________________________

While Loop:

-> Continues re-iterating itself until givem condition becomes false, or it encounters break
-> Syntax:
   > while condition:
   >   code block...
-> break : To break the loop if  a particular condition is encountered.
-> continue : To skip the current iteration of the loop for a particular condition.

_________________________________________________________________________________________________________________________________________

For Loop:

-> For loop in python do not require the iterating variable to be pre-defined.
-> Syntax:
          -> Strings: > for var_name in "str_text":
                      >   code block...
          -> Collections: > for var-name in collection_name:
                          >   code block...
          -> specified number of iterations: > for var_name in range(start_index,end_index,step)
                                             >   code block... 

_________________________________________________________________________________________________________________________________________

Functions:

-> Syntax: 
          > def func_name(arguments...)
          >   code block...
          >   return statement...
-> In function definition, the function can call itself.

_________________________________________________________________________________________________________________________________________

Lambda Function:

-> Lambda function in python is an inline anonymous function.
-> A lambda function can be defined like this: 
                                              > var_name = lambda arg_1,arg_2,arg_3 : return value
-> new functions can be derived from a Lambda function, by fixing some of its arguments.

_________________________________________________________________________________________________________________________________________

Classes and Objects:

-> To create a Class, we use the keyword: class
-> Example:
           > class class_name:
           >   code block...
-> To create an object of a Class, we do the following: object_name = class_name()
-> Constructor: in order to directly initialize the object created, one should define the __init__() function.
   Syntax: > def __init__(self,arg_1,arg_2,...)
           >   self.feat_1 = arg_1
           >   self.feat_2 = arg_2
           >   ...
-> Then we could give the arguments as follows, while creating the object: object_name = class_name(arg_1,arg_2,...)
-> The self parameter can be exchanged with any name.
-> A function defined inside a class, must have self as an argument, in order to interact with the class features.
-> certain properties of a class which do not suit the object, may be deleted from the object definition,as follows:
         > del obj_name.property_name
-> The object may also be deleted by : del obj_name

_________________________________________________________________________________________________________________________________________

Inheritance:

-> Inheritance is means for inheriting data from one class (parent class) to others (child classes).
-> For directly inheriting from a parent class, we do the following:
     > class child_class(parent_class)
     >  self
-> Now, in order to add more features to the child_class, we must set up its own __init__() function, here is how we do it:
     > class child_class(parent_class)
     >   def __init__(self,arg_1,arg_2,new_one)
     >     parent_class.__init__(self,arg_1,arg_2)
     >     self.new_feat = new_one
     >   def newfunc(self)
     >     define func...
 ---------------------------------------------------------------------------------------------------------------------------------------
|Note: If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method| 
|will be overridden.                                                                                                                    |
 ---------------------------------------------------------------------------------------------------------------------------------------

_________________________________________________________________________________________________________________________________________

Iterators:

-> An iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
-> The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
-> The __next__() method also allows you to do operations, and must return the next item in the sequence.
-> An example of an integer printing iteration, via __iter__ and __next__:
   
                                            class MyClass:
                                              def __init__(self):
                                                self.a = 1

                                              def __iter__(self):
                                                return self

                                              def __next__(self):
                                                x = self.a
                                                self.a += 1
                                                return x


                                            obj = MyClass()
                                            obj_iter = iter(obj)

                                            for x in range(50):
                                              print(next(obj_iter))
-> Further, we can also setup conditions to stop iterations, inside the __next__() itself.
-> This is the syntax used: raise StopIteration
-> An example of a loop running through 20 iterations(only):
                            if self.a <= 20:
                              x = self.a
                              self.a += 1
                              return x
                            else:
                              raise StopIteration
-> the printing loop may now simply look like this:
         > for x in obj_iter
         >   print(x)

_________________________________________________________________________________________________________________________________________ 

Module

-> A module is basically a file you include in a code, to access its functions ,defined arrays , etc.
-> A module maybe imported as follows: import module_name
-> a module feature may then be used as follows: module_name.feature
-> If one wishes to use the module by another name, then , do the following: import module_name as name_desired
   #now you can access features by name_desired.feature
-> dir(module_name) returns all the function names (or variable names) in a module.
-> in order to only import a feature of the module, use the following syntax: from module_name import feature_name

_________________________________________________________________________________________________________________________________________

Input:

-> Taking user input in python is super easy. Simply do the following: reader_variable = input()

_________________________________________________________________________________________________________________________________________

Try and Except:

-> This is generally used for debugging 
-> syntax: 
          > try:
          >	  code block...
          > except error_type:
          >	  print("Error statement")
          > else:
          >   print("Error statement")
          > finally:
          >   print("Error statement")
-> Error types:
--------------------------------------------------------------------------------------------------------
AssertionError:	        Raised when the assert statement fails.
AttributeError:	        Raised on the attribute assignment or reference fails.
EOFError:               Raised when the input() function hits the end-of-file condition.
FloatingPointError:	    Raised when a floating point operation fails.
GeneratorExit:          Raised when a generator close() method is called.
ImportError:            Raised when the imported module is not found.
IndexError:	            Raised when the index of a sequence is out of range.
KeyError:               Raised when a key is not found in a dictionary.
KeyboardInterrupt:	    Raised when the user hits the interrupt key (Ctrl+c or delete).
MemoryError:            Raised when an operation runs out of memory.
NameError:              Raised when a variable is not found in the local or global scope
NotImplementedError:    Raised by abstract methods.
OSError:                Raised when a system operation causes a system-related error.
OverflowError:	        Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError:	        Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError:	        Raised when an error does not fall under any other category.
StopIteration:	        Raised by the next() function to indicate that there is no further item to be 
                        returned by the iterator.
SyntaxError:	        Raised by the parser when a syntax error is encountered.
IndentationError:	    Raised when there is an incorrect indentation.
TabError:	            Raised when the indentation consists of inconsistent tabs and spaces.
SystemError:	        Raised when the interpreter detects internal error.
SystemExit:	            Raised by the sys.exit() function.
TypeError: 	            Raised when a function or operation is applied to an object of an incorrect type.
UnboundLocalError:	    Raised when a reference is made to a local variable in a function or method, but
                        no value has been bound to that variable.
UnicodeError:	        Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError:	    Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError:	    Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError:	Raised when a Unicode-related error occurs during translation.
ValueError:	            Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError:	    Raised when the second operand of a division or module operation is zero.
--------------------------------------------------------------------------------------------------------
_________________________________________________________________________________________________________________________________________

File Handling:

-> Python has the following four modes for opening a file
   > "r" - read mode
   > "w" - write mode
   > "a" - append mode
   > "x" - create mode
-> Additionaly, the file type may also be specified:
   > "t" - text
   > "b" - binary
-> Syntax: file_var = open(file_name,"mode-file_type") # mode and file type have to be written together
-> File Reading: 
   > for complete file reading, we directly write  > var.read()
   > we can also specify in the brackets of the read function, the number of characters we want to read.
   > for returning a single line of a file > var.readline()
   > or, read the completete file line by line, as follows
                                                          > file_var = open(file_name,"mode-file_type")
                                                          > for var_2 in file_var
                                                          >     print(var_2)
   > finally do close the file by: var.close()
-> File Writing:
   > Syntax: file_var.write("Text to be written comes here...")
-> Deleting a file/folder:
   > firstly we will have to import the package os: import os
   > Next: os.remove("file_name")
   > To remove a folder, do: os.rmdir("folder_name")

_________________________________________________________________________________________________________________________________________

_________________________________________________________________________________________________________________________________________

