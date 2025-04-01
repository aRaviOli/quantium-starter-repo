import csv
import os
import glob
import pandas as pd
from re import sub

csv_dir = '../data'
output_dir = '../output'
output_file = os.path.join(output_dir, 'pink_morsel_sales.csv')

# Making an output directory
os.makedirs(output_dir, exist_ok=True)

# Using glob to grab all csv files
csv_files = glob.glob(os.path.join(csv_dir, '*.csv'))

with open(output_file, mode='w') as output:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for csv_file in csv_files:
        with open(csv_file) as open_file:
            csv_reader = csv.reader(open_file, delimiter=',')
            next(csv_reader)

            # 0-name, 1-price, 2-quantity, 3-date, 4-region
            for row in csv_reader:
                if row[0] == 'pink morsel':
                    price = float(sub(r'[^\d.]', '', row[1]))
                    sales = price * float(row[2])
                    sales = "${:,.2f}".format(sales)

                    writer.writerow({'sales': sales, 'date': row[3], 'region': row[4]})
    