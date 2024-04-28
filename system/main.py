import sys
import os
import subprocess
import say_hello

print(sys.byteorder)
print(sys.getsizeof(sys))
print(sys.platform)
print(sys.version_info)
print(sys.version)

if sys.version_info.major < 3:
    print("You need update Python version to 3.7 or higher")
elif sys.version_info.minor < 7:
    print("You need update Python version to 3.7 or higher")
else:
    print("You have Python version 3.7 or higher")


print(os.getlogin())
print(os.environ.get('LOGLEVEL'))
os.chdir('../os')
print(os.getcwd())



cp = subprocess.run(['C:\\Windows\\System32\\cmd.exe', '/c', 'dir'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True)

print(cp.stdout)

cp = subprocess.run(['C:\\Windows\\System32\\cmd.exe', '/c', 'dir'], 
                    stderr=subprocess.PIPE, 
                    universal_newlines=True)

print(cp.stderr)

cp = subprocess.run(['C:\\Windows\\System32\\cmd.exe', '/c', 'dir', '/tmp'], 
                    stdout=subprocess.PIPE, 
                    universal_newlines=True,
                    )

print(cp.stdout)
