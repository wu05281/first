import csv


out_file = open('output_file.csv', 'w', newline='')
# 用制表符代替逗号来分隔单元格，并有两倍行距
# out_file_writer = csv.writer(out_file, delimiter='\t', lineterminator='\n\n')
out_file_writer = csv.writer(out_file)
out_file_writer.writerow(['a','b',3])
out_file.close();