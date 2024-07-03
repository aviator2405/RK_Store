import tkinter as tk
from tkinter import messagebox, Menu, Entry, Label
import mysql.connector
import winsound
import os

class AmazonClone(tk.Tk):
    def __init__(self,username):
        super().__init__()
        self.title("WELCOME TO RK PATEL AND COMAPANY")
        self.geometry("800x600")

        self.username = username  # Get the username of the currently logged-in user

        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "rkpatel",
        }

        self.user_data = self.fetch_user_data()

        self.products = self.fetch_products_from_db()
        self.cart = []

        self.create_widgets()
        self.create_menu()

        # Review page variables
        self.review_frame = None
        self.review_listbox = None
        self.address_entry = None
        self.phone_entry = None

    def fetch_user_data(self):
        user_data = {}
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor(dictionary=True)
            query = f"SELECT name, address, phone FROM users WHERE username = '{self.username}'"
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                user_data = result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        return user_data

    def fetch_products_from_db(self):
        # Replace with your MySQL database connection details
        global connection
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "rkpatel",
        }

        products = []
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM stock")  # Use "stock" as the table name
            products = cursor.fetchall()
            return products
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def create_widgets(self):
        # Product list frame
        self.product_frame = tk.Frame(self)
        self.product_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

        product_label = tk.Label(self.product_frame, text="Products")
        product_label.pack()

        self.product_listbox = tk.Listbox(self.product_frame, selectmode=tk.SINGLE, width=40, height=15,
                                          background='red', borderwidth=2, relief=tk.RAISED)
        self.product_listbox.pack(fill=tk.BOTH, expand=True)

        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product['prod_name']} - Rs. {product['selling_price']:.2f}")

        add_to_cart_button = tk.Button(self.product_frame, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack()

        checkout_button = tk.Button(self.product_frame, text="Checkout", command=self.show_review_page)
        checkout_button.pack()

    def viewcart(self):
        winsound.Beep(400, 200)
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Add some items before checking out.")
        else:
            new = tk.Tk()
            self.review_frame = tk.Frame(new)
            self.review_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

            review_label = tk.Label(self.review_frame, text="Review Cart")
            review_label.pack()

            self.review_listbox = tk.Listbox(self.review_frame, selectmode=tk.SINGLE, width=40, height=15)
            self.review_listbox.pack(fill=tk.BOTH, expand=True)
            for product in self.cart:
                self.review_listbox.insert(tk.END, f"{product['prod_name']} - Rs. {product['selling_price']:.2f}")

            address_label = Label(self.review_frame, text="Shipping Address:")
            address_label.pack()
            self.address_entry = Entry(self.review_frame)
            self.address_entry.pack()

            phone_label = Label(self.review_frame, text="Phone Number:")
            phone_label.pack()
            self.phone_entry = Entry(self.review_frame)
            self.phone_entry.pack()

            delete_button = tk.Button(self.review_frame, text="Delete Item", command=self.delete_item)
            delete_button.pack()
            new.mainloop()

    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        cart_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Cart", menu=cart_menu)
        cart_menu.add_command(label="View Cart", command=self.viewcart)
        cart_menu.add_separator()
        cart_menu.add_command(label="Clear Cart", command=self.clear_cart)

    def add_to_cart(self):
        winsound.Beep(400, 200)
        selected_index = self.product_listbox.curselection()
        if selected_index:
            product_index = selected_index[0]
            product = self.products[product_index]
            self.cart.append(product)
            messagebox.showinfo("Added to Cart", f"{product['prod_name']} has been added to your cart.")

    def show_review_page(self):
        winsound.Beep(400, 200)
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Add some items before checking out.")
        else:
            if self.review_frame:
                self.review_frame.destroy()
            self.review_frame = tk.Frame(self)
            self.review_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

            review_label = tk.Label(self.review_frame, text="Review Cart")
            review_label.pack()

            self.review_listbox = tk.Listbox(self.review_frame, selectmode=tk.SINGLE, width=40, height=15)
            self.review_listbox.pack(fill=tk.BOTH, expand=True)
            for product in self.cart:
                self.review_listbox.insert(tk.END, f"{product['prod_name']} - Rs. {product['selling_price']:.2f}")

            address_label = Label(self.review_frame, text="Shipping Address:")
            address_label.pack()
            avar = tk.StringVar()
            avar.set(self.user_data.address)
            self.address_entry = Entry(self.review_frame,textvariable=avar)
            self.address_entry.pack()

            phone_label = Label(self.review_frame, text="Phone Number:")
            phone_label.pack()
            pvar = tk.StringVar()
            pvar.set(self.user_data.phone)
            self.phone_entry = Entry(self.review_frame,textvariable=pvar)
            self.phone_entry.pack()

            checkout_button = tk.Button(self.review_frame, text="Final Checkout", command=self.final_checkout)
            checkout_button.pack()

            delete_button = tk.Button(self.review_frame, text="Delete Item", command=self.delete_item)
            delete_button.pack()

            back_button = tk.Button(self.review_frame, text="Back to Products", command=self.back_to_products)
            back_button.pack()

            self.product_frame.pack_forget()

    def final_checkout(self):
        winsound.Beep(400, 200)
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Add some items before checking out.")
        else:
            total_price = sum(float(product["selling_price"]) for product in self.cart)
            address = self.address_entry.get()
            phone = self.phone_entry.get()
            order_summary = f"Total Price: Rs.{total_price:.2f}\n"
            order_summary += f"Shipping Address: {address}\n"
            order_summary += f"Phone Number: {phone}\n\n"
            order_summary += "Thank you for shopping with us!"
            messagebox.showinfo("Final Checkout", order_summary)
            self.cart = []
            self.review_frame.destroy()
            self.create_widgets()

    def delete_item(self):
        winsound.Beep(400, 200)
        selected_index = self.review_listbox.curselection()
        if selected_index:
            item_index = selected_index[0]
            del self.cart[item_index]
            self.review_listbox.delete(item_index)

    def back_to_products(self):
        winsound.Beep(400, 200)
        self.review_frame.destroy()
        self.create_widgets()

    def clear_cart(self):
        winsound.Beep(400, 200)
        self.cart = []

if __name__ == "__main__":
    app = AmazonClone('rohit')
    app.mainloop()
