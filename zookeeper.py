import os
import json
import sys
import pandas as pd


# with open('sample.json', 'r') as openfile:
 
#     # Reading from json file
#     json_object = json.load(openfile)
# os.system('python broker1.py')
if os.path.isfile('bk1.txt'):
    os.system('python broker1.py')
elif os.path.isfile('bk2.txt'):
    os.system('python broker2.py')
elif os.path.isfile('bk3.txt'):
    os.system('python broker3.py')
else:
    print("System failure !!")
    sys.exit()