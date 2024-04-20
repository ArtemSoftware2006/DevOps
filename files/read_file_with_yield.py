def line_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

reader = line_reader('data/data.txt')

with open('data/dist.txt', 'w') as dist_file:
    for line in reader:
        dist_file.write(line)