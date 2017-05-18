import csv

open_file = open('example.csv')
csv_file = csv.reader(open_file)
for row in csv_file:
    print('Row #' + str(csv_file.line_num) + ' ' + str(row))
