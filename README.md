# clone_pages
This is a simple program for studying requests, it should not be used for anything other than understanding how it works. Thanks

---

In terminal enter with code.

```
python clone_pages_python.py "https:local_web_to_the_page" "name_from_clone"
```

for help

```
python clone_pages_python.py -h
```

In the main we receive the arguments passed by the user.
```py
    url = sys.argv[1]
    name_page = sys.argv[2]
```

This function receives the contents of the page, and using the decode ('utf-8'), it creates a file with the last name and writes the content inside.
```py
def create_copy_page(create_copy, name_page):
    with open(f'{name_page}.html', 'w', encoding='utf-8') as file_html:
        file_html.write(create_copy.decode('utf-8'))
```
