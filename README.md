# RadwanLang
    Simple and easy programming language which i made for educational purposes & for fun.


### Requirements :
- Python 3.10 or above
- Windows OS only
- Save code with extension '.radwan' 


### Installation

```
git clone https://github.com/RadwanHegazy/RadwanLang
```

```
cd RadwanLang\core
```

### Try the Code bellow
```
# This is a comment line

# define variable 
s: name = ""

# take input and save it to the variable
@userInput: name, "Enter your name "

i: age = 0
@userInput: age, "Enter your Age > "

f: salary = 0
@userInput: salary, "Enter Your salary > "

b: is_student = 0
@userInput: is_student, "Student ? [1/0] > "


# clean the screen
@cleanScreen

# write the output on screen
@write: "Your name is " , name
@write: "Your Age is  ", age
@write: "Your salary is ", salary
@write: "is Student ", is_student
```

### Run `code.radwan`

```
py interpreter.py ..\code.radwan
```
