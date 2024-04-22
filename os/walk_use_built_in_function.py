import fire 
import os

def walk(path): 
    for parent_path, directories, files in os.walk(path):
        print(f'Check {parent_path}')
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            print(f'\n\tPath: {file_path}')
            print(f'\tFilename: {file_name}')
            print(f'\tSize: {os.path.getsize(file_path)}')
            print(f'\tLast access: {os.path.getatime(file_path)}')

if __name__ == '__main__':
  fire.Fire()