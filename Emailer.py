import smtplib, getpass

default = 'justseb3@gmail.com'
dad = 'marius.scurtescu@gmail.com'
mom = 'zsoka.scurtescu@gmail.com'
Connor = 'con9123@sd64.bc.ca'
Jonah = 'jon9154@sd64.bc.ca'
seb = 'sebastain.scurtescu@gmail.com'

names = [default,dad,mom,Connor,Jonah,seb]


def send_email(recipient):
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    print('which email do you want to send from?')
    sender = str(inpt())
    
    for i in range(0,len(names)):
        if sender == names[i]:
            sender == names[i]
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
