
__________________________________________________________JAVA CODING TUTORIAL_________________________________________________________
                                                            --RISHABH SOOD--

Date Created: 23/07/2019
_______________________________________________________________________________________________________________________________________

different type of variables

int myNum = 5;
float myFloatNum = 5.99f; over here we have to use the character 'f' after init. the variable defined.
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";
double myNum = 19.99d;

_______________________________________________________________________________________________________________________________________

type casting:

Widening Casting (automatically) - converting a smaller type to a larger type size
byte -> short -> char -> int -> long -> float -> double
               example: int myInt = 9;
                        double myDouble = myInt;
-----------------------------------------------------------------------------------
Narrowing Casting (manually) - converting a larger type to a smaller size type
double -> float -> long -> int -> char -> short -> byte
               example: double myDouble = 9.78;
                        int myInt = (int) myDouble;
_______________________________________________________________________________________________________________________________________

Strings:

 str_name.length() returns the length of the string.
 str_name.toUpperCase() and str_name.toLowerCase are useful functions respectively
 str_name.indexOf("sub_str") returns index of sub_string (first occurrence).
 //"\" is used to add characters like " , ' and / to a string.
_______________________________________________________________________________________________________________________________________

Java math library:


-> Math.max(x,y) and Math.min(x,y) return maximum and minimum out of the two arguments given respectively
-> Math.sqrt(x) returns square root of x respectively.
-> Math.random() returns a number between 0-1.
-> Math.acos/asin/atan/sinh/cosh/tanh/sin/cos/tan(x) return function based values as can be interpreted.
-> toDegrees/toRadians(x):
   Converts an angle measured in radians to an approx. equivalent angle measured in degrees nand vice-versa.
-> pow(x,y) returns x^y.
-> Math.log/log10(x) return logarithms of x respectively with the base E/10.
-> hypot(x, y)	Returns sqrt(x2 +y2) without intermediate overflow or underflow.
-> exp(x) returns the value of e^x.

_______________________________________________________________________________________________________________________________________

If-Else statement:


if (condition1) {
   block of code to be executed if condition1 is true
} else if (condition2) {
   block of code to be executed if the condition1 is false and condition2 is true
} else {
   block of code to be executed if the condition1 is false and condition2 is false
}

_______________________________________________________________________________________________________________________________________

ternary operator: 

variable = (condition) ? expressionTrue : expressionFalse;
_______________________________________________________________________________________________________________________________________

switch statement:


switch(expression) {
  case x:
     code block
    break;
  case y:
     code block
    break;
  default:
     code block
}

_______________________________________________________________________________________________________________________________________

The while and the do while loop:


while (condition) {
   code block to be executed
}

and----------------------------

do {
   code block to be executed
}
while (condition);

_______________________________________________________________________________________________________________________________________

The for loop:


for (statement 1; statement 2; statement 3) {
   code block to be executed
}
Statement 1 is executed (one time) before the execution of the code block.

Statement 2 defines the condition for executing the code block.

Statement 3 is executed (every time) after the code block has been executed.

_______________________________________________________________________________________________________________________________________

The exclusive for-each loop:


for (type variable : arrayname) {
   code block to be executed
}


break exits the loop , while continue makes the loop skip the current iteration after it is encountered.
_______________________________________________________________________________________________________________________________________

defining arrays:

String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
int[] myNum = {10, 20, 30, 40};

arr_name.length returns number of elements in the array.
_______________________________________________________________________________________________________________________________________

Multi dimensional arrays:


-> accessing an element:
   int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
   int x = myNumbers[1][2]; (7)

-> Traversing:
   int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    for (int i = 0; i < myNumbers.length; ++i) {
      for(int j = 0; j < myNumbers[i].length; ++j) {
        System.out.println(myNumbers[i][j]);
      }
    }

_______________________________________________________________________________________________________________________________________

Methods or Functions

static return_type MyMethod(args)
{
    code to be executed
}

_______________________________________________________________________________________________________________________________________

Classes in java:

public class MyClass{
         class members
}

-> in order to create a new object (say myObj) of sthe class ,we use the following syntax:
   MyClass myObj = new MyClass();

-> in order to lock the value of a defined variable, use the keyword 'final' before it

-> The dot operator is used to access fields related to the object.

-> while static methods can be accessed openly across the class, public methods can only be referred through
   objects of the class.

_______________________________________________________________________________________________________________________________________

constructors and destructors:


a constructor is defined as follows:
public ClassName(args)
{
   initialization...
}
_______________________________________________________________________________________________________________________________________

class nesting:

class OuterClass {
  int x = 10;

  class InnerClass {
    int y = 5;
  }
}

public class MyMainClass {
  public static void main(String[] args) {
    OuterClass myOuter = new OuterClass();
    OuterClass.InnerClass myInner = myOuter.new InnerClass(); //on creating objects of nested class
    System.out.println(myInner.y + myOuter.x);
  }
}

inner classes can be private,static and protected:
-> a private class cannot be accessed from the outer class.
-> a static class can be accessed without creating an object of the outer class.
-> inner classes can access attributes of the outer class, for example, functions may be defined in it to return the values of variables defined in the 
OuterClass
_______________________________________________________________________________________________________________________________________

Inheritance:

class Base_Class {
    members..
    }

class Child_Class extends Base_Class {
    members..

    public static void main(String[] args) {
        executable code..
    }
 }

_______________________________________________________________________________________________________________________________________

Data abstraction:

-> object cannot be created for an abstract class.
-> an abstract method can only be defined inside an abstract class. It can only be defined in the subclass.
-> a child class of the abstract class must be created in order to access the class and define its abstract functions.
-> defining an abstract class and abstract method:
   abstract class class_name { //abstract class
   public abstract void abstract_func_name(); //abstract method
   other members...
   }

_______________________________________________________________________________________________________________________________________

Java Interface:

-> An interface is basically an abstract class with the following pre-defined specifications:
   -> all methods defined in it are public and abstract.
   -> variables defined are final.
   -> An interface can extend another Java interface only, an abstract class can extend another Java class and implement multiple Java interfaces.
   -> Interfaces are comparatively slower.

-> Defining an interface:
      interface interface_name{
        members..
      }
-> implementing an interface (Inheritance basically)
       class class_name implements interface_name{
            define functions of implemented interface here...
            and other members..
       }

Note: Multiple implementation can be easily done by seperating multiple interface names by commas. Same can be done for inhertitance (extends).
_______________________________________________________________________________________________________________________________________

Enum (to be used for constant values):

-> Enum can have attributes and methods.
-> everything defined in it is public,static and final.
-> defining an Enum:
   enum enum_name{
    //constant names in capital letters(seperated by commas)..
   }
-> accessing enum constants:
   enum_name myVar = enum_name.contant_name; //(copies constant name to myVar)
-> enum can be used in switch statement.
-> looping through an enum:
   for (enum_name myVar : enum_name.values()) {
     System.out.println(myVar);
   }

   here, the values method returns an array of all enum constants.
_______________________________________________________________________________________________________________________________________

User Input:

-> To get any type of input, the Java class Scanner must be imported.
   How to:
   at begining of the file, type the following:
   import java.util.Scanner; (as the scanner class is a part of the util package).
-> Next we must define a Scanner object, which will take our input:
   Scanner myObj = new Scanner(System.in);
-> Finally, taking different data types of input:
      1. Integer/Long
         int/long var = myObj.nextInt()/nextLong();
      2. String
         String str_var = myObj.nextLine();
      3. Boolean
         boolean bool_var = myObj.nextBoolean();
      4. Float
         float float_var = myObj.nextFloat();

_______________________________________________________________________________________________________________________________________

Date and Time:

-> We import the Java date package, in order to work with date and time API.
   How to:
   import java.time.LocalDate/LocalTime/LocalDateTime;
   or
   import java.time.format.DateTimeFormatter;
-> For Date:
   LocalDate myObj = LocalDate.now();
-> For Time:
   LocalTime myObj = LocalTime.now();
-> For Date and Time:
   LocalDateTime myObj = LocalDateTime.now();
-> Format:
    LocalDateTime myDateObj = LocalDateTime.now(); 
    DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss"); 
    String formattedDate = myDateObj.format(myFormatObj); 
    System.out.println("After formatting: " + formattedDate);
-> E can be used to display the day.

_______________________________________________________________________________________________________________________________________

Java ArrayList:

-> resizable array.
-> easy addition and removal of elements.
-> We import the ArrayList class form the Java util package, as follows:
   import java.util.ArrayList;
-> Creating an ArrayList object:
   ArrayList<data-type> arr_name = new ArrayList<data-type>();
-> Various usable functions:
       1. add:
          arr_name.add(element);
       2. remove: 
          arr_name.remove(element_index_no);
       3. access:
          arr_name.get(element_index_no);
       4. change:
          arr_name.set(element_index_no,value);
       5. size:
          arr_name.size();
       6. clear:
          arr_name.clear();
       7. sort:
          -> import collections: import java.util.Collections;
          -> Collections.sort(arr_name);
  -> looping is same.
_______________________________________________________________________________________________________________________________________

Java Hashmap:

-> Hashmap allows the user to set the indexing type of the list as per their choice.
-> In arrays, indexing is set to integers, and cannot be changed.
-> We import the HashMap class from the Java util package,as follows:
   import java.util.HashMap;
-> Creating a HashMap object:
   HashMap<key_type, object_type> HashMap_Name = new HashMap<key_type, object_type>();
-> Various usable functions:
       1. To add element:
          HashMap_Name.put(key_value,object_value);
       2. access:
          HashMap_Name.get(key_value);
       3. remove:
          HashMap_Name.remove(key_value);
       4. clear:
          HashMap_Name.clear();
       5. size:
          HashMap_Name.size();
       6. looping:
          for(key_type/object_type i : HashMap_Name.keySet()/values())
          {
            ....
          }
_______________________________________________________________________________________________________________________________________

Java Wrapper Classes:

-> Provide a way to use primitive data types as objects.
-> Primitive Data Type| Wrapper Class
   ------------------------------------
        byte          |    Byte
        short         |    Short
        int           |    Integer
        long          |    Long
        float         |    Float
        double        |    Double
        boolean       |    Boolean
        char          |    Character

-> Collection objects, such as ArrayList, accept only objects, hence instead of primitive data types, wrapper classes are used there.
-> A wrapper class object maybe simply declared as one declares a variable.
-> The toString() method is used to convert wrapper objects to strings.
_______________________________________________________________________________________________________________________________________

Java Files:

-> We import the File class from the io package in order to work with files. Here is how to import:
   import java.io.File;
-> Next we create an object of the Class file, as follows:
   File myObj = new File("filename.txt");
-> If, the file does not already exist and one wishes to create a new file, we use the createNewFile() method availabe in the class File.
       -> We always include the try...catch block, in order to declare error, if file is not created for any reason.
       -> createNewFile() is a boolean method which returns "true" when the file is succesfully created.
       -> for the exception, we include another class from package io: import java.io.IOException;
       -> Here is an example:

            try { 
             File myObj = new File("filename.txt"); 
             if (myObj.createNewFile()) { 
                System.out.println("File created: " + myObj.getName()); 
             } else { 
                System.out.println("File already exists."); 
             } 
            } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace(); 
            } 
-> 
      --------------------------------------------------------------------------------
     |     Method      |   Type     |        Description                               |
      --------------------------------------------------------------------------------
     |canRead()        |  Boolean   |  Tests whether the file is readable or not       |
     |canWrite()       |  Boolean   |  Tests whether the file is writable or not       |
     |createNewFile()  |  Boolean   |  Creates an empty file                           |
     |delete()         |  Boolean   |  Deletes a file                                  |
     |exists()         |  Boolean   |  Tests whether the file exists                   |
     |getName()        |  String    |  Returns the name of the file                    |
     |getAbsolutePath()|  String    |  Returns the absolute pathname of the file       |
     |length()         |   Long     |  Returns the size of the file in bytes           |
     |list()           |  String[]  |  Returns an array of the files in the directory  |
     |mkdir()          |  Boolean   |  Creates a directory                             |
      --------------------------------------------------------------------------------

-> Writing to a file:
         -> We now further import the FileWriter class: import java.io.FileWriter;   
         -> Here is an example:

            try { 
             FileWriter myWriter = new FileWriter("filename.txt"); 
             myWriter.write("text to be written comes here...");
             myWriter.close();
             System.out.println("Successfully wrote to the file."); 
            } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace(); 
            }
            
-> Reading from a file:
        -> import java.io.FileNotFoundException;  // Import this class to handle errors
        -> import java.util.Scanner; // Import the Scanner class to read text files
        -> create a file object myObj.
        -> Set up a scanner object, myReader: 
           Scanner myReader = new Scanner(myObj);
        -> Create a while loop which gets and prints statements, until end of the file is reached:
           while (myReader.hasNextLine()) {
             String data = myReader.nextLine();
             System.out.println(data);
           }
        -> close the Scanner object.
        -> for the exception:
           catch (FileNotFoundException e) {
              System.out.println("An error occurred.");
              e.printStackTrace();
           }
_______________________________________________________________________________________________________________________________________ 
