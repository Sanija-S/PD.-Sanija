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

atb = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break 
    elif event == 'q':
       atb.append(values["VAR1"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR1']}\n")
    elif event == 'w':
       atb.append(values["VAR4"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR4']}\n")
    elif event == 'e':
       cb_answers = [key for key, value in values.items() if key.startswith('VAR') and value]
       atb.extend(cb_answers)
       window["Multilains"].update(f"Jūsu atbildes: {' '.join(cb_answers)}\n")
    elif event == 'r':
       atb.append(values["VAR10"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR10']}\n")
    elif event == 't':
       atb.append(values["VAR13"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR13']}\n")
    elif event == 'y':
       atb.append(values["VAR16"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR16']}\n")
    elif event == 'u':
       atb.append(values["VAR19"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR19']}\n")
    elif event == 'i':
       atb.append(values["VAR20"])
       window["Multilains"].update(f"Jūsu atbilde:{values['VAR19']}\n")
       for answer in atb:
           print(answer)
       break

    
       
       
     
    elif event == 'Pabeigt':
     print("Paldies!") 

window.close()
