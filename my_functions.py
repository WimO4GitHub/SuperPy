import csv
from datetime import *
import my_csv_handler

def bought_id_sold(find_bought_id:int)->bool:
    # Checks if bought_id {find_bought_id} is sold.
    find_bought_id = str(find_bought_id)
    message = False
    line_no = 0
    with open('Sold.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_bought_id = row[1]
                if find_bought_id == this_bought_id:
                    message = True
                    break
            line_no += 1
    return message

def bought_id_expired(find_bought_id:int)->bool:
    # Checks if bought_id = {find_bought_id} is expired.
    find_bought_id = str(find_bought_id)
    mytoday_datetime = my_csv_handler.read_mytoday()
    message = False
    line_no = 0
    with open('Bought.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_bought_id=row[0]
                if find_bought_id == this_bought_id:
                    this_expires_on = row[4]
                    this_expires_on = datetime.strptime(this_expires_on + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                    if mytoday_datetime >= this_expires_on:
                        message = True
                        break
            line_no += 1
    return message

def product_id_in_csv_inventory(find_product_name:str):
    # Searches the product_id of {product_name} in Inventory.csv.
    found_product_id = ""
    line_no = 0
    with open('Inventory.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:
                this_product_name = row[2]
                if find_product_name == this_product_name:
                    found_product_id = row[1]
                    break
            line_no =+ 1
    return found_product_id

def find_bought_id(find_product_name:str):
    # print(f'<<find_bought_id>> Start searching bought_id for {find_product_name} in Bought.csv')
    
    mytoday_datetime = my_csv_handler.read_mytoday()
    # Searches bought_id for {find_product_name} in Bought.csv
    message = ''
    with open('Bought.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            product_name = row[1]
            # check if the product_name is bought 
            if product_name == find_product_name:   # yes, it is bought
                # check if it is not expired
                product_expiration_date = row[4]
                if product_expiration_date > mytoday_datetime:          # it hasn´t expired
                    # check if it not sold yet
                    bought_id = row[0]
                    if not(bought_id_sold(str(bought_id))):             # it hasn't been sold yet
                        message = bought_id
                        return message
    return message

def total_sold_price(date:datetime):
    # Calculates the total_sold_price up to and including the specified date    
    line_no = 0
    total_sold_price = 0    
    with open('Sold.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_sell_date = row[2]
                this_sell_date = datetime.strptime(this_sell_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date >= this_sell_date:
                    this_sell_price = float(row[3])
                    total_sold_price = total_sold_price + this_sell_price
            line_no =+ 1
    return total_sold_price   

def total_bought_price(date:datetime):
    # Calculates the total_bought_price up to and including the specified date
    line_no = 0
    total_bought_price = 0    
    with open('Bought.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_buy_date = row[2]
                this_buy_date = datetime.strptime(this_buy_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date >= this_buy_date:
                    this_buy_price=float(row[3])
                    total_bought_price = total_bought_price + this_buy_price
            line_no =+ 1
    return total_bought_price   

def total_expired_price(date:datetime):
    # Calculates the total_expired_price up to and including the specified date
    line_no = 0
    total_expired_price = 0    
    with open('Expired.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_expire_date = row[0]
                this_expire_date = datetime.strptime(this_expire_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date >= this_expire_date:
                    this_buy_price=float(row[2])
                    total_expired_price = total_expired_price + this_buy_price
            line_no =+ 1
    return total_expired_price   

def revenue(date:datetime):
    # In SuperPy 'revenue' is defined as: the total price of all (and only) SOLD products
    revenue = total_sold_price(date)
    return revenue
    
def profit(date:datetime):
    # In SuperPy 'profit' is defined as: the total price of (all sold products - bought products - expired products)."
    profit = total_sold_price(date) - total_bought_price(date) - total_expired_price(date)
    return profit

def this_date_total_sold_price(date:datetime):
    # Calculaties the total_sold_price on the specified date    
    line_no = 0
    this_date_total_sold_price = 0    
    with open('Sold.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_sell_date = row[2]
                this_sell_date = datetime.strptime(this_sell_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date == this_sell_date:
                    this_sell_price = float(row[3])
                    this_date_total_sold_price = this_date_total_sold_price + this_sell_price
            line_no =+ 1
    return this_date_total_sold_price   

def this_date_total_bought_price(date:datetime):
    # Calculaties the total_bought_price on the specified date
    line_no = 0
    this_date_total_bought_price = 0    
    with open('Bought.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_buy_date = row[2]
                this_buy_date = datetime.strptime(this_buy_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date == this_buy_date:
                    this_buy_price=float(row[3])
                    this_date_total_bought_price = this_date_total_bought_price + this_buy_price
            line_no =+ 1
    return this_date_total_bought_price   

def this_date_total_expired_price(date:datetime):
    # Calculates the total_expired_price on the specified date
    line_no = 0
    this_date_total_expired_price = 0    
    with open('Expired.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #skip the first row with coumn headers
                this_expire_date = row[0]
                this_expire_date = datetime.strptime(this_expire_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
                if date == this_expire_date:
                    this_buy_price=float(row[2])
                    this_date_total_expired_price = this_date_total_expired_price + this_buy_price
            line_no =+ 1
    return this_date_total_expired_price   

def this_date_revenue(date:datetime):
    # In SuperPy 'revenue' is defined as: the total price of all (and only) SOLD products
    this_date_revenue = this_date_total_sold_price(date)
    return this_date_revenue
    
def this_date_profit(date:datetime):
    # In SuperPy 'profit' is defined as: the total price of (all sold products - bought products - expired products)."
    this_date_profit = this_date_total_sold_price(date) - this_date_total_bought_price(date) - this_date_total_expired_price(date)
    return this_date_profit