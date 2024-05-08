import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def display_books(books):
    for book in books:
        print("Title:", book['title'])
        print("Author:", book['author'])
        print("Price:", book['price'])
        print()

def main():
    data = read_json_file('books.json')
    display_books(data['books'])

if __name__ == "__main__":
    main()
