import smtplib, getpass


def send_email(recipient):
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()

    while True:
        print('Enter your password:')
        password = getpass.getpass()
        password = str(password)

        try:
            smtpObj.login('justseb3@gmail.com', password)
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

