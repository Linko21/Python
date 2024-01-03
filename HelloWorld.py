from openpyxl import Workbook
wb= Workbook()
#ws=wb.active

def createFile():
    a=input('Bitte geben Sie einen Dateinamen ein', )
    b= a+'.xlsx'

    wb.save(b)

#ws.title='Geburtsdatum'
#ws['A1'].value = 'Name'
#ws['B1'].value = 'Geburtsdatum'  
createFile()
