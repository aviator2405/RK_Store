import pandas as pd
import numpy as np
# import csv
import matplotlib.pyplot as plt
import mysql.connector
import winsound

conn = mysql.connector.connect(host="localhost", user="root", password='', database='rkpatel')
cursor = conn.cursor()

plt.rcParams["figure.figsize"] = (10, 8)


def Items():
    c = []
    df = pd.read_csv("G:\STORE_MANAGEMENT_IN_PYTHON_WITH_SOURCE_CODE\ITEM.csv")
    loop = True
    while loop == True:
        e = input("Do u want to add an item (Y/N) : ")
        if (e == "Y") or (e == "y"):
            a = input("Enter Item_Id(id) of product to be added : ")
            b = int(input("Enter quantity of item : "))
            if ((df["ITEM_CODE"] == a).any()):
                d = df[df["ITEM_CODE"] == a]
                f = list(d["SELLING_PRICE"])
                for i in f:
                    c.append(i * b)

            else:
                print("Id not valid!!")
        elif ((e == "N") or (e == "n")):
            loop = False
            print("Thank you for shopping \nYour total amount is : ", sum(c))
        else:
            print("Please enter Yes(Y) or No(N)")

    return (sum(c))


def profit(useless):
    winsound.Beep(400, 200)
    cursor.execute("select * from sales")
    df1 = pd.DataFrame(cursor.fetchall(),
                       columns=['prod_code', "jan", 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct',
                                'nov', 'decem'])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        r = df1.iloc[i]
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        sum = int(r.jan) + int(r.feb) + int(r.mar) + int(r.apr) + int(r.may) + int(r.jun) + int(r.jul) + int(
            r.aug) + int(r.sept) + int(r.oct) + int(r.nov) + int(r.decem)
        total = diff * sum
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in last Year (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_jan(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jan from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jan"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].jan)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in January (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_feb(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,feb from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "feb"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].feb)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in february (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_mar(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,mar from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "mar"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].mar)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in march (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_apr(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,apr from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "apr"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].apr)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in april (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_may(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,may from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "may"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].may)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in may (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_jun(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jun from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jun"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].jun)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in june (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_jul(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jul from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jul"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].jul)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in july (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_aug(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,aug from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "aug"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].aug)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in augest (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_sept(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,sept from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "sept"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].sept)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in september (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_oct(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,oct from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "oct"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].oct)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in october (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_nov(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,nov from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "nov"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].nov)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in november (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def total_profit_decem(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,decem from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "decem"])
    print(df1)
    cursor.execute("select prod_code,selling_price,cost_price from stock")
    df2 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'selling_price', "cost_price"])
    profit = []
    for i in range(len(df2)):
        diff = int(df2.iloc[i].selling_price) - int(df2.iloc[i].cost_price)
        total = diff * int(df1.iloc[i].decem)
        profit.append(total)
    fig, ax = plt.subplots()
    # df1 = pd.read_csv(filename)
    x = list(df1["prod_code"])
    y = profit
    plot = plt.bar(np.arange(len(x)), y, color="orange")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Total profit in december (in Rs.)")
    plt.xlabel("Item Code")
    plt.ylabel("Total profit (in k)")
    plt.show()


def sales(useless):
    winsound.Beep(400, 200)
    cursor.execute("select * from sales")
    df1 = pd.DataFrame(cursor.fetchall(),
                       columns=['prod_code', "jan", 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct',
                                'nov', 'decem'])
    print(df1)
    prod_code = []
    totalsal = []
    for i in range(len(df1)):
        r = df1.iloc[i]
        prod_code.append(r.prod_code)
        sum = int(r.jan) + int(r.feb) + int(r.mar) + int(r.apr) + int(r.may) + int(r.jun) + int(r.jul) + int(
            r.aug) + int(r.sept) + int(r.oct) + int(r.nov) + int(r.decem)

        totalsal.append(sum)

    fig, ax = plt.subplots()

    x = list(prod_code)
    y = list(totalsal)
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units soid last Year')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in the year")
    plt.show()


def sales_jan(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jan from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jan"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['jan'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in January')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in January")
    plt.show()
    return ()


def sales_feb(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,feb from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "feb"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['feb'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in February')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in February")
    plt.show()
    return ()


def sales_mar(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,mar from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "mar"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['mar'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in March')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in March")
    plt.show()
    return ()


def sales_apr(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,apr from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "apr"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['apr'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in April')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in April")
    plt.show()
    return ()


def sales_may(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,may from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "may"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['may'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in Mayr')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in May")
    plt.show()
    return ()


def sales_jun(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jun from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jun"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['jun'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in June')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in June")
    plt.show()
    return ()


def sales_jul(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,jul from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "jul"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['jul'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in July')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in July")
    plt.show()
    return ()


def sales_aug(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,aug from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "aug"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['aug'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in August')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in August")
    plt.show()
    return ()


def sales_sept(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,sept from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "sept"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['sept'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in September')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in September")
    plt.show()
    return ()


def sales_oct(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,oct from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "oct"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['oct'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in October')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in October")
    plt.show()
    return ()


def sales_nov(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,nov from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "nov"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['nov'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in November')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in November")
    plt.show()
    return ()


def sales_decem(useless):
    winsound.Beep(400, 200)
    cursor.execute("select prod_code,decem from sales")
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "decem"])
    fig, ax = plt.subplots()

    x = list(df1["prod_code"])
    y = list(df1['decem'])
    plot = plt.bar(np.arange(len(x)), y, color="cyan")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title('Amount of Units sold in December')
    plt.xlabel("Item Code")
    plt.ylabel("No. of Unit Sold in December")
    plt.show()
    return ()


def stocks():
    winsound.Beep(400, 200)
    cursor.execute("select *from stock")
    # filename = "G:\STORE_MANAGEMENT_IN_PYTHON_WITH_SOURCE_CODE\ITEM.csv"
    fig, ax = plt.subplots()
    # df1=pd.read_csv(filename)
    df1 = pd.DataFrame(cursor.fetchall(), columns=['prod_code', "prod_name", 'selling_price', 'cost_price', 'stock'])
    x = list(df1["prod_code"])
    y = list(df1["stock"])
    plot = plt.bar(np.arange(len(x)), y, color="y")
    for idx, rect in enumerate(plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                x[idx],
                ha='center', va='bottom', rotation=90)
    plt.xticks(np.arange(len(x)))
    plt.grid(True)
    plt.title("Stock Left previous Year")
    plt.xlabel('Item Code')
    plt.ylabel('Stock Left')
    plt.show()
    return ()
