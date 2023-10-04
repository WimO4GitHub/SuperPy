import csv
from datetime import *
import my_functions

def read_mytoday():
    # read my_today from Today.csv
    line_no = 0
    with open('SuperPy.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                my_today=row[0]
            line_no =+ 1
    my_today = row[0]
    my_today_datetime = datetime.strptime(my_today, '%Y-%m-%d')
    return my_today_datetime

def modify_mytoday(shift_in_days:int)->datetime:
    # define new my_today
    my_today_datetime = read_mytoday()
    my_new_today_datetime = my_today_datetime + timedelta(days=shift_in_days)
    my_new_today_datetime = my_new_today_datetime.strftime('%Y-%m-%d')
    my_today_datetime = my_today_datetime.strftime('%Y-%m-%d')
    # write to SuperPy.csv
    new_row=list()
    new_row.append(my_new_today_datetime)
    with open('SuperPy.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['my_today']) 
        csvwriter.writerow(new_row)

def next_id(csv_name:str)->int:
    # counting lines in {csv_name}
    line_no = 0
    with open(csv_name, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            line_no += 1
    next_id = line_no
    return next_id

def show_csv(csv_name:str):
    # show table content {csv_name} to user
    row_no = 0
    with open(csv_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row_no == 0:
                print(f'---{csv_name}---------------------------')
                print(row)
            else:
                print(row)
            row_no =+ 1
    print()

def append_csv(csv_name:str, new_row:list):
    # append row to {csv_name}
    with open(csv_name, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_row)

def make_csv_inventory_and_expired():
    # make a new Inventory.csv and Expired.csv')
    with open('Inventory.csv', 'w', newline='') as csvfile:
        csvwriterInventory = csv.writer(csvfile)
        csvwriterInventory.writerow(['date','bought_id','product_name']) 
        with open('Expired.csv', 'w', newline='') as csvfile:
            csvwriterExpired = csv.writer(csvfile)
            csvwriterExpired.writerow(['date','bought_id','buy_price']) 
            line_no = 0
            with open('Bought.csv', 'r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if line_no >= 1:    #skip the first row with coumn headers
                        bought_id = row[0]
                        product_name = row[1]
                        buy_date = row [2]
                        buy_date = datetime.strptime(buy_date, '%Y-%m-%d')
                        buy_price = row[3]
                        expiration_date = row[4]
                        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
                        # check if product_id is sold
                        bought_id_sold = my_functions.bought_id_sold(bought_id)
                        if bought_id_sold:
                            1 == 1 # a dummy line
                        else:
                            # check if product is expired
                            if my_functions.bought_id_expired(bought_id):
                                # define new row
                                new_row=list()
                                new_row.append(buy_date.strftime("%Y-%m-%d"))
                                new_row.append(str(bought_id))
                                new_row.append(str(buy_price))
                                # write row to Expired.csv
                                csvwriterExpired.writerow(new_row) 
                            else:
                                # define new row
                                new_row=list()
                                new_row.append(buy_date.strftime("%Y-%m-%d"))
                                new_row.append(str(bought_id))
                                new_row.append(str(product_name))
                                # write to Inventory.csv
                                csvwriterInventory.writerow(new_row) 
                    line_no =+ 1 