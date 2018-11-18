# 1) rzczy z biblioteki standardowej
#import sys
#import os
#import csv

# 2) rzeczy z biblioteki zewnetrzneych

# 3) moduly z naszej aplikacji

#import B
from B import bar

print('jestem w module a')

def foo():
    return 'Foo z modulu A'
print(foo)