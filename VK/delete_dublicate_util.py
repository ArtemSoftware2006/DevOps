import argparse


def detele_duplicate(source_path, output_path):
    print('Start delete duplicate...')
    lines_seen = set() # создаем пустой набор для хранения уникальных строк

    with open(source_path, 'r') as infile:
        with open(output_path, 'w') as outfile:
            for line in infile:
                if line not in lines_seen: # проверяем, есть ли текущая строка в наборе
                    lines_seen.add(line) # добавляем строку в набор
                    outfile.write(line) 

    print("Finish delete duplicate!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-u',
                        help='Path to source file',
                        action='append')
    parser.add_argument('--output', '-p',
                        help='Path to output file',
                        action='append')
    args = parser.parse_args()

    csv_source_path = '.'
    csv_output_path = '.\\output.csv'

    if not args.source:
        print('No source file')
        return
    if args.source:
        csv_source_path = args.source[0]
    if args.output:
        csv_output_path = args.output[0]

    detele_duplicate(csv_source_path, csv_output_path)

if __name__ == '__main__':
    main()