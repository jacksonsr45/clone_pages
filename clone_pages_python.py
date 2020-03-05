import requests
import sys



def create_copy_page(create_copy, name_page):
    with open(f'{name_page}.html', 'w', encoding='utf-8') as file_html:
        file_html.write(create_copy.decode('utf-8'))



def main():
    url = sys.argv[1]
    name_page = sys.argv[2]
    
    if sys.argv[1] == "-h":
        print('Helo to de simple system for clone pages. \n')
        print('Enter with python clone_pages_python.py "https:local_web_to_the_page" "name_from_clone"')
        print('\n or python3 clone_pages_python.py "https:local_web_to_the_page" "name_from_clone"')
    else:
        print('Helo to de simple system for clone pages. \n')
        print(f'Creating file {name_page}.html in this folder path. \n')
        req = requests.get(url)
        create_copy_page( req.content, name_page)
        print(f'Created::::{name_page}.html \n')



if __name__ == "__main__":
    main()