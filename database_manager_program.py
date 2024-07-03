import mysql.connector
import pandas as pd

conn = mysql.connector.connect(host='localhost',user='root',password='',database='rkpatel')
print(conn.is_connected())
cursor = conn.cursor()


def check_cred(username, password):
    cursor.execute("select *from credential")
    dataframe = pd.DataFrame(cursor.fetchall(), columns=['username', "password"])
    for i in range(0, len(dataframe)):
        row = dataframe.iloc[i]
        if username == row.username and password == row.password:
            return True

    else:
        return False


def new_login_cred(user, passw):
    cursor.execute("select *from credential")
    dataframe = pd.DataFrame(cursor.fetchall(), columns=['username', "password"])
    for i in range(0, len(dataframe)):
        row = dataframe.iloc[i]
        if user == row.username:
            return False
    cursor.execute(f"insert into credential values('{str(user)}','{str(passw)}')")
    conn.commit()
    return True


def new_login_per(user, name, add, phone):
    cursor.execute(f"insert into per_info values('{str(user)}','{str(name)}','{str(add)}',{int(phone)})")
    conn.commit()
    return


def stock_update(prod_code, prod_name, selling_price, cost_price, stock):
    selling_price = int(selling_price)
    cost_price = int(cost_price)
    stock = int(stock)
    if selling_price < cost_price:
        return ('e1')
    try:
        cursor.execute(
            f"insert into stock values('{str(prod_code)}','{str(prod_name)}',{int(selling_price)},{int(cost_price)},{int(stock)})")
    except mysql.connector.IntegrityError:
        return ('e2')

    conn.commit()
    cursor.execute(f"insert into sales values('{str(prod_code)}',0,0,0,0,0,0,0,0,0,0,0,0)")
    conn.commit()
    return ('e0')
    pass

# def create_order_table():
#     cursor.execute('select * from order_index')
#     data=pd.DataFrame(cursor.fetchall(),columns=['o_id','username','date_of_order'])
#     d=data
#     c = str(d.iloc[len(d) - 1].o_id)
#     b = c.strip('m')
#     b=1+int(b)
#     b=str(b)+'m'
#     cursor.execute(f'create table {b} (')
#     return b
#
# d=create_order_table()
# print (d)
