'''
How to check file is empty or not
'''
import os
print(os.stat("test.txt").st_size==0)