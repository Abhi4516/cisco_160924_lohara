from patient_service import patient_add,patient_display,patient_id,patient_remove,patient_update


def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
7-end                       
your choice:'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()

    elif choice == 4:
         id =int(input('Enter the id : '))
         patient_id(id)

    elif choice ==5:
        id =int(input("Enter the id : "))
        patient_update(id)
    elif choice == 7:
        pass 
    else:
        print('Invalid menu')
    return choice
#7. menus 
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')


