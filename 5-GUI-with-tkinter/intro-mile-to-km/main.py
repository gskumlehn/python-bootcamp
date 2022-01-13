import tkinter

FONT = ('Arial', 12, 'normal')

# Calculates how many KM in Mile entry and shows result in label
def calculate():
    result = float(entry.get())*1.6
    labelresult['text'] = str(round(result,2))

# Initiates window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=300)
window.config(padx=50, pady=20)

#labels
labelmiles = tkinter.Label(text='Miles', font=FONT, pady=2)
labelmiles.grid(row=0, column=2)

labelkm = tkinter.Label(text='Km', font=FONT, pady=2)
labelkm.grid(row=1, column=2)

label1 = tkinter.Label(text='is equal to', font=FONT, pady=2)
label1.grid(row=1, column=0)

labelresult = tkinter.Label(text='0', font=FONT, pady=2)
labelresult.grid(row=1, column=1)

#buttons

buttoncalc = tkinter.Button(text='Calculate', command=calculate, font=FONT, pady=2)
buttoncalc.grid(row=2, column=1)


#entry
entry = tkinter.Entry(text='0', font=FONT, width=5)
entry.grid(row=0, column=1)


window.mainloop()
