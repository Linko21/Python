from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

# from openpyxl.worksheet.worksheet import Worksheet
# import os

wb = Workbook()
ws = wb


def create_empty_excel_file():
    a = input('Bitte geben Sie einen Dateinamen ein\n')
    b = a + '.xlsx'
    wb.save(b)
    return (b)


#    print('path: '+os.path.abspath(b))
#     if not os.path.exists(b):    
#        wb.save(b)
#        print('new Workbook saved')
#    else:
#        print('use existing Workbook')

def load_excel_file():
    file_name = 'Test.xlsx'
    return load_workbook(file_name)


def row_and_col_writer():
    ws = wb.active
    ws.title = 'sheet #1'
    ws['A1'].value = 'Name'
    ws['B1'].value = 'Geburtsdatum'
    ws['A2'].value = 'Iche'
    ws['B2'].value = 'heute'
    ws['C1'].value = 'Irgendwas'
    ws['C2'].value = 'Toll'
    ws['A100'].value = '100x A'
    ws['B100'].value = '100x B'
    ws['C100'].value = '100x C'
    ws['E100'].value = '100x E'
    wb.save('Test.xlsx')


def row_and_col_reader():
    ws = wb.active
    for row in range(1, 3):
        r = ws['A' + str(row)].value
        for col in range(1, 3):
            z = ws['A' + str(col)].value
            print(r, z)


def row_and_col_reader_2():
    print("with array")
    ws = wb.active
    for row in range(1, 3):
        row_index = str(row)
        for col_index in ['A', 'B', 'C']:
            v = ws[col_index + row_index].value
            print("[" + col_index + "," + row_index + "] = " + v)


def internet_solution():
    print("internet_solution")
    wb = load_workbook('Test.xlsx')
    sheet = wb.active
    for i in range(1, sheet.max_row + 1):
        row = [cell.value for cell in sheet[i]]
        print("row " + str(i), row)

    index_of_last_row = sheet.max_row
    last_row = sheet[index_of_last_row]
    last_row_number_of_columns = len(last_row)
    for j in range(0, last_row_number_of_columns):
        print("(", index_of_last_row, ",", j, "/", last_row_number_of_columns, ") = ", last_row[j].value)

    new_row = sheet[index_of_last_row + 1]
    new_row[0].value = "foo0"
    new_row[1].value = "foo1"
    new_row[3].value = "foo3"
    wb.save('Test.xlsx')


create_empty_excel_file()
load_excel_file()
row_and_col_writer()
row_and_col_reader()
row_and_col_reader_2()
internet_solution()
