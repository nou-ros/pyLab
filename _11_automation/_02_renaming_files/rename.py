import os

os.chdir('F:\\Python\\automation\\renaming_files\\files')

# print(os.getcwd())

#listing all the files in the directory.
for f in os.listdir():
    # print(f)
    # separating files by name and extension
    # print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    # print(file_name.split(' '))
    f_title, f_course, f_num = f_name.split(" ")
    # print(f_num)
    f_num = f_num[1:2]
    #The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
    f_num = f_num.zfill(2)
    # print(f'{f_num}-{f_title}{f_ext}')
    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(f, new_name)