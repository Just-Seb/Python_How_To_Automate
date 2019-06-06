import smtplib, getpass

default = 'justseb3@gmail.com'
dad = 'marius.scurtescu@gmail.com'
mom = 'zsoka.scurtescu@gmail.com'
Connor = 'con9123@sd64.bc.ca'
Jonah = 'jon9154@sd64.bc.ca'
seb = 'sebastain.scurtescu@gmail.com'

names = ['default','dad','mom','Connor','Jonah','seb']
emails = ['justseb3@gmail.coom','marius.scurtescu@gmail.com','zsoka.scurtescu@gmail.com','con9123@sd64.bc.ca','jon9154@sd64.bc.ca','sebastain.scurtescu@gmail.com']
list_length = len(names)

def send_email(recipient):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    print('which email do you want to send from?')
    sender = str(input())
    if sender == names[0]:
        sender = emails[0]

    for i in range(0, list_length):
        if recipient == names[i]:
            recipient = emails[i]
            break

    while True:
        print('Enter your password:')
        password = getpass.getpass()
        password = str(password)

        try:
            smtpObj.login(sender, password)
            password = None
            break
        except smtplib.SMTPAuthenticationError:
            print('Try again bad password:/')
    print('Subject: ')
    subject = 'Subject: ' + str(input())
    print('Main Body: ')
    main_body = str(input())
    print('Ending: ')
    ending = str(input())
    smtpObj.sendmail('justseb3@gmail.com', recipient, subject + '\n' + main_body + '\n' + ending)
    smtpObj.quit()


print('Do you want to send an email? Y/n')
answer = str(input())

if answer == ' ' or answer == 'y' or answer == 'Y':
    print('Who do you want to send the email to?')
    person = str(input())
    send_email(person)

elif answer == 'n' or answer == 'N':
    print("Ok have a nice day :)")
