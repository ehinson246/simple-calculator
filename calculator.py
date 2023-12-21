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
    sg.Text("Input_number"),
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

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()