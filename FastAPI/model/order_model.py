from config.sql import order_sql, order_item_sql
from model.database import DBconnect
from datetime import datetime
import time
import sys

def get_time_now():
    current_time = time.time()
    current_milli_time = int(round(current_time * 10000000))
    current_date_time = str(datetime.fromtimestamp(current_time))[:23]
    return current_milli_time, current_date_time

def data_2_list(order, order_id, purchase_time):


    order_data = []
    order_data.append([
        order_id,
        order.customer_name,
        order.customer_id,
        purchase_time
    ])

    order_item_data = []
    for item in order.order_item:
        order_item_data.append([
            order_id,
            item.product_name,
            item.amount,
            item.product_id,
            item.price
        ])
    return order_data, order_item_data

class OrderModel:
    def __init__(self):
        pass

    def Add(self, order):
        milli_time, date_time = get_time_now()
        order_data, order_item_data = data_2_list(order, milli_time, date_time)

        db_connect = DBconnect(sys.platform, 'app')
        db_connect.insert(order_sql['create_order'], order_data)
        db_connect.insert(order_item_sql['create_order_item'], order_item_data)

    def Update(self, order):
        milli_time, date_time = get_time_now()
        order_data, order_item_data = data_2_list(order, order.order_id, date_time)

        db_connect = DBconnect(sys.platform, 'app')
        db_connect.delete(order_item_sql['delete_order_item'].format(order.order_id))
        db_connect.insert(order_item_sql['create_order_item'], order_item_data)

        db_connect.delete(order_sql['delete_order'].format(order.order_id))
        db_connect.insert(order_sql['create_order'], order_data)

    def Delete(self, order_id):
        db_connect = DBconnect(sys.platform, 'app')
        db_connect.delete(order_item_sql['delete_order_item'].format(order_id))
        db_connect.delete(order_sql['delete_order'].format(order_id))