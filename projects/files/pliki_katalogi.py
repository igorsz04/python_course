import os
import time
print('getcwd')
print (os.getcwd())

print('listdir')
print(os.listdir('.'))

print(time.ctime(os.path.getmtime('zwierzeta.txt')))
