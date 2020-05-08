# sending mail
import smtplib 
import ssl

# receiving mail
import imaplib 

# parsing mail
import email


import datetime


# tls
def send_mail(sender_mail, sender_password, receiver_mail, mail_subject, mail_body, smtp_server_incoming="smtp.gmail.com"):

    message = "Subject: {0}\n\n{1}".format(mail_subject, mail_body).encode("utf-8")

    connection = smtplib.SMTP(smtp_server_incoming, 587)
    connection.ehlo()
    connection.starttls()
    connection.ehlo()

    connection.login(sender_mail, sender_password)
    connection.sendmail(sender_mail, receiver_mail, message)

    print("The mail has been sent")
    # print("The mail has been sent. Time:{}".format(str(datetime.datetime.now().time())[0:8])) # uses datetime

    connection.close()


# ssl
def send_mail2(sender_mail, sender_password, receiver_mail, mail_subject, mail_body, smtp_server_incoming="smtp.gmail.com"):

    message = "Subject: {0}\n\n{1}".format(mail_subject, mail_body).encode("utf-8")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server_incoming, 465, context=context) as server:
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail, receiver_mail, message)

    print("The mail has been sent")
    # print("The mail has been sent. Time:{}".format(str(datetime.datetime.now().time())[0:8])) # uses datetime



# get last mail if it is not amultipart  mail
def get_last_mail(sender_mail, sender_password, delete=False, server_outgoing="imap.gmail.com"):
    
    connection = imaplib.IMAP4_SSL(server_outgoing)
    connection.login(sender_mail, sender_password)
    connection.list()
    connection.select("inbox")                                           
    result, all_of_inbox = connection.search(None, "ALL")


    # data is a list.
    ids = all_of_inbox[0]
    # ids is a space separated string
    id_list = ids.split() 

    # get the latest
    latest_email_id = id_list[-1]
    # fetch the email body
    result, latest_email = connection.fetch(latest_email_id, "(RFC822)") 

    # parse mail from bytes
    message = email.message_from_bytes(latest_email[0][1])

    if(delete):
        connection.store(id_list[-1], '+FLAGS', '\\Deleted')
        connection.expunge()
        print("Last mail deleted")

    connection.close()
    connection.logout()

    subject = message["Subject"]
    sender = message["from"]
    mail_body_text = message.get_payload()

    return  sender, subject, mail_body_text




sender_mail = ""
sender_password = ""
receiver_mail = ""


