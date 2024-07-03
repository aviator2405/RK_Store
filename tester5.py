import tkinter as tk
from tkinter import messagebox, Menu, Entry, Label
import mysql.connector
import pandas as pd
import winsound


class AmazonClone(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.title("WELCOME TO RK PATEL AND COMAPANY")
        self.geometry("800x600")

        self.username = username
        self.user_data = self.fetch_user_data()

        self.products = self.fetch_products_from_db()
        self.cart = []
        self.quantity = None  # Instance variable to store quantity

        self.create_widgets()
        self.create_menu()

        # Review page variables
        self.review_frame = None
        self.review_listbox = None
        self.address_entry = None
        self.phone_entry = None

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

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        return products

    def fetch_user_data(self):
        global connection
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "rkpatel",
        }

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)
            query = f"SELECT * FROM per_info WHERE username = '{self.username}'"
            cursor.execute(query)
            result = pd.DataFrame(cursor.fetchall(), columns=['username', 'name', 'address', 'phone'])

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        return result

    def create_widgets(self):
        # Product list frame
        self.product_frame = tk.Frame(self)
        self.product_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
        wellabel = Label(self.product_frame, text=f'Welcome {self.user_data.iloc[0].username}', font='algerian 20 bold')
        wellabel.pack()

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
                self.review_listbox.insert(tk.END,
                                           f"{product['prod_name']} - Rs. {product['selling_price']:.2f} - Quantity: {product['quantity']}")

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
            quanwin = tk.Tk()
            tk.Label(quanwin, text="ENTER QUANTITY").pack(side=tk.LEFT)
            quantity_entry = tk.Entry(quanwin)
            quantity_entry.pack(side=tk.LEFT)
            submit_button = tk.Button(quanwin, text='SUBMIT', font="arial 15 bold",
                                      command=lambda: self.set_quantity(quantity_entry.get(), quanwin))
            submit_button.pack(side=tk.BOTTOM)
            quanwin.mainloop()

    def set_quantity(self, quantity, quanwin):
        if quantity.isdigit() and int(quantity) > 0:
            self.quantity = int(quantity)
            quanwin.destroy()
            self.process_add_to_cart()
        else:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")

    def process_add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            product_index = selected_index[0]
            product = self.products[product_index]

            product_with_quantity = {
                'prod_name': product['prod_name'],
                'selling_price': product['selling_price'],
                'quantity': self.quantity
            }
            self.cart.append(product_with_quantity)

            messagebox.showinfo("Added to Cart", f"{self.quantity} {product['prod_name']} has been added to your cart.")

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
                self.review_listbox.insert(tk.END,
                                           f"{product['prod_name']} - Rs. {product['selling_price']:.2f} - Quantity: {product['quantity']}")

            # Entry fields for address and phone
            address_label = Label(self.review_frame, text="Shipping Address:")
            address_label.pack()
            avar = tk.StringVar()
            # print(self.user_data.iloc[0].address)
            avar.set(f'{self.user_data.iloc[0].address}')
            self.address_entry = Entry(self.review_frame, textvariable=avar)
            self.address_entry.pack()
            phone_label = Label(self.review_frame, text="Phone Number:")
            phone_label.pack()
            pvar = tk.StringVar()
            pvar.set(self.user_data.iloc[0].phone)
            self.phone_entry = Entry(self.review_frame, textvariable=pvar)
            self.phone_entry.pack()

            # Buttons on the review page
            checkout_button = tk.Button(self.review_frame, text="Final Checkout", command=self.final_checkout)
            checkout_button.pack()

            delete_button = tk.Button(self.review_frame, text="Delete Item", command=self.delete_item)
            delete_button.pack()

            back_button = tk.Button(self.review_frame, text="Back to Products", command=self.back_to_products)
            back_button.pack()

            # Hide the product frame
            self.product_frame.pack_forget()

    def final_checkout(self):
        winsound.Beep(400, 200)
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Add some items before checking out.")
        else:
            total_price = sum(float((product["selling_price"]*product['quantity'])) for product in self.cart)
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
    username = "rohit"  # Replace with the actual username
    app = AmazonClone(username)
    app.mainloop()
