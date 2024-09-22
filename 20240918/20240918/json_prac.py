import json
patients=[{'id':1,'name':'Abhi'},
          {'id':2,'name':'Rohit'},

           {'id':3,'name':'Akshar'},
           {'id':4,'name':'jasprit'}]

new_file=json.dumps(patients)
print(new_file)


with open('patient_data.json','w') as json_db:
    json.dump(patients,json_db)

    