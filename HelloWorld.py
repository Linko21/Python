from openpyxl import Workbook
#from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.reader.excel import load_workbook
import os

wb= Workbook()
def create_File():  
    a=input('Bitte geben Sie einen Dateinamen ein\n')
    b= a+'.xlsx'
    print('path: '+os.path.abspath(b))
    if not os.path.exists(b):    
        wb.save(b)
        print('new Workbook saved')
    else:
        print('use existing Workbook')
    
def Spaltennamen():
    c=input('Bitte geben den Dateinamen an\n')
    d=c+'.xlsx'
    wb=load_workbook(d)
    ws=wb.active
    ws.title='Geburtsdatum'
    ws['A1'].value = 'Name'
    ws['B1'].value = 'Geburtsdatum'  
    wb.save(d)


createFile()
Spaltennamen()

