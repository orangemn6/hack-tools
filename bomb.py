## J's Text Bomber ##
import time
import smtplib

#CONFIG. You can change any of the values on the right.
email_provider = 'smtp.gmail.com' #server for your email- see ReadMe on github
email_address = "@gmail.com" #your email
email_port = 587 #port for email server- see ReadMe on github
password = "" #your email password
msg = "message" #your txt message
text_amount = 200 #amount sent
target_email = "target" #target number. must be in email form- see ReadMe on github
wait = 0.01 #seconds in between messages
#END CONFIG

### DO NOT EDIT BELOW THIS LINE ###
server = smtplib.SMTP(email_provider, email_port)
server.starttls()
server.login(email_address, password)
for _ in range(0,text_amount):
    server.sendmail(email_address,target_email,msg)
    print("sent")
    time.sleep(wait)
print("{} texts were sent. Hope you had a good time ;)".format(text_amount))
server.quit()
