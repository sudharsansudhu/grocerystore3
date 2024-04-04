from back_end.sql_connection import get_sql_connection


def delete_product(connection,order_id):
    cursor = connection.cursor()
    query = ("DELETE FROM orders where order_id ="+str(order_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 1))