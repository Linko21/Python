import json
import os

from openpyxl import Workbook
import requests
from openpyxl.utils.cell import column_index_from_string


keys = []
wb = Workbook()
ws = wb.active

url = 'https://api.lorcana-api.com/cards/all'
param = dict()
resp = requests.get(url = url, params = param)
data = resp.json()


for f in range (len(data)):
    sub_obj1 = data[f]
    keys = list(sub_obj1.keys())
    
key = set(keys)
key_sorted = sorted(key)

for k in range (len(key_sorted)):
    ws.cell(row = (0 + 1), column = (k + 1), value = key_sorted [k]);
    
for p in range (len(data)):
    sub_obj2 = data[p]
      
    for j in range(len(key_sorted)):
        key_entry = key_sorted[j]
        if key_entry in sub_obj2:
            v = sub_obj2[key_entry]
            ws.cell(row = (p + 2), column = (j + 1), value = v);
        
wb.save('Test.xlsx')
print('saved: ' + os.path.abspath('Test.xlsx'))