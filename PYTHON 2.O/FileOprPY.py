import os
import sys
import pathlib
from pathlib import Path
print("1",Path.cwd())
print("2",os.getcwd())
print("3",pathlib.Path().absolute())
print('File name :    ', os.path.basename(__file__))
print('Directory Name:', os.path.dirname(__file__))
print('Absolute path of file:  ', os.path.abspath(__file__))
print('Absolute directoryname: ', os.path.dirname(os.path.abspath(__file__)))

import os
pythonfile = 'pathfinding.py'

# if the file is present in current directory,
# then no need to specify the whole location
print("Path of the file..", os.path.abspath(pythonfile))

for root, dirs, files in os.walk(r'E:\geeksforgeeks\path_of_given_file'):
    for name in files:
      
          # As we need to get the provided python file, 
        # comparing here like this
        if name == pythonfile:  
            print(os.path.abspath(os.path.join(root, name)))
# print("First :- 1.py"+f"File is:{os.path.basename}")
