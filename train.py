
import json


def add_contact(data):
    name = input('Name: ').strip()
    phone = input('Phone number: ').strip()

    data.append({
        "name": name,
        "phone": phone
    })

    print('Contact added successfully!')


def delete_contact(data):
    choice = input('Delete by name or phone? (name/phone): ').strip().lower()

    if choice == 'name':
        search = input('Enter contact name: ').strip()

        for person in data:
            if person["name"].lower() == search.lower():
                data.remove(person)
                print('Contact deleted successfully!')
                return

    elif choice == 'phone':
        search = input('Enter contact phone number: ').strip()

        for person in data:
            if person["phone"] == search:
                data.remove(person)
                print('Contact deleted successfully!')
                return

    else:
        print('Invalid choice!')
        return

    print('Contact not found!')


def search_contact(data):
    choice = input('Search by name or phone? (name/phone): ').strip().lower()

    if choice == 'name':
        search = input('Enter contact name: ').strip()

        for person in data:
            if person["name"].lower() == search.lower():
                print(person)
                return

    elif choice == 'phone':
        search = input('Enter contact phone number: ').strip()

        for person in data:
            if person["phone"] == search:
                print(person)
                return

    else:
        print('Invalid choice!')
        return

    print('Contact not found!')


def main():

    with open("data.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    while True:

        print('\n----- PHONE BOOK -----')
        print('1 = Add')
        print('0 = Delete')
        print('2 = Search')
        print('4 = Exit')

        number = input('Choose an option: ')

        if number == '1':
            add_contact(data)

        elif number == '0':
            delete_contact(data)

        elif number == '2':
            search_contact(data)

        elif number == '4':
            print('Goodbye!')
            break

        else:
            print('Invalid option!')

        with open('data.json', 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


main()
