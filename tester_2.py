from tkinter import *
from tkinter import messagebox
import mysql.connector
import pandas as pd
from PIL import Image, ImageTk
import requests
from io import BytesIO
#
def load_image():
    url = 'https://www.instagram.com/p/Cw7SsjfRN_d/'
    try:
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((300, 300))  # Resize the image as needed
        img = ImageTk.PhotoImage(img)

        l1.config(image=img)
        l1.image = img  # Keep a reference to prevent garbage collection

    except Exception as e:
        l1.config(text="Error: Unable to load image")
        print(e)

# getting the stock data from database

# connecting to database
try:
    conn = mysql.connector.connect(host="localhost",
                                   user="ROOT".lower(),
                                   password="",
                                   database="rkpatel")
    print('database connected'.upper())
    cursor = conn.cursor()
except Exception as e:
    a = messagebox.showerror('error'.upper(), 'DATABASE not connected'.upper())
    # print('not connected'.upper())
    print(e)
    exit()
    pass
if conn.is_connected():
    # database file into dataframes
    cursor.execute('select * from stock')
    data = pd.DataFrame(cursor.fetchall(), columns=['prod_code', 'prod_name', 'selling_price', 'cost_price', 'stock'])
    print(data)

root = Tk()
root.state('zoomed')
root.title('welcome to r. k. patel and comapany'.title())
root.configure(background='#000000')

frame = Frame(root,background='#A9A9A9')
frame.pack(fill=X,padx=10,pady=5)

l1=Label(frame,text='rohit')
l1.pack(padx=10)

Button(frame,text='load',command=load_image).pack()

root.mainloop()
