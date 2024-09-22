from patient import Patient


patients = {}

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patient[patient.id]=patient
   
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
          del patient[id]
            
        #end if 
    #end for 
    print(f'No such id {id}')
#5. patient_display()
def patient_display():
    global patients
    for patient in patients:
        print(patient)



def patient_id(id):
     for patient in patients:   
        if patient.id==id:
            print(patient)



def patient_update(id):
    for patient in patients:
        if patient.id==id:
            name=input('Enter the name : ')
            patient.name=name
