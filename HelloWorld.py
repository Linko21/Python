from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.xml.constants import MAX_ROW, MAX_COLUMN, MIN_COLUMN, MIN_ROW
#import os

wb = Workbook()
ws = wb

def create_empty_excel_file():  
    #a = input('Bitte geben Sie einen Dateinamen ein\n')
    b = 'Test.xlsx' #a+'.xlsx'
    wb.save(b)
    return(b)
#    print('path: '+os.path.abspath(b))
#     if not os.path.exists(b):    
#        wb.save(b)
#        print('new Workbook saved')
#    else:
#        print('use existing Workbook')

def load_excel_file():
    file_name='Test.xlsx'
    return load_workbook(file_name)

def row_and_col_writer():
    ws = wb.active
    ws.title ='Geburtsdatum'
    ws['A1'].value = 'Name'
    ws['B1'].value = 'Geburtsdatum'
    ws['A2'].value = 'Name'
    ws['B2'].value = 'Geburtsdatum'
    #ws['A50'].value = 120
    #ws['B100'].value = 900  
    wb.save('Test.xlsx')

def row_and_col_reader():
    ws = wb.active
#    for row in range(MIN_ROW+1,5):
#        r = ws ['A'+str(row)].value    
#        for col in range(MIN_COLUMN+1,5):
#            z = ws['A'+str(col)].value
#            print(r, z)
    for i in range(1, wb.active.max_row+1):
        row = [cell.value for cell in wb.active[i]]
        print("In Zeile "+str(i), row)
        cell = row
        if cell.value is None:
            cell.value = 'Eintrag'
            break        
        
create_empty_excel_file()
load_excel_file()
row_and_col_writer()
row_and_col_reader()