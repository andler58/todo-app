import PySimpleGUI as gui
from Converters import convert

feet_label = gui.Text("Enter feet: ")
feet_input = gui.Input(key="feet")

inches_label = gui.Text("Enter inches: ")
inches_input = gui.Input(key="inches")

button = gui.Button("Convert")
output_label = gui.Text("", key="output")
layout = [[feet_label, feet_input], [inches_label, inches_input], [button, output_label]]

window = gui.Window("Convertor", layout=layout)

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()