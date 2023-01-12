order_sql = {
    'create_order': "INSERT INTO [Order] (order_id, customer_name, customer_id, purchase_time) VALUES(?, ?, ?, ?)",
    'delete_order': "DELETE FROM [Order] WHERE order_id = '{}'"
}

order_item_sql = {
    'create_order_item': "INSERT INTO Order_item (order_id, product_name, amount, product_id, price) VALUES(?, ?, ?, ?, ?)",
    'delete_order_item': "DELETE FROM Order_item WHERE order_id = '{}'"
}
