# RadwanLang
    Simple and easy programming language which i made for educational purposes & for fun.


## Requirements :
- Python 3.10 or above
- Windows OS only
- Save code with extension '.radwan' 


## Installation

```
git clone https://github.com/RadwanHegazy/RadwanLang
```


## Write your first code in RadwanLang 🔥


### For Comments we use `#`
```
# This is a comment line

# this is the secend comment
```

### Define the variables `<var_type>: <var_key> = <var_value>`

Avaliable Data Types : 
- `s:` -> for string
- `i:` -> for integers
- `f:` -> for floats
- `b:` -> for booleans 


```
# define variable 
s: name = ""
i: age = 0
f: salary = 0
b: is_student = 0
```


### Built-in Methods `@<method_name>`

These is all built-in methods in the language :
- `@userInput: <variable_name>, <output_text> ` -> take input from user and save it on a variable you choose
- `@cleanScreen` -> clean the screen
- `@calc: <variable_name>, <operation>` -> for calculation 
- `@write: <*args>` -> for write data on screen


### Usage of built-in methods
```
# Define Variables
s: name = ""
i: age = 0
f: salary = 0
b: is_student = 0

# Ask user for data
@userInput: name, "Enter your name "
@userInput: age, "Enter your Age > "
@userInput: salary, "Enter Your salary > "
@userInput: is_student, "Student ? [1/0] > "


# clean the screen
@cleanScreen

# write the output on screen
@write: "Your name is " , name
@write: "Your Age is  ", age
@write: "Your salary is ", salary
@write: "is Student ", is_student

# do an calculation operation with built-in method calc
f: result = 0

@calc : result , 123 + 103 + (123 - 11) / 12

@write: "The result of operation is : " , result

```

### If conditions `@if: <var_1> <operaion> <var_2> -> <screen_output>`

Avaliable operations:
- `==` -> check if the var_1 equals var_2
- `!=` -> check if var_1 not equals var_2

### Usage of condition statement
```
# Define vars
s: name = ""
i: age = 0

# ask user for input
@userInput: name, "Please Enter Your Name >> "
@userInput: age, "Enter Your Age >> "

# check for name
@if: name != "radwan" -> "No, Name Not Equals 'radwan'"
@if: name == "radwan" -> "Yes Name Equals Radwan"

# check for age
@if: age == 19 -> "Yes the age is 19."
@if : age != 19 -> "No The age not equals 19"
```

### For run the code

```
py core/interpreter.py <file_path.radwan>
```
