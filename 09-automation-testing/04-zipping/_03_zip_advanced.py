# download a file and zip it 
import requests

import zipfile

r = requests.get('https://github.com/nou-ros/ny-folio/archive/master.zip')

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())
    data_zip.extractall('data')