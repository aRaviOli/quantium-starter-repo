import csv
import os
import glob
import pandas as pd
from re import sub

DATA_DIR = '../data'
OUTPUT_DIR = '../output'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'pink_morsel_sales.csv')

# Make output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Use glob to grab all csv files
csv_files = glob.glob(os.path.join(DATA_DIR, '*.csv'))


def standard():
    with open(OUTPUT_FILE, mode='w') as output:
        fieldnames = ['sales', 'date', 'region']
        writer = csv.writer(output)
        writer.writerow(fieldnames)
        # dictionary method
        # writer = csv.DictWriter(output, fieldnames=fieldnames)
        # writer.writeheader()
    
        
        for csv_file in csv_files:
            with open(csv_file) as open_file:
                csv_reader = csv.reader(open_file, delimiter=',')
                
                # skips header
                next(csv_reader)

                # 0-name, 1-price, 2-quantity, 3-date, 4-region
                for row in csv_reader:
                    if row[0] == 'pink morsel':
                        price = float(sub(r'[^\d.]', '', row[1]))
                        sales = price * float(row[2])
                        writer.writerow([sales, row[3], row[4]])
                        # writer.writerow({'sales': sales, 'date': row[3], 'region': row[4]})


def using_pandas():
    dfs = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        
        pink_morsel = df[df['product'] == 'pink morsel'].copy()
        pink_morsel['price'] = pink_morsel['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
        pink_morsel['quantity'] = pink_morsel['quantity'].astype(float)
        pink_morsel['sales'] = pink_morsel['price'] * pink_morsel['quantity']

        result = pink_morsel[['sales', 'date', 'region']]
        dfs.append(result)

    df = pd.concat(dfs)
    # df = df.sort_values(by='date', ascending=True)
    df.to_csv(OUTPUT_FILE, index=False)

    
if __name__ == "__main__":
    standard()
