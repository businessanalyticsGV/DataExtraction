import os
from os import system as cmd

server = '//10.109.10.140/InventariosCC'

### 0.- ERROR HANDLER
try:
    ls_qvd = os.listdir(server)
    print(server+'... Ready')
except:
    input('Server not in line...')
    exit()

### 1.- QLIKVIEW WITH COMMAND LINE
print('\nExtracting...')

qvdExe = 'C:/"Program Files"/QlikView/qv.exe'
qvdQVW = ' /r "C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work/00. QVDs/Extraction/DataExtraction/'
qvdQVW = qvdQVW+'Extraction.qvw"'

cmd(qvdExe+qvdQVW)

print('\nFinished...')