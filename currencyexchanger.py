import requests
from tkinter import *
from tkinter.ttk import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Currency exchanger")
        self.currencies = sorted([i for i in self.get_change_rate().keys()])
        self.rates_list = self.get_change_rate()
        self.resultat = StringVar()

        self.label1 = Label(master, text="value and currency:")
        self.label1.grid(row=0, column=0)
        
        self.entry1 = Entry(master)
        self.entry1.grid(row=0, column=1)

        self.combo1 = Combobox(master, values=self.currencies)
        self.combo1.grid(row=0, column=2)
        self.combo1.current(0)

        self.label2 = Label(master, text="change currency:")
        self.label2.grid(row=1, column=0)

        self.equal = Label(master, textvariable=self.resultat)
        self.equal.grid(row=1, column=1)

        self.combo2 = Combobox(master, values=self.currencies)
        self.combo2.grid(row=1, column=2)
        self.combo2.current(0)

        self.calculate = Button(master, text="Calculate", command=self.get_values)
        self.calculate.grid(row=2, column=0, columnspan=3)



    def get_values(self):
        self.resultat.set(str(round(float(self.entry1.get()) * (1 / self.rates_list[self.combo1.get()]) * self.rates_list[self.combo2.get()],2)))

    def get_change_rate(self):
        response = requests.get("https://api.exchangeratesapi.io/latest")
        return response.json()["rates"]


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
