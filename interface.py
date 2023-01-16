from get_AI_prompt import get_prompt
import PySimpleGUI as sg
import requests
import threading

# All the stuff inside your window.
def window_layout():
    sg.theme('DarkGrey5')

    layout = [[sg.Text('Enter your email', size=(15, 1)), sg.InputText(key='-EMAIL-', size=(50, 10))],
            [sg.Text('Enter style'), sg.Combo(['business', 'casual', 'family'], key='-STYLE-', size=(15, 1))],
            [sg.Button('Create'), sg.Button('Cancel')],
            [sg.Output(size=(70, 30), font='Courier 8',
                         expand_x=True, expand_y=True, key='-OUTPUT-')]
          ]
    window = sg.Window('Email', layout, titlebar_icon=b'eye.ico', finalize=True)
    return window

window = window_layout()

while True:
    event, values = window.read()
    email = values['-EMAIL-']
    style = values['-STYLE-']
    if event == sg.WIN_CLOSED:
        break
    if event == 'Create':
        thread = threading.Thread(target=get_prompt, args=(email, style))
        thread.start()