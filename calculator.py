#!/usr/bin/env python3

import PySimpleGUI as sg

layout = [[]]

window = sg.Window("Title", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()