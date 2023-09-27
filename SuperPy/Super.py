# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
from argparse import *              #!of kan het met minder?!#
from csv import *                   #!of kan het met minder?!#
from datetime import *              #!of is er meer nodig?!#
#from markdown import *              #!of is er meer nodig?!#
#from rich.console import *          #!of is er meer nodig?!#

import my_csv_handler as my_csv_handler
import my_functions
import my_initiate as my_initiate

# argparse SuperPy
parser = ArgumentParser(description="Welcome to SuperPy - your command line interface. Additional information is given in 'Gebruikershandleiding SuperPy' and 'Technische handleiding SuperPy'.") 
subparsers = parser.add_subparsers(dest="command")
    
# create initiate subparser
initiate_parser = subparsers.add_parser("initiate", help="To reset SuperPy in it´s startposition on 2023-01-01.")
        
# with 1 argument
initiate_parser.add_argument("startsituation", type=str, help="Specify the situation you want to begin with.")  

# create buy subparser
buy_parser = subparsers.add_parser("buy", help="To buy SuperPy products.")
        
# with 3 arguments
buy_parser.add_argument("product_name", type=str, help="Specify the name of the product that is bought.")  
buy_parser.add_argument("price", type=float, help="Specify the price that had to be payed.")       
buy_parser.add_argument("expiration_date", type=str, help="Specify in the expiration date of the product.")  
#!voeg type toe, zodat alleen datums ingevoerd kunnen worden!#
        
# create sell subparser
sell_parser = subparsers.add_parser("sell", help="To sell SuperPy products.")
        
# with 2 arguments
sell_parser.add_argument("product_name", type=str, help="type in the name of the product that is solled.")  
sell_parser.add_argument("price", type=float, help="type in the price that is obtained.")

# create report subparser
report_parser = subparsers.add_parser("report", help="To report over SuperPy products.")
        
# with arguments
report_parser.add_argument("--type", type=str, help="Specify the report type you'd like to see (revenue, profit, csv).")
report_parser.add_argument("--period", type=str, help="Specify the periode (today, yesterday).")
report_parser.add_argument("--csv", type=str, help="Specify the csv-filename which has to be shown (SuperPy.csv, bought.csv, sold.csv, expired.csv, inventory.csv, all).")
#!bij alle een zinvolle helptekst toevoegen!#

# create date subparser
date_parser = subparsers.add_parser("date", help="To display today's date used in SuperPy.")

# with no arguments
# no arg

# create advancetime subparser
shiftdays_parser = subparsers.add_parser("shiftdays", help="To 'time travel' in SuperPy")
#!voeg zinvolle helptekst toe!#
#         
# with 1 argument
shiftdays_parser.add_argument("days", type=int, help="type in the number of days to 'time travel'.")  

# parse arguments
args = parser.parse_args()

if args.command == "initiate":
    startsituation = args.startsituation
    if startsituation == 'own':
        my_initiate.initiate(startsituation)
        print('OK, SuperPy is initiated and ready for use.')
    else:
        print(f"Sorry, 'startsituation = {startsituation}' is not a correct value. Correct value is: own.")

if args.command == "buy":
    #make new row to append
    next_bought_id = my_csv_handler.next_id('Bought.csv')
    buy_date = my_csv_handler.read_mytoday()
    
    new_row=list()
    new_row.append(str(next_bought_id))
    new_row.append(args.product_name)
    new_row.append(buy_date.strftime("%Y-%m-%d"))
    new_row.append(str(args.price))
    new_row.append(args.expiration_date)
    
    # append new row
    my_csv_handler.append_csv('Bought.csv', new_row)
    my_csv_handler.make_csv_inventory_and_expired()
    print('OK')

if args.command == "sell":
    #check: is product_name in Inventory.csv?
    found_product_id = my_functions.product_id_in_csv_inventory(args.product_name)

    if found_product_id != "":
        # make new row to append
        next_sold_id = my_csv_handler.next_id('Sold.csv')
        bought_id = found_product_id
        sell_date = my_csv_handler.read_mytoday()
    
        new_row=list()
        new_row.append(str(next_sold_id))
        new_row.append(str(bought_id))
        new_row.append(sell_date.strftime("%Y-%m-%d"))
        new_row.append(str(args.price))
    
        # append row
        my_csv_handler.append_csv('Sold.csv', new_row)
        my_csv_handler.make_csv_inventory_and_expired()
        print('OK')
    else:
        print(f'<<args.command == "sell">> Sorry, selling {args.product_name} is not possible. The product is not in inventory.')

if args.command == "report":
    if args.type == "revenue":
        if args.period == 'today':
            mytoday_datetime = my_csv_handler.read_mytoday()
            my_today = my_csv_handler.read_mytoday()
            revenue = my_functions.revenue(my_today)
            print("In SuperPy 'revenue' is defined as: the total price of all (and only) SOLD products.")
            print(f"Today's revenue: {revenue}.") 

        elif args.period == 'yesterday':
            mytoday_datetime = my_csv_handler.read_mytoday()
            print("In SuperPy 'revenue' is defined as: the total price of all (and only) SOLD products.")
            print(f"Yesterday's revenue: {my_functions.revenue(mytoday_datetime - timedelta(days=1))}") 

        else:
            print(f"Sorry, 'period = {args.period}' is not a correct value. Correct values are: today, yesterday.")

    if args.type == "profit":
        if args.period == 'today':
            mytoday_datetime = my_csv_handler.read_mytoday()
            print("In SuperPy 'profit' is defined as: the total price of (all sold products - bought products - expired products).")
            print(f"Today's profit: {my_functions.profit(mytoday_datetime)}") 
            
        elif args.period == 'yesterday':
            mytoday_datetime = my_csv_handler.read_mytoday()
            print("In SuperPy 'profit' is defined as: the total price of (all sold products - bought products - expired products).")
            print(f"Yesterday's profit: {my_functions.profit(mytoday_datetime - timedelta(days=1))}") 

        else:
            print(f"Sorry, 'period = {args.period}' is not a correct value. Correct values are: today, yesterday.")

    if args.type == "csv":
        if args.csv == "all":
            my_csv_handler.show_csv('SuperPy.csv')
            my_csv_handler.show_csv('Bought.csv')
            my_csv_handler.show_csv('Sold.csv')
            my_csv_handler.show_csv('Expired.csv')
            my_csv_handler.show_csv('Inventory.csv')
        else:
            my_csv_handler.show_csv(str(args.csv))
    
if args.command == "date":
    mytoday_datetime = my_csv_handler.read_mytoday()
    print(f'In SuperPy it is now {mytoday_datetime.strftime("%Y-%m-%d")}.')

if args.command == "shiftdays":
    my_csv_handler.modify_mytoday(args.days)
    my_csv_handler.make_csv_inventory_and_expired()

    mytoday_datetime = my_csv_handler.read_mytoday()
    print(f'In SuperPy it is now {mytoday_datetime.strftime("%Y-%m-%d")}.')