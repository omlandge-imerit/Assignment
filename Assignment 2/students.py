import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def display_students(students):
    for student in students:
        print("Name:", student['name'])
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        print()

def main():
    data = read_json_file('students.json')
    display_students(data['students'])

if __name__ == "__main__":
    main()
