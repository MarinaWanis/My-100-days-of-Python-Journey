from tkinter import *

window = Tk()
window.config(padx=20,pady=20)
window.title('Miles to KM converter')


def convert_miles_to_km():
    input_entered = input.get()
    if input_entered:
        input_entered = float(input.get())

        if input_clicked.get() == "Miles":
            if output_clicked.get() == "Miles":
                miles = round(input_entered)
                result.config(text=miles)
            elif output_clicked.get() == "Kilometers":
                km = round(input_entered * 1.60934)
                result.config(text=km)
            elif output_clicked.get() == "Centimeters":
                cm = round(input_entered * 160934)
                result.config(text=cm)
            elif output_clicked.get() == "Millimeters":
                mm = round(input_entered * 1609340.0007802)
                result.config(text=mm)

    if input_clicked.get() == "Kilometers":
        if output_clicked.get() == "Miles":
            miles = round(input_entered/1.60934)
            result.config(text=miles)
        elif output_clicked.get() == "Kilometers":
            km = round(input_entered)
            result.config(text=km)
        elif output_clicked.get() == "Centimeters":
            cm = round(input_entered * 100000)
            result.config(text=cm)
        elif output_clicked.get() == "Millimeters":
            mm = round(input_entered * (10**6))
            result.config(text=mm)

    if input_clicked.get() == "Centimeters":
        if output_clicked.get() == "Miles":
            miles = round(input_entered/100)
            result.config(text=miles)
        elif output_clicked.get() == "Kilometers":
            km = round(input_entered/100000)
            result.config(text=km)
        elif output_clicked.get() == "Centimeters":
            cm = round(input_entered)
            result.config(text=cm)
        elif output_clicked.get() == "Millimeters":
            mm = round(input_entered * 10)
            result.config(text=mm)

    if input_clicked.get() == "Millimeters":
        if output_clicked.get() == "Miles":
            miles = round(input_entered/(6.2137**-7))
            result.config(text=miles)
        elif output_clicked.get() == "Kilometers":
            km = round(input_entered/(10**6))
            result.config(text=km)
        elif output_clicked.get() == "Centimeters":
            cm = round(input_entered/10)
            result.config(text=cm)
        elif output_clicked.get() == "Millimeters":
            mm = round(input_entered)
            result.config(text=mm)


input = Entry(width=10)
input.grid(column=1, row=0)

options= [
    "Miles",
    "Kilometers",
    "Centimeters",
    "Millimeters"
]
input_clicked= StringVar()
input_drop= OptionMenu(window , input_clicked, *options)
input_drop.grid(column=2, row=0)
input_clicked.set("Miles")

equal = Label(text=" =")
equal.grid(column=3, row=0)

result= Label(text=0)
result.grid(column=4, row=0)


output_clicked= StringVar()
output_drop= OptionMenu(window, output_clicked, *options)
output_drop.grid(column=5, row=0)
output_clicked.set("Kilometers")

convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=3, row=2)

window.mainloop()
