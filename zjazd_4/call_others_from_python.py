import os

x = os.system("dir")
y = os.system("ipconfig")

print(x)
print(y)

#x = os.popen("ipconfig").read()


import subprocess
p = subprocess.Popen("notepad.exe") # wywoływanie programu np jak w tym przypadku notepad

print('lalalala')

