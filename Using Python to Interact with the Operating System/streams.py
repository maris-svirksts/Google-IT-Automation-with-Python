#! python

#data = input("This will come from STDIN: ")
#print("Now we write it to STDOUT: " + data)

import os

print("PATH: " + os.environ.get("PATH", ""))
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

import sys
print(sys.argv)

# ./streams.py one two three
# ['./streams.py', 'one', 'two', 'three']