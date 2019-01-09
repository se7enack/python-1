#!/bin/env python3

# @dangerousness Jan082019

import webbrowser, os

file="/etc/hosts"

try:
    if os.path.exists(file):
        if os.path.isfile(file):
            print(open(file).read())
        else:
            print(file + " exists, however it is not a file (looks more like a folder to me).")
            print("Correct the path to point to an actual file.")
    elif not os.path.exists(file):
        print(file + " is missing.")
except UnicodeDecodeError:
    webbrowser.open('file://' + os.path.realpath(file))
except NameError:
    print("Error: looks like a var not defined")
