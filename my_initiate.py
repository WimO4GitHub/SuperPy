from datetime import *
import csv
import my_functions
import my_csv_handler

def initiate(startsituation:str):
    # reset all csv-files to startvalue
    if startsituation == 'own':
        # initiate SuperPy.csv
        with open('SuperPy.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['my_today'])
            csvwriter.writerow(['2023-01-01'])
        my_csv_handler.show_csv('SuperPy.csv')
        # initiate Bought.csv
        with open('Bought.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['bought_id','product_name','buy_date','buy_price','expiration_date'])
        my_csv_handler.show_csv('Bought.csv')
        # initiate Sold.csv
        with open('Sold.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['sold_id','bought_id','sell_date','sell_price'])
        my_csv_handler.show_csv('Sold.csv')
        # initiate Expired.csv
        with open('Expired.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['date','bought_id','buy_price'])
        my_csv_handler.show_csv('Expired.csv')
        # initiate Inventory.csv
        with open('Inventory.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['date','bought_id','product_name'])
        my_csv_handler.show_csv('Inventory.csv')