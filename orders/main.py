import os.path
import tkinter as tk

from openpyxl.workbook import Workbook

from orders import Utils
from orders.Utils import Dishes

random_values = Utils.RandomValues(1)


def create_result():
    print("Berechne Ergebnis tut gerade noch nix ...")
    # TODO lies beide excel tabellen ein und bestimme den preis pro person, was wer zu zahlen hat
    # wenn derjenige gerade geburtstag hat, ist die bestellung 20% günstiger


def create_new_prices():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Preise'
    ws['A1'].value = 'Gericht'
    ws['B1'].value = 'Preis'
    for i in range(0, len(Dishes)):
        ws["A" + str(i + 2)].value = Dishes[i]
        ws["B" + str(i + 2)].value = random_values.float_value()
    name = "prices.xlsx"
    wb.save(name)
    print("created: " + os.path.abspath(name))


def create_new_orders():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Bestellungen'
    ws['A1'].value = 'Vorname'
    ws['B1'].value = 'Nachname'
    ws['C1'].value = 'Geburtsdatum'
    ws["D1"].value = "Gericht"
    ws["E1"].value = "Anzahl"
    for i in range(2, 6):
        ws['A' + str(i)] = random_values.first_name()
        ws['B' + str(i)].value = random_values.last_name()
        ws['C' + str(i)].value = random_values.date(today=random_values.boolean_value())
        ws['D' + str(i)].value = Dishes[random_values.int_value(1, len(Dishes) - 1)]
        ws['E' + str(i)].value = random_values.int_value()
    name = "orders.xlsx"
    wb.save(name)
    print("created: " + os.path.abspath(name))


gui = tk.Tk()

file_name_input_value = tk.StringVar()

create_new_orders_button = tk.Button(gui, text="Bestellungen neu erstellen", command=create_new_orders)
create_new_orders_button.pack()

create_new_prices_button = tk.Button(gui, text="Preise neu erstellen", command=create_new_prices)
create_new_prices_button.pack()

result_label = tk.Label(gui, text="Dateiname für Ergebnis")
result_label.pack()

file_name_text_box = tk.Entry(gui, textvariable=file_name_input_value)
file_name_text_box.insert(0, "result.xlsx")
file_name_text_box.pack()

create_result_button = tk.Button(gui, text="Berechne Ergebnis", command=create_result)
create_result_button.pack()

gui.mainloop()
