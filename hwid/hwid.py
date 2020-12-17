import requests
import subprocess
import mysql.connector

mainDrive = str(subprocess.check_output('wmic diskdrive get serialnumber')).split('\\r\\n')[1].strip('\\r').strip()
sysModel = str(subprocess.check_output('wmic computersystem get model')).split('\\r\\n')[1].strip('\\r').strip()
baseBoard = str(subprocess.check_output('wmic baseboard get serialnumber')).split('\\r\\n')[1].strip('\\r').strip()

hwid = (mainDrive + sysModel + baseBoard)


req = requests.get('http://localhost/pyhwid/auth.php?hwid=' + hwid)

if req.text == 'authed':
    print('Hardware Authenticated')
else:
    print('Error with Hardware ID, please contact support')
