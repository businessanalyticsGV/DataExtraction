import os
from os import system as cmd
from datetime import datetime as dt
from datetime import timedelta as td

path = os.getcwd().replace('\\','/')+'/'
path = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/00. QVDs/Extraction/DataExtraction/'

#### 0.- UPDATE DATE HANDLER
yesterday = dt.today()+td(days = -1)
yesterday = yesterday.strftime('%d/%m/%Y')

file = open(path+'date.txt','r')
date = file.read()
file.close()

if date == yesterday:
    print('Already updated')
    exit()

### 1.- QLIKVIEW WITH COMMAND LINE
server = '//10.109.10.140/InventariosCC'

def Extraer():

    print('\nExtracting...')

    qvdExe = 'C:/"Program Files"/QlikView/qv.exe'
    qvdQVW = ' /r "C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/00. QVDs/Extraction/DataExtraction/'
    qvdQVW = qvdQVW+'Extraction.qvw"'

    cmd(qvdExe+qvdQVW)

    ######## PASSING YESTERDAY
    file = open(path+'date.txt','w')
    file.write(yesterday)
    file.close()

    #############################################
    print('\nFinished...')
    os._exit(1)

### 0.- ERROR HANDLER
def Loop():
    try:
        inpp = input('First Update. Continue? (anykey == yes/no)... ')
        if inpp == 'no':
            os._exit(1)
        os.listdir(server)
        Extraer()
    except:
        inp = input('\nNot in line. Update? (anykey == yes/no)... ')
        if inp == 'no':
            exit()
        while True:
            Loop()
        exit()
Loop()