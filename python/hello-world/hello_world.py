#
# Exercism.io
# Python track
# Problem #1 - Hello World
# github.com/marnovo/Exercism
#

name = input("Tell your name: ")

def hello(name=''):
    if name == '':
        message = "Hello, World!"
    else:
        message = "Hello, " + name + "!"
    return message

print(hello(name))