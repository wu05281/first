import csv, os

# exist_ok=True 需要时创建上级目录
os.makedirs('head_removed', exist_ok=True)
for csv_file_name in os.listdir('.'):
    if not csv_file_name.endswith('.csv'):
        continue
    csv_rows = []
    csv_file = open(csv_file_name)
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        csv_rows.append(row)
    csv_file.close()
    csv_file_new = open(os.path.join('head_removed', csv_file_name), 'w', newline='')
    csv_file_new_writer = csv.writer(csv_file_new)
    for row_new in csv_rows:
        csv_file_new_writer.writerow(row_new)
    csv_file_new.close()