import PySimpleGUI as sg



dalas = [
    [sg.T("1. Kurā gadā Latvijas valsts tika dibināta?")],
    [sg.Radio('1918', 'RADIO1', default=True, key='VAR1'), sg.Radio('1919', 'RADIO1', key='VAR2'), sg.Radio('1917', 'RADIO1', key='VAR3')],
    [sg.Button('Nākamais jautājums', key='q')],

    [sg.T("2. Kurš bija Latvijas pirmais prezidents?")],
    [sg.Radio('Egils Levits', 'RADIO2', default=True, key='VAR4'), sg.Radio('Kārlis Ulmanis', 'RADIO2', key='VAR5'), sg.Radio('Edgars Rinkēvičs', 'RADIO2', key='VAR6')],
    [sg.Button('Nākamais jautājums', key='w')],

    [sg.T("3.Kādas krāsas tiek attēlotas Latvijas valsts karogā?")],
    [sg.CB('Sarkans',  'RADIO1', key='VAR7'), sg.CB('Balts', key='VAR8'), sg.CB('Zils', key='VAR9')],
    [sg.Button('Nākamais jautājums', key='e')],

    [sg.T("4. Kā sauca padomju savienību?")],
    [sg.Radio('PSRS', 'RADIO4', default=True, key='VAR10'), sg.Radio('UTP', 'RADIO4', key='VAR11'), sg.Radio('RSPS', 'RADIO4', key='VAR12')],
    [sg.Button('Nākamais jautājums', key='r')],

    [sg.T("5. kurā datumā tika dibināta LATVIJA?")],
    [sg.Radio('12. dec', 'RADIO5', default=True, key='VAR13'), sg.Radio('16. nov', 'RADIO5', key='VAR14'), sg.Radio('18. nov', 'RADIO5', key='VAR15')],
    [sg.Button('Nākamais jautājums', key='t')],

    [sg.T("6. Zem kuras vasts/ vienības bija Latvija padomju laikos?")],
    [sg.Radio('Francija', 'RADIO6', default=True, key='VAR16'), sg.Radio('Spānija', 'RADIO6', key='VAR17'), sg.Radio('PSRS', 'RADIO6', key='VAR18')],
    [sg.Button('Nākamais jautājums', key='y')],

    [sg.T("7. Kurā gadā Latvija atguva savu neatkarību?")],
    [sg.Radio('1989', 'RADIO7', default=True, key='VAR19'), sg.Radio('1986', 'RADIO7', key='VAR20'), sg.Radio('1983', 'RADIO7', key='VAR21')],
    [sg.Button('Nākamais jautājums', key='u')],

    [sg.T("8. Kurā gadā notika Barikāžu diena?")],
    [sg.Radio('Egils Levits', 'RADIO8', default=True, key='VAR4'), sg.Radio('Kārlis Ulmanis', 'RADIO8', key='VAR5'), sg.Radio('Edgars Rinkēvičs', 'RADIO8', key='VAR6')],
    [sg.Button('Nākamais jautājums', key='i')],

    [sg.Button("Pabeigt")],
    [sg.Multiline(size=(40, 10), key='Multilains', disabled=True)]

]

window = sg.Window("Viktorina", dalas, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break 
    elif event == 'q':
       pirmais=values["RADIO1"]
       window["Multilains"].update(f"Jūsu atbilde:{pirmais}")
    elif event == 'w':
       otrais=values["RADIO2"]
    elif event == 'e':
       tres=values["RADIO3"]
    elif event == 'r':
       cet=values["RADIO4"]
    elif event == 't':
       piek=values["RADIO5"]
    elif event == 'y':
       sest=values["RADIO6"]
    elif event == 'u':
       sept=values["RADIO7"]
    elif event == 'i':
       ast=values["RADIO8"]

    
       
       
     
    elif event == 'Pabeigt':
     print("Paldies!") 

window.close()
