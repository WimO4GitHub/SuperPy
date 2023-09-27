import csv
from datetime import *
import my_csv_handler

def bought_id_sold(find_bought_id:int)->bool:
#    print(f'<<bought_id_sold>> Checking if bought_id {find_bought_id} is sold.')
    find_bought_id = str(find_bought_id)

    message = False
    line_no = 0
    with open('Sold.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #sla de eerste regel met kolomnamen over
                this_bought_id = row[1]
#                print(f'<<bought_id_sold>> find_bought_id: {find_bought_id} {type(find_bought_id)}, this_bought_id: {this_bought_id} {type(this_bought_id)}.')
#                print(f'<<bought_id_sold>> compare find_bought_id == this_bought_id, {find_bought_id} == {this_bought_id}, {find_bought_id == this_bought_id}.')                                    
                if find_bought_id == this_bought_id:
#                    print(f'<<bought_id_sold>> {find_bought_id} is sold.')
                    message = True
                    break
            line_no += 1
#    print(f'<<bought_id_sold>> {message}')
#    print()            
    return message

def bought_id_expired(find_bought_id:int)->bool:
#    print(f'<<bought_id_expired>> Checking if bought_id = {find_bought_id} is expired.')
    find_bought_id = str(find_bought_id)
    mytoday_datetime = my_csv_handler.read_mytoday()
#    print(f'<<bought_id_expired>> mytoday_datetime: {mytoday_datetime} {type(mytoday_datetime)}')

    message = False
    line_no = 0
    with open('Bought.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #sla de eerste regel met kolomnamen over
                this_bought_id=row[0]
#                print(f'<<bought_id_expired>> find_bought_id: {find_bought_id} {type(find_bought_id)}, this_bought_id: {this_bought_id} {type(this_bought_id)}.')
#                print(f'<<bought_id_expired>> compare find_bought_id == this_bought_id, {find_bought_id} == {this_bought_id}, {find_bought_id == this_bought_id}.')                                    
                if find_bought_id == this_bought_id:

                    this_expires_on = row[4]
                    this_expires_on = datetime.strptime(this_expires_on + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
#                    print(f'<<bought_id_expired>> this_expires_on: {this_expires_on} {type(this_expires_on)}, mytoday_datetime: {mytoday_datetime} {type(mytoday_datetime)}.')
#                    print(f'<<bought_id_expired>> compare mytoday_datetime >= this_expires_on, {mytoday_datetime} >= {this_expires_on}, {mytoday_datetime >= this_expires_on}.')                                    
                    if mytoday_datetime >= this_expires_on:
#                        print(f'<<bought_id_expired>> bought_id {find_bought_id} with expiration_date {this_expires_on} is expired on {mytoday_datetime}')
                        message = True
                        break
            line_no += 1
#    print(f'<<bought_id_expired>> {message}')
#    print()            
    return message

def product_id_in_csv_inventory(find_product_name:str):
#    print(f'<<product_id_in_csv_inventory>> Start seaching the product_id of {find_product_name} in Inventory.csv.')

    found_product_id = ""
    line_no = 0
    with open('Inventory.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:

                this_product_name = row[2]
#                print(f'<<product_id_in_csv_inventory>> find_product_name: {find_product_name} {type(find_product_name)}, this_product_name: {this_product_name} {type(this_product_name)}.')
#                print(f'<<product_id_in_csv_inventory>> compare find_product_name == this_product_name, {find_product_name} == {this_product_name}, {find_product_name >= this_product_name}.')
                
                if find_product_name == this_product_name:
                    found_product_id = row[1]
                    break
            line_no =+ 1
    
#    print(f'<<product_id_in_csv_inventory>> {found_product_id}')
#    print()            
    return found_product_id

def find_bought_id(find_product_name:str):
#    print(f'<<find_bought_id>> Start searching bought_id for {find_product_name} in Bought.csv')
    
    mytoday_datetime = my_csv_handler.read_mytoday()
#    print(f'<<bought_id_expired>> mytoday_datetime {mytoday_datetime} {type(mytoday_datetime)}')
    
    message = ''

    with open('Bought.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
#            print(f'<<find_bought_id>> row {row}')
           
            product_name = row[1]
#            print(f'<<find_bought_id>> Check {product_name} = {find_product_name}: {product_name == find_product_name}')
            
            # check if the product_name is bought 
            if product_name == find_product_name:   # yes, it is bought
                                
                # check if it is not expired
                product_expiration_date = row[4]
#                print(f'<<find_bought_id>> Check {product_expiration_date} > {mytoday_datetime}: {product_expiration_date > mytoday_datetime}.')
                if product_expiration_date > mytoday_datetime:              # it hasn´t expired
                    
                    # check if it not sold yet
                    bought_id = row[0]
                    if not(bought_id_sold(str(bought_id))):             # it hasn't been sold yet
                        message = bought_id
#                        print(f'<<find_bought_id>> Message relating to {find_product_name} in Bought.csv: {message}.')
#                        print()
                        return message

#    print(f'<<find_bought_id>> Message relating to {find_product_name} in Bought.csv: {message}.')
#    print()     
    return message

def total_sold_price(date:datetime):
#    print(f'<<total_sold_price>> start calculating total_sold_price on {date}.')
    
    line_no = 0
    total_sold_price = 0    
    with open('Sold.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #sla de eerste regel met kolomnamen over
                this_sell_date = row[2]
                this_sell_date = datetime.strptime(this_sell_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
#                print(f'<<total_sold_price>> date: {date} {type(date)}, this_sell_date: {this_sell_date} {type(this_sell_date)}')
#                print(f'<<total_sold_price>> compare date >= this_sell_date, {date} >= {this_sell_date}, {date >= this_sell_date}')
                if date >= this_sell_date:
                    this_sell_price = float(row[3])
#                    print(f'<<total_sold_price>> this_sell_price: {this_sell_price} {type(this_sell_price)}')

                    total_sold_price = total_sold_price + this_sell_price
#                    print(f'<<total_sold_price>> line_no {line_no}, this_sell_price {this_sell_price}, total_sold_price {total_sold_price}')
            line_no =+ 1
    return total_sold_price   

def total_bought_price(date:datetime):
#    print(f'<<total_bought_price>> start calculating total_bought_price on {date}.')
    
    line_no = 0
    total_bought_price = 0    
    with open('Bought.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #sla de eerste regel met kolomnamen over
                this_buy_date = row[2]
                this_buy_date = datetime.strptime(this_buy_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
#                print(f'<<total_bought_price>> date: {date} {type(date)}, this_sell_date: {this_buy_date} {type(this_buy_date)}')
#                print(f'<<total_bought_price>> compare date >= this_sell_date, {date} >= {this_buy_date}, {date >= this_buy_date}')
                if date >= this_buy_date:
                    this_buy_price=float(row[3])
                    total_bought_price = total_bought_price + this_buy_price
#                    print(f'<<total_bought_price>> line_no {line_no}, this_buy_price {this_buy_price}, total_bought_price {total_bought_price}')
            line_no =+ 1
    return total_bought_price   

def total_expired_price(date:datetime):
#    print(f'<<total_expired_price>> start calculating total_expired_price on {date}.')
    
    line_no = 0
    total_expired_price = 0    
    with open('Expired.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if line_no >= 1:    #sla de eerste regel met kolomnamen over
                this_expire_date = row[0]
                this_expire_date = datetime.strptime(this_expire_date + ' 00:00:00', '%Y-%m-%d %H:%M:%S')
#                print(f'<<total_expired_price>> date: {date} {type(date)}, this_expire_date: {this_expire_date} {type(this_expire_date)}')
#                print(f'<<total_expired_price>> compare date >= this_expire_date, {date} >= {this_expire_date}, {date >= this_expire_date}')
                if date >= this_expire_date:
                    this_buy_price=float(row[2])
                    total_expired_price = total_expired_price + this_buy_price
#                    print(f'<<total_expired_price>> line_no {line_no}, this_buy_price {this_buy_price}, total_expired_price {total_expired_price}')
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
