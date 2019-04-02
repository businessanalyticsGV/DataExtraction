import os
from os import system as cmd
from sys import exit

server = '//10.109.10.140/InventariosCC'

### 1.- QLIKVIEW WITH COMMAND LINE
def Extraer():

    print('\nExtracting...')

    qvdExe = 'C:/"Program Files"/QlikView/qv.exe'
    qvdQVW = ' /r "C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/00. QVDs/Extraction/DataExtraction/'
    qvdQVW = qvdQVW+'Extraction.qvw"'

    cmd(qvdExe+qvdQVW)

    print('\nFinished...')
    os._exit(1)

### 0.- ERROR HANDLER
def Loop():
    try:
        os.listdir(server)
        Extraer()
    except:
        inp = input('\nUpdate? (anykey == yes/no)...')
        if inp == 'no': 
            exit()
        while True:
            Loop()
        exit()
Loop()