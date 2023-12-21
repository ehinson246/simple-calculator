#!/usr/bin/env python3

import PySimpleGUI as sg

sg.set_options(font = ('Franklin', 20), button_element_size = (6,1.5))

button_size = (6,1.5)

line_1 = [
    sg.Text("Input:"),
    sg.Push(),
    sg.Text("Running Total:")
]

line_2 = [
    sg.Text('0', key = '-INPUT-'),
    sg.Push(),
    sg.Text("RT_number")
]

line_3 = [
    sg.Button("7", key = "-SEVEN-", size = button_size),
    sg.Button("8", key = "-EIGHT-", size = button_size),
    sg.Button("9", key = "-NINE-", size = button_size),
    sg.Button("+", key = "-PLUS-", size = button_size)
]

line_4 = [
    sg.Button("4", key = "-FOUR-", size = button_size),
    sg.Button("5", key = "-FIVE-", size = button_size),
    sg.Button("6", key = "-SIX-", size = button_size),
    sg.Button("-", key = "-MINUS-", size = button_size)
]

line_5 = [
    sg.Button("1", key = "-ONE-", size = button_size),
    sg.Button("2", key = "-TWO-", size = button_size),
    sg.Button("3", key = "-THREE-", size = button_size),
    sg.Button("•", key = "-MULTIPLY-", size = button_size)
]

line_6 = [
    sg.Button("0", key = "-ZERO-", expand_x = True, size = button_size),
    sg.Button(".", key = "-DECIMAL-", size = button_size),
    sg.Button("÷", key = "-DIVIDE-", size = button_size)
]

line_7 = [
    sg.Button("Clear All", key = "-CLEAR-", expand_x = True, size = button_size),
    sg.Button("Del.", key = "-DELETE-", size = button_size),
    sg.Button("=", key = "-COMPUTE-", size = button_size)
]

layout = [
    line_1,
    line_2,
    line_3,
    line_4,
    line_5,
    line_6,
    line_7
]

window = sg.Window("Title", layout)

# digit_keys = [
#     '-ONE-',
#     '-TWO-',
#     '-THREE-',
#     '-FOUR-',
#     '-FIVE-',
#     '-SIX-',
#     '-SEVEN-',
#     '-EIGHT-',
#     '-NINE-',
#     '-ZER0-',
# ]

digit_keys = {
    '-ONE-': 1,
    '-TWO-': 2,
    '-THREE-': 3,
    '-FOUR-': 4,
    '-FIVE-': 5,
    '-SIX-': 6,
    '-SEVEN-': 7,
    '-EIGHT-': 8,
    '-NINE-': 9,
    '-ZER0-': 0,
}

def get_digit(event):
    digit = window[event].get_text()
    return digit

# def append_digit_to_input_number(digit):
#     input_number = window['-INPUT-'].get()
#     if input_number == '0':
#         input_number = str(digit)
#         window['-INPUT-'].update(input_number)
#     else:
#         input_number = input_number + str(digit)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in digit_keys:
        digit = get_digit(event)
        print(digit)
        # append_digit_to_input_number(digit)

window.close()