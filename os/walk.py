import os
import fire
def walk(path):
    print(f'Check {path}')
    children = os.listdir(path)
    for child in children:
        child_path = os.path.join(path, child)
        if os.path.isfile(child_path):
            print(f'''
    Filepath: {child_path}
    Name: {child}
    Size: {os.path.getsize(child_path)}
    Last access: {os.path.getatime(child_path)}
''')
        elif os.path.isdir(child_path):
            walk(child_path)

if __name__ == '__main__':
  fire.Fire()