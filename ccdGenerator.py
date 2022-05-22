import csv

with open('certList.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        with open('ccd_files/' + row[0], 'w') as ccd:
            ccd.write('ifconfig-push ' + row[1] + ' 255.255.255.0')
            ccd.close()
    file.close()
