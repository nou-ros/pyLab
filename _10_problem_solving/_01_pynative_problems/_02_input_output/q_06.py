'''
write all file content into new file by skiping line 5 from following file
'''
count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)

print(count)

with open('newFile.txt', "w") as f:
    for line in lines:
        if(count==3):
            count-=1
            continue
        else:
            f.write(line)
        count-=1
