from openpyxl import Workbook
#from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.reader.excel import load_workbook

wb= Workbook()
def createFile():
    a=input('Bitte geben Sie einen Dateinamen ein', )
    b= a+'.xlsx' 
    wb.save(b)
    
def Spaltennamen():
    c=input('Bitte geben den Dateinamen an', )
    d=c+'.xlsx'
    wb=load_workbook(d)
    ws=wb.active
    ws.title='Geburtsdatum'
    ws['A1'].value = 'Name'
    ws['B1'].value = 'Geburtsdatum'  
    wb.save(d)


createFile()
Spaltennamen()
