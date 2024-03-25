import PySimpleGUI as sg
dalas=[
 [sg.T("1. Kurā gadā Latvijas valsts tika dibināta?")],
 [sg.Radio('1918', 'RADIO1', default=True, key='option1'), sg.Radio('1919', 'RADIO1', key='option2'), sg.Radio('1917', 'RADIO3', default=True, key='option3')],
 [sg.Button('Nākamais jautājums')],
 [sg.T("2. Kurš bija Latvijas pirmais prezidents?")],
 [sg.Radio('Egils Levits', 'RADIO4', default=True, key='option4'), sg.Radio('Kārlis Ulmais', 'RADIO5', key='option5'), sg.Radio('Edgars Rinkēvičs', 'RADIO6', default=True, key='option6')],
 [sg.Button('Nākamais jautājums')]
]

logs=sg.Window("Viktorina", dalas, resizable=True)
while True:
    event,values=logs.read()
    if event==sg.WIN_CLOSED:
     break
logs.close()