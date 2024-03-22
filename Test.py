import json
import os

from openpyxl import Workbook
import requests
from openpyxl.utils.cell import column_index_from_string


keys = []
wb = Workbook()
ws = wb.active

url = 'https://api.lorcana-api.com/cards/all'
url2 = 'https://api.lorcana-api.com/sets/all'
param = dict()
resp = requests.get(url = url, params = param)
data = resp.json()

resp2 = requests.get(url = url2, params = param)
data2 = resp2.json()

keys =set()
card_sets = dict()

for a in range (len(data2)):
    sub_obj = data2[a]
    card_sets.update({sub_obj['Set_ID']: sub_obj['Set_Num']})
key = sorted(keys)

for set_id, num in card_sets.items():
    print(set_id, num)
    #ws.title = set_id + ' ' + str(num)
    ws = wb.create_sheet(set_id + ' ' + str(num))
    for f in range (len(data)):
        sub_obj1 = data[f]
        keys.update((sub_obj1.keys()))
    
        key = sorted(keys)

        for k in range (len(key)):
            ws.cell(row = (0 + 1), column = (k + 1), value = key [k]);
            
     
for p in range (len(data)):
    sub_obj2 = data[p]
for set_id, num in card_sets.items():
    print('das hier ist die zweite', set_id)
    sheet_name = str(set_id + ' ' + str(num))
    ws = wb [sheet_name]
    print('das ist hier ist ws', ws)
    if set_id  in str(sub_obj2):
        print('Das Funktioniert')
    else:
        print('Das Funktioniert nicht')
        #print('das hier ist die if', set_id)
        for j in range(len(key)):
            key_entry = key[j]
            if key_entry in sub_obj2:
                v = sub_obj2[key_entry]
                ws.cell(row = (p + 2), column = (j + 1), value = v);
        #print('Funktioniert')
    #else:
        #print('Funktioniert nicht')
      
    #for j in range(len(key)):
        #key_entry = key[j]
        #if key_entry in sub_obj2:
            #v = sub_obj2[key_entry]
            #ws.cell(row = (p + 2), column = (j + 1), value = v);
            
wb.remove(wb['Sheet'])


        
wb.save('Test.xlsx')
print('saved: ' + os.path.abspath('Test.xlsx'))