import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'abhijeetbade2000@gmail.com'
email_passwd = 'lqmb ntwu xjbj izkk'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg=" Abhijeet Bade ")
connection.close()
print('Mail sent successfully')






