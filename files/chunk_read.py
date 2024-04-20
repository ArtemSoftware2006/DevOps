def process_data(data):
    print('data')

with open('data/img.ico', 'rb') as file:
    while True:
        chunk = file.read(1024)
        if chunk:
            process_data(chunk)
        else:
            break

