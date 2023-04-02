from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'devanshmehta06@gmail.com'
email_password = 'uvjhuwisllrdjegh'

email_reciever = 'devanshmehta06@gmail.com'

subject = 'Recommendations'

body = '''
    Body
'''

em = EmailMessage()
em['From']=email_sender
em['To']=email_reciever
em['subject']=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,'uvjhuwisllrdjegh')
    smtp.sendmail(email_sender,email_reciever,em.as_string())
