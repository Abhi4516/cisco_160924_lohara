"""http://api.openweathermap.org/data/2.5/weather?q=Pune&


https://openweathermap.org/find?utf8=✓&q=pune&appid
https://openweathermap.org/find?utf8=✓&q=pune&appid34e3e6f45fdc7ddc79ef9ed7ea49edd2&units=metric


aba68a5a9d12d75dadbe0159d8e2d768


https://api.openweathermap.org/data/2.5/weather?q=Pune&appid=34e3e6f45fdc7ddc79ef9ed7ea49edd2&units=metric

34e3e6f45fdc7ddc79ef9ed7ea49edd2
"""


import json
import requests

class NotesApp:
    def ___init__(self):
         url='http://localhost:5000'

         return url.json()
        

    def read_all(self):
         res=requests.get(f'{url}')
         return res.json()
    def read_by_id(self):
        res=requests.get(f'http://localhost:5000/notes/notes/{id}')
        return res.json()
    
    def create(self,note_json_str):
        headers={'content-type':'application/json'}
        res=requests.posts('http://localhost:5000/notes/notes',data=note_json_str,headers=headers)
        return res.json()
    
    def update(self,id,note_json_str):
        headers={'content-type':'application/json'}
        res=requests.put(f'{self.url}'/notes/{id},data=note_json_str,headers=headers)
        return res.json()

app =NotesApp()
choice=int(input('1=all,2-read_by_id,3-create,4-update,5-delete,6-search\nchoice: '))
if  choice==1:
    notes=app.read_all()
    print(notes)

elif choice == 2:
    id =int(input('id: '))
    notes=app.read_by_id(id)
    print(notes)            

elif choice==3:
    title=input('title: ') 
    notes=input('notest: ')
    note_dict={'title':title,'notes':notes}
    note_json_str=json.dumps(note_dict)
    note=app.create(note_json_str) 
    print(note)  

elif choice==4:
    id=int(input('id: '))
    title=input('title: ') 
    notes=input('notest: ')
    note_dict={'title':title,'notes':notes}
    note_json_str=json.dumps(note_dict)
    note=app.create(note_json_str) 
    print(note)  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "gmaheswaranmca@gmail.com"
receiver_email = "gmaheswaranmca@yahoo.com"
subject = "Test Email from Python"
body = "This is a test email sent from Python!"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body
msg.attach(MIMEText(body, 'plain'))

# SMTP server details
smtp_server = "smtp.gmail.com"
port = 587  # For TLS (or use 465 for SSL)
password = ""#"your_email_password"

# Create a secure connection with the SMTP server
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection with TLS
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection