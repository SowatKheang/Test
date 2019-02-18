## Home Work: create contact program with some functions (add, search, edit and delete)
## Student's name: Kheang Sowat

my_contacts = [ ]

while True:
    print('\t\n -- -- -- -- -- -- Contact Menu -- -- -- -- -- -- --')
    print('|                                                   |')
    print('| 1. Add new contact________________________________|')
    print('| 2. Search, Edit or Delete_________________________|')
    print('| 3. Quit___________________________________________|')
    print('|                                                   |')
    print('-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n')
    print('-- -- -- -- -- -- This is my phone list -- -- -- -- |')
    print(f'\n{my_contacts} \n')

    choice = input('Please select your choice: ')
    
    if choice == '1':
        name = input('\tName: ').title()
        while True:
            phone = input('\tTelephone: ')

            if phone.isdigit():
                phoneNumber = phone
                break
            else:
                print("\tTry again! That was not number")
                continue

        my_contacts.append(
            {
                'name':f'{name}',
                'telephone':f'{phoneNumber}'
            }
        )
        print('\tA new contact has been added!!!\n')    
    
    elif choice == '2':
        while True:
            search = input('Enter a Name or a Phone Numer to search: ')
            for contact in my_contacts:
                if  contact['name'].title() == search.title() or contact['telephone'] == search:
                    print(contact['name'] +"  "+ contact['telephone'])
                    continue

            print('\nPress E to Edit or Press D to Delete or Q to Quit this option ')
            option = input('Please enter the option: ')

            if option == 'E':
                new_name = input("\tNew name: ").title()
                new_phone_number = input("\tNew telephone:")
                for contact in my_contacts:
                    if contact['name'].title() == search.title() or contact['telephone'] == search:
                        contact['name']= new_name
                        contact['telephone'] = new_phone_number
                        break
                break

            if option == 'D':
                for contact in my_contacts:
                    if contact['name'] == search.title() or contact['telephone'] == search:
                        my_contacts.remove(contact)
                        break
                break
            
            if option == 'Q':
                break
     
    elif choice == '3':
        break

