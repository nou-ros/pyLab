# for windows
import os 

db_user = os.environ.get('MY_EMAIL')
db_password = os.environ.get('MY_PASS')

print(db_user)
print(db_password)

'''
for linux
import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)
'''