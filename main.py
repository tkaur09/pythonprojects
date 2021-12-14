import smtplib as tk
import random
a=tk.SMTP("smtp.gmail.com",587)
a.starttls()
a.login("studykaur1@gmail.com","Studykaur@12")
sub="Hello"
body="User"
message="subject:{}\n\n{}".format(sub,body)
print(message)
list=["studykaur1@gmail.com"]
a.sendmail("studykaur1@gmail.com",list,message)
print("Email sent")
a.quit()