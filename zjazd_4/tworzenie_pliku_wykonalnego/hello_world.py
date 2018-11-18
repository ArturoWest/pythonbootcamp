import sys
import time

if len(sys.argv) >1:
    print("Hello", sys.argv[1])
else:
    print('Hello world')

# pip install pyinstaller
# pyinstaller --onefile hello_world.py
