import os
import random
import smtplib

def automatic_email():
    user=input("Enter Your Name : ")
    email= input("Enter Your Email : ")
    test=input("Write a message")
    message= (f"Dear {user} ,\n ,{test} \n Welcome to MM Group")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("makgun095@gmail.com", "------")
    s.sendmail('&&&&&&&&&&&', email,message)
    print("Email Sent")

automatic_email()