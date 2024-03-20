"""CSV fiiles"""

import csv
# to write in csv file
# with open('data.csv', 'w', ) as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'age'])
#     writer.writerow(['Hashir Nouman', 23])
#     writer.writerow(['Mutahar Nouman', 27])

# read from csv
with open("data.csv") as file:
    reader = csv.reader(file)
    # if the for loop after print won't run because the cursor was at the start
    # but conversion to list with list() method will put curosr at the end of file
    # print(list(reader))
    for row in reader:
        print(row)
