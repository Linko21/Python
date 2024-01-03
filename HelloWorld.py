from openpyxl import Workbook
wb= Workbook()
#ws=wb.active
def Datei_Erstellen():
    a=input('Geben Sie einen Dateinahmen ein', )
    b= a+'.xlsx'

    wb.save(b)

#ws.title='Geburtsdatum'
#ws['A1'].value = 'Name'
#ws['B1'].value = 'Geburtsdatum'  
Datei_Erstellen()