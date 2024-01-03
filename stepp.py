from datetime import datetime

from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook


def create_empty_excel_file():
    file_name = "Test.xlsx"
    workbook = Workbook()
    workbook.save(file_name)
    return "Test.xlsx"


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


fileName = create_empty_excel_file()
wb = load_excel_file(fileName)
fill_data(wb)
wb.save(fileName)
