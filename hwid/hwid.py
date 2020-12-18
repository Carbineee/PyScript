import requests
import subprocess
import hashlib
import os
import binascii

mainDrive = str(subprocess.check_output('wmic diskdrive get serialnumber')).split('\\r\\n')[1].strip('\\r').strip()
sysModel = str(subprocess.check_output('wmic computersystem get model')).split('\\r\\n')[1].strip('\\r').strip()
baseBoard = str(subprocess.check_output('wmic baseboard get serialnumber')).split('\\r\\n')[1].strip('\\r').strip()

hwid = (mainDrive + sysModel + baseBoard)




def login():

    username = input('Enter your username: ')
    password = input('Enter your password: ')
    hashPass = hashlib.md5( password.encode('utf-8') ).hexdigest()

    req = requests.get('http://localhost/auth.php?username=' + username + '&password=' + hashPass)

    print('http://localhost/auth.php?username=' + username + '&password=' + hashPass)


def register():

    print('Register')

    username = input('Enter a username: ')
    password = input('Enter a password: ')
    code = input('Enter Invite Code: ')

    hashPass = hashlib.md5( password.encode('utf-8') ).hexdigest()

    req = requests.get('http://localhost/register.php?username=' + username + '&password=' + hashPass + '&code=' + code)

    print(req.text)

register()