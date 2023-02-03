import functions
import PySimpleGUI as gui

label = gui.Text("Type In a To-Do: ")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")


window = gui.Window('My To-Do App:', layout=[[label], [input_box, add_button]])
window.read()
window.close()
