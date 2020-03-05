import requests
import sys



def create_copy_page(create_copy, name_page):
    with open(f'{name_page}.html', 'w', encoding='utf-8') as file_html:
        file_html.write(create_copy.decode('utf-8'))



def main():
    url = sys.argv[1]
    name_page = sys.argv[2]

    req = requests.get(url)
    create_copy_page( req.content, name_page)



if __name__ == "__main__":
    main()