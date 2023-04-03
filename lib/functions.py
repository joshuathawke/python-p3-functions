#!/usr/bin/env python3
# greetProgrammer function
def greet_programmer():
    print("Hello, programmer!")
    
# greet function
def greet(name):
    print(f"Hello, {name}!")
    
# greetWithDefault function
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
# add function
def add(num1, num2):
    return num1 + num2
    
# halve function
def halve(number):
    if type(number) != int and type(number) != float:
        return None
    return number / 2