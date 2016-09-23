#coding=ascii
import csv
# import os
#
my_file = 'C:\\Users\\chloe\\AppData\\Local\\Programs\\Python\\Python35\\chloetest\\canshu1.csv'
readers = csv.reader(open(my_file,'rt'))
# freaders = csv.reader(my_file,'rb')
# headers = next(freaders)
for reader in readers:
    print(reader[0])
    print(reader[1])
    print(reader[2])
    print(reader[3])
#import csv
with open( 'C:\\Users\\chloe\\AppData\\Local\\Programs\\Python\\Python35\\chloetest\\canshu1.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

f.close()