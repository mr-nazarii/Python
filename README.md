# Python

Python Tutorials

``sh

<!-- If else -->

if (x == 4):

    print("Hello there")

else:
print("Generall Kenobi")

<!-- Operators -->

xx = 20
kk = xx % 7

res = 7 \*\* 2

print(type(res))
print(float(kk))
print(type(float(kk)))

<!--

class 'int'>
6.0
<class 'float'>

 -->

string = "123"
print(type(string))
print(type(int(string)))

print(string)

<!--

<class 'str'>
<class 'int'>
123

 -->

flag = True

rawnum = input("Enter a number to multiply on 2\n")
while flag == True:
rawnum = input("Try again\n")

    try:
        rawnum = int(rawnum)
    except:
        print("Invalid input")
        continue

    print("2 * ",rawnum,"=",2 * rawnum)
    flag = False

<!-- def functions -->

def thing(name):
print("Hello world!",name,"Happy to see you!")

def greet(name):
return "Hello "+ name

print(greet('Nazarii'))

``

## pyTutorial9 File handle
