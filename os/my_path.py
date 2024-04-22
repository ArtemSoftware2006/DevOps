import os
cur_dir = os.getcwd()

print(cur_dir)
# Отделяет путь от имени каталога
print(os.path.split(cur_dir))
# Путь до каталога
print(os.path.dirname(cur_dir))
# Название каталога
print(os.path.basename(cur_dir))

while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)
