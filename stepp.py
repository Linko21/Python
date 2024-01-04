from datetime import datetime

from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook


def create_empty_excel_file(file_name):
    workbook = Workbook()
    workbook.save(file_name)
    return file_name


def load_excel_file(name):
    return load_workbook(name)


def fill_data(workbook):
    ws = workbook.active
    ws.title = 'Geburtsdatum'
    ws['A1'].value = 'Name'
    ws['A2'].value = 'in Name'
    ws['B1'].value = 'Geburtsdatum'
    ws['B2'].value = 'jeden tag :D'
    ws['C1'].value = 'Aktuelle Zeit'
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    ws['C2'].value = current_time


file_name1 = create_empty_excel_file("Bestellungen.xlsx")
file_name2 = create_empty_excel_file("Buchungen.xlsx")
file_name3 = create_empty_excel_file("Test3.xlsx")
wb1 = load_excel_file(file_name1)
wb2 = load_excel_file(file_name2)
wb3 = load_excel_file(file_name3)
fill_data(wb1)
fill_data(wb2)
fill_data(wb3)
wb1.save(file_name1)
wb2.save(file_name2)
wb3.save(file_name3)
