import zipfile

'''
my_zip = zipfile.ZipFile('files.zip', 'w')
my_zip.write('test.txt')
my_zip.write('thumb.png')
my_zip.close()
'''
'''
# with context manager, without compression
with zipfile.ZipFile('files.zip', 'w') as my_zip:
    my_zip.write('test.txt')
    my_zip.write('thumb.png')
'''
'''
# with compression
with zipfile.ZipFile('files_comp.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('test.txt')
    my_zip.write('thumb.png')
'''

# extracting zip file
with zipfile.ZipFile('files_comp.zip', 'r') as my_zip:
    # print(my_zip.namelist())
    # my_zip.extractall('files')
    my_zip.extract('thumb.png')