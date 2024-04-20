import pathlib

file_path = 'data/data.txt'
file = open(file_path)
text = file.read()
print(text)
print(file)
file.close()

file = open(file_path)
text = file.readlines()
print(text)
print(text[1])
file.close()

with open(file_path) as file:
    text = file.read()
    print(text)

img_path = 'data/img.ico'
with open(img_path, 'rb') as file:
    btext = file.read()
    print(btext[:100])

file_path='c:/Users/Artem/Desktop/Programs/DevOps/files/data/data2.txt'
text = '''Artem Egorov
Sinior Developer'''
with open(file_path, 'w') as file:
    file.write(text)


