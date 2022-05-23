import csv

CFG_NAME = 0
IP_ADDR = 1

with open('certList.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        with open('ccd_files/' + row[CFG_NAME], 'w') as ccd:
            ccd.write('ifconfig-push ' + row[IP_ADDR] + ' 255.255.255.0')
