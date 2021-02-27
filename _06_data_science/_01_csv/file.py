import csv

'''
# reading the the new file with tab delimater
with open("new_names.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")

    for line in csv_reader:
        print(line)
'''

# regular read and writer
'''
with open("names.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # will return an object
    # print(csv_reader)

    # next(csv_reader)

    # for line in csv_reader:
    #         print(line[2])

    # writing to a different csv file with dash delimater
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
'''

'''
# another way to read csv file with dictreader
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line)
        print(line['email'])
'''

'''
# dictreader and dictwriter
# write with dictwriter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('dict_file.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames= fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            # print(line)
            del line['email']
            csv_writer.writerow(line)
'''


'''
We should not naem a file csv.py. When we do, Python will look in our file for the csv code instead of the standard library csv module.
'''