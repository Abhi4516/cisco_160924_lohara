
patient_database={}

def patient_id_name(patient_id,patient_name):

   if patient_id in patient_database:
       print('Ptaient id is already exist')
   else:
      patient_database[patient_id]=patient_name 
      print(f'Patient name is {patient_name} with id {patient_id}')      
    


def delete_patient_id(patient_id):
    if delete_patient_id in patient_database:
       del patient_database[patient_id]
    else:
       print('Patient id is not present')   


def patients_records():
    if patient_database: 
     for patient_id,patient_name in patient_database.items():
        print(f"id {patient_id} : name {patient_name}")            
    


while True:
    print("1: Add a patient")
    print("2: Delete a patient")
    print("3: all patients data")
    print("4: Exit")
   
    choice = input("Choose an option (1/2/3/4): ")

    if choice == '1':
        patient_id = input("Enter patient ID: ")
        patient_name = input("Enter patient name: ")
        patient_id_name(patient_id, patient_name)

    elif choice == '2':
        patient_id = input("Enter patient ID to delete: ")
        delete_patient_id(patient_id)

    elif choice == '3':
        patients_records()

    elif choice == '4':
        print("Exiting the program.")
        break