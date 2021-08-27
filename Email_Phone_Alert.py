#alert.py

""" 
This function creates email or phone alerts using an email account. Current configuration is for gmail. 

Notes:
    'subject' = message body
    'to' = recipient
    'from' = user's email address
    'server' must be configured for the email server being used
    Must set up 2-factor authentication to get an app password and you must have an app password to use third-party apps.
    If phone alerts will be sent, the 10 digit phone number must have the @ext specific to the carrier.
"""

import smtplib
from email.message from EmailMessage

def email_alert(subject,body,recipient):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subjec'] = subject
	msg['to'] = to
	
	
	user = "email address"
	msg['from'] = user
	password = "password" #use app password
	
	server = smtplib.SMTP("smtp.gmail.com", 587) #customize according to email server
	server.starttls()
	server.login(user,password)
	server.send_message(msg)
	
	server.quit()
	
if __main__ == '__main__':
	email_alert("Hey", "Hello World", recipient) #add cell service carrier's @#### to the ten-digit phone number to send a text message instead