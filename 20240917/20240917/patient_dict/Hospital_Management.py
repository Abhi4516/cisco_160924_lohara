class Patient:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
#2. patients[]
patients = {}

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[id]=name
#4. patient_remove(id)
def patient_remove(id):
    if id in patients:
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                del patients[id]
                print('Patient deleted successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
#5. patient_display()
def patient_display():
    global patients
    for id in patients:
        print(patients[id])



def patient_id(id):
    
        patient=patients.get(id)
        if patient ==None:
            print('none')
        print(patient)    



def patient_update(id):
    for id_new,name_new in patients.items():
        if id_new==id:
            name=input('Enter the name : ')
            patients[id_new]=name
            print(patients)



    #global patients
    #patient=patients.get(id)
    #name=input('Enter the name : ')
    #patient.name=name
#6. menu 
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
#8. driver program
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')
#8. driver program
menus()




d