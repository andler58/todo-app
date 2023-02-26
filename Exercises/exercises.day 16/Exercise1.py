import PySimpleGUI as gu

label1 = gu.Text("Enter feet: ")
input1 = gu.Input()

label2 = gu.Text("Enter inches")
input2 = gu.Input()

convert_button = gu.Button("Convert")

window = gu.Window("Convert",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button]])

window.read()
window.close()
