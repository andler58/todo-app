import PySimpleGUI as gui

label1 = gui.Text("Select files to compress: ")
input1 = gui.Input()
choose_button1 = gui.FilesBrowse("Choose")

label2 = gui.Text("Select destination folder: ")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose")

compress_button = gui.Button("Compress")

window = gui.Window("File Compressor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]])


window.read()
window.close()
