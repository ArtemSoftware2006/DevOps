import os
import time
import platform
from pprint import pprint

print(os.listdir('../'))
os.mkdir('new_folder')
time.sleep(1)
os.rename('./new_folder', 'new_folder2')
time.sleep(1)
os.rmdir('new_folder2')

path_dires = './dir1/dir2'
os.makedirs(path_dires)
os.chdir('./dir1')
os.chdir('..')
time.sleep(3)
os.removedirs(path_dires)

# create file in python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')

os.chmod('file.txt', 0o755)
pprint(os.stat('file.txt'))

print(platform.system())