import sys

def hello_world():
    if len(sys.argv) > 1:
        print("Hello", sys.argv[1])

    else:
        print("Hello World")

hello_world()
