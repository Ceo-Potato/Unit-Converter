import PySimpleGUI as sg

#the layout of the window
layout = [
    [
    sg.Input(key = "-INPUT-"),
    sg.DropDown(["km to mile", "mile to km", "kg to pound", "pound to kg", "sec to min", "min to sec"], key = "-UNITS-"),
    sg.Button("Convert", key = "-CONVERT-")
    ],
    [sg.Text("Output: ", key = "-OUTPUT-")]
]

#the window variable
window = sg.Window("Converter", layout)

while True:
    #open the window
    event, values = window.read()

    #if close window button is pressed then stop the while loop
    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_Value = values["-INPUT-"]
        if input_Value.isnumeric():
            match values["-UNITS-"]:
                case "km to mile":
                    output = round(float(input_Value) * 0.6214,3)
                    output_string = f"Output: {output}"
                case "mile to km":
                    output = round(float(input_Value) / 0.6214,3)
                    output_string = f"Output: {output}"
                case "kg to pound":
                    output = round(float(input_Value) * 2.20462,3)
                    output_string = f"Output: {output}"
                case "pound to kg":
                    output = round(float(input_Value) / 2.20462,3)
                    output_string = f"Output: {output}"
                case "sec to min":
                    output = round(float(input_Value) / 60,2)
                    output_string = f"Output: {output}"
                case "min to sec":
                    output = round(float(input_Value) * 60,2)
                    output_string = f"Output: {output}"

            window["-OUTPUT-"].update(output_string)
        else:
            window["-OUTPUT-"].update("please enter a number")
    

#close the window when while loop is stopped
window.close()