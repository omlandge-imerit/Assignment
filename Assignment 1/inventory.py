import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def calculate_total_price(items):
    total_price = 0
    for item in items:
        total_price += item['price']
    return total_price

def main():
    data = read_json_file('inventory.json')
    total_price = calculate_total_price(data['items'])
    print("Total inventory price:", total_price)

if __name__ == "__main__":
    main()
