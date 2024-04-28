import requests
import os
import argparse

def load_page(path_urls, path_pages_dir):
    with open(path_urls, 'r') as file_urls:
        urls = file_urls.read()
        urls = urls.split()
        print(urls)
    
    if not os.path.exists(path_pages_dir):
        os.mkdir(path_pages_dir)

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            document_name = url.split('/')[-1]
            path_page = path_pages_dir + '/' + document_name

            if os.path.exists(path_page):
                print ('Page already exists:', url)
                continue

            with open(path_page, 'w', encoding='utf-8') as file_page:
                file_page.write(response.text)
            print('Page saved:', url)
        else:
            print('Page not saved:', url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', '-u',
                        help='Path to file with urls',
                        action='append')
    parser.add_argument('--pages', '-p',
                        help='Path to directory for pages',
                        action='append')
    args = parser.parse_args()

    
    path_urls = './urls'
    path_pages = './pages'

    if args.urls:
        path_urls = args.urls[0]
    if args.pages:
        path_pages = args.pages[0]

    load_page(path_urls, path_pages)
