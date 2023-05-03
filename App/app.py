import PySimpleGUI as sg 

#definicion de tema
sg.theme('black') 

  
layout = [[sg.Text('Inicializar app?...')], 
          [sg.Button('START'), sg.Button('CANCEL')] ] 
 
window = sg.Window('safe-eye', layout,no_titlebar=True,grab_anywhere=True)
 
while True: 
    event, values = window.read() 
    if event in (None, 'CANCEL'): 
        break 
    
    if event == 'START':
        print('inicializado....')
         
window.close()