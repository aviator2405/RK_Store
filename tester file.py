# OM GANESHAY NAMAH
# MAIN GUI INTERFACE

from tkinter import *
from tkinter import messagebox
import winsound
from database_manager_program import *
from admin_window import *


def call_check_cred(useless=0):
    winsound.Beep(400, 200)
    r = username.get()
    if check_cred(username.get(), password.get()):
        # TO CLOSE THE PREVIOUS WINDOWS
        root.destroy()
        # ADMIN WINDOW
        if r == 'admin':

            adminWin = Tk()
            adminWin.title("ADMIN WINDOW")
            adminWin.state('zoomed')
            adminWin.geometry("1080x1080")
            def call_stock_update():

                result = stock_update(prod_code.get(), prod_name.get(), selling_price.get(), cost_price.get(),
                                      stock.get())
                if result == 'e1':
                    a = messagebox.showinfo('ERROR MESSAGE',
                                            'SELLING PRICE IS LESS THAN COST PRICE. ITS A LOSS-MAKING DEAL')
                elif result == 'e2':
                    a = messagebox.showinfo('ERROR MESSAGE', 'PRODUCT CODE MATCHES WITH OTHER PRODUCT_CODE')
                else:
                    a = messagebox.showinfo('ERROR MESSAGE', 'PRODUCT ENTERED IN THE DATABASE SUCCESSFULLY')

            frame1 = Frame(adminWin, bg="red", borderwidth=6, relief=RAISED)
            frame1.pack(side=LEFT, fill='y')

            ps = Label(text='WELCOME TO R.K. PATEL AND COMAPANY ADMIN WINDOW')
            ps.pack()

            jan = Label(text='', cursor='hand2')

            feb = Label(text='', cursor='hand2')

            mar = Label(text='', cursor='hand2')

            apr = Label(text='', cursor='hand2')

            may = Label(text='', cursor='hand2')

            jun = Label(text='', cursor='hand2')

            jul = Label(text='', cursor='hand2')

            aug = Label(text='', cursor='hand2')

            sept = Label(text='', cursor='hand2')

            oct = Label(text='', cursor='hand2')

            nov = Label(text='', cursor='hand2')

            decem = Label(text='', cursor='hand2')

            overal = Label(text='', cursor='hand2')

            pcl = Label(text="product code")

            pcval = StringVar()
            prod_code = Entry(textvariable=pcval)


            pnl = Label( text="product Name")

            pnval = StringVar()
            prod_name = Entry(textvariable=pnval)


            spl = Label(text="selling Price")

            spval = IntVar()
            selling_price = Entry(textvariable=spval)


            cpl = Label(text="cost Price")

            cpval = IntVar()
            cost_price = Entry(textvariable=cpval)


            sl = Label(text="stock")

            sval = IntVar()
            stock = Entry(textvariable=sval)
            

            entrysubmittbutton=Button(text="Submit Entry",command=call_stock_update)
            pcl.pack(anchor='nw')
            prod_code.pack(anchor='nw')
            pnl.pack(anchor='nw')
            prod_name.pack(anchor='nw')
            spl.pack(anchor='nw')
            selling_price.pack(anchor='nw')
            cpl.pack(anchor='nw')
            cost_price.pack(anchor='nw')
            sl.pack(anchor='nw')
            stock.pack(anchor='nw')
            entrysubmittbutton.pack(anchor='nw')

            # janp = Label(frame2,text='')
            # janp.pack()

            # febp = Label(frame2,text='')
            # febp.pack()

            # marp = Label(frame2,text='')
            # marp.pack()

            # aprp = Label(text='')
            # aprp.pack()

            # mayp = Label(frame2,text='')
            # mayp.pack()

            # junp = Label(frame2,text='')
            # junp.pack()

            # julp = Label(frame2,text='')
            # julp.pack()

            # augp = Label(frame2,text='')
            # augp.pack()

            # septp = Label(frame2,text='')
            # septp.pack()

            # octp = Label(frame2,text='')
            # octp.pack()

            # novp = Label(frame2,text='')
            # novp.pack()

            # decemp = Label(frame2,text='')
            # decemp.pack()

            # overalp = Label(adminWin,)
            # overalp.pack()

            # new entry
            new = True

            def call_sales():
                winsound.Beep(400, 200)
                ps.config(text='SALES')

                pcl.destroy()
                prod_code.destroy()
                pnl.destroy()
                prod_name.destroy()
                spl.destroy()
                selling_price.destroy()
                cpl.destroy()
                cost_price.destroy()
                sl.destroy()
                stock.destroy()
                entrysubmittbutton.destroy()

                jan.pack(anchor='nw')
                feb.pack(anchor='nw')
                mar.pack(anchor='nw')
                apr.pack(anchor='nw')
                may.pack(anchor='nw')
                jun.pack(anchor='nw')
                jul.pack(anchor='nw')
                aug.pack(anchor='nw')
                sept.pack(anchor='nw')
                oct.pack(anchor='nw')
                nov.pack(anchor='nw')
                decem.pack(anchor='nw')
                overal.pack(anchor='nw')


                jan.config(text='JANUARY')
                jan.bind('<Button-1>', sales_jan)

                feb.config(text='FEBRUARY')
                feb.bind('<Button-1>', sales_feb)

                mar.config(text='MARCH')
                mar.bind('<Button-1>', sales_mar)

                apr.config(text='APRIL')
                apr.bind('<Button-1>', sales_apr)

                may.config(text='MAY')
                may.bind('<Button-1>', sales_may)

                jun.config(text='JUNE')
                jun.bind('<Button-1>', sales_jun)

                jul.config(text='JULY')
                jul.bind('<Button-1>', sales_jul)

                aug.config(text='AUGUST')
                aug.bind('<Button-1>', sales_aug)

                sept.config(text='SEPTEMBER')
                sept.bind('<Button-1>', sales_sept)

                oct.config(text='OCTOBER')
                oct.bind('<Button-1>', sales_oct)

                nov.config(text='NOVEMBER')
                nov.bind('<Button-1>', sales_nov)

                decem.config(text='DECEMBER')
                decem.bind('<Button-1>', sales_decem)

                overal.config(text='OVERALL')
                overal.bind("<Button-1>", sales)

            def call_profit():
                winsound.Beep(400, 200)

                ps.config(text='PROFIT')

                pcl.destroy()
                prod_code.destroy()
                pnl.destroy()
                prod_name.destroy()
                spl.destroy()
                selling_price.destroy()
                cpl.destroy()
                cost_price.destroy()
                sl.destroy()
                stock.destroy()
                entrysubmittbutton.destroy()

                jan.pack(anchor='nw')
                feb.pack(anchor='nw')
                mar.pack(anchor='nw')
                apr.pack(anchor='nw')
                may.pack(anchor='nw')
                jun.pack(anchor='nw')
                jul.pack(anchor='nw')
                aug.pack(anchor='nw')
                sept.pack(anchor='nw')
                oct.pack(anchor='nw')
                nov.pack(anchor='nw')
                decem.pack(anchor='nw')
                overal.pack(anchor='nw')

                jan.config(text='JANUARY')
                jan.bind('<Button-1>', total_profit_jan)

                feb.config(text='FEBRUARY')
                feb.bind('<Button-1>', total_profit_feb)

                mar.config(text='MARCH')
                mar.bind('<Button-1>', total_profit_mar)

                apr.config(text='APRIL')
                apr.bind('<Button-1>', total_profit_apr)

                may.config(text='MAY')
                may.bind('<Button-1>', total_profit_may)

                jun.config(text='JUNE')
                jun.bind('<Button-1>', total_profit_jun)

                jul.config(text='JULY')
                jul.bind('<Button-1>', total_profit_jul)

                aug.config(text='AUGUST')
                aug.bind('<Button-1>', total_profit_aug)

                sept.config(text='SEPTEMBER')
                sept.bind('<Button-1>', total_profit_sept)

                oct.config(text='OCTOBER')
                oct.bind('<Button-1>', total_profit_oct)

                nov.config(text='NOVEMBER')
                nov.bind('<Button-1>', total_profit_nov)

                decem.config(text='DECEMBER')
                decem.bind('<Button-1>', total_profit_decem)

                # photo = PhotoImage(file="HELLO.png")
                overal.config(text="OVERALL")
                overal.bind("<Button-1>", profit)



            def show_entry():
                jan.destroy()
                feb.destroy()
                mar.destroy()
                apr.destroy()
                may.destroy()
                jun.destroy()
                jul.destroy()
                aug.destroy()
                sept.destroy()
                oct.destroy()
                nov.destroy()
                decem.destroy()
                overal.destroy()

                ps.config(text='new entry   ')
                pcl.pack(anchor='nw')
                prod_code.pack(anchor='nw')
                pnl.pack(anchor='nw')
                prod_name.pack(anchor='nw')
                spl.pack(anchor='nw')
                selling_price.pack(anchor='nw')
                cpl.pack(anchor='nw')
                cost_price.pack(anchor='nw')
                sl.pack(anchor='nw')
                stock.pack(anchor='nw')
                entrysubmittbutton.pack(anchor='nw')

            Button(frame1, text='show profit', command=call_profit).pack(padx=66, pady=100)
            Button(frame1, text="Show sales", command=call_sales).pack(padx=66, pady=100)
            Button(frame1, text="Show Stock", command=stocks).pack(padx=66, pady=100)
            Button(frame1, text='Stock Entry', command=show_entry).pack(padx=66, pady=10)
            adminWin.mainloop()
        else:
            # CUSTOMER WINDOW
            genWin = Tk()
            genWin.geometry("1080x1080")
            genWin.title("WELCOME TO R.K. PATEL AND COMPANY")
            genWin.state('zoomed')
            genWin.mainloop()

    else:
        a = messagebox.showinfo('ERROR MESSAGE', 'INVALID,BAD CREDENTIALS')


def call_newlogin():
    def call_func():
        if new_login_cred(usern.get(), passwor.get()):
            new_login_per(usern.get(), cname.get(), address.get(), pnum.get())
            a = messagebox.showinfo("INFORMATION MESSAGE", "YOU HAVE SUCCESSFULLY CREATED YOUR ACCOUNT !!")
            window.destroy()
        else:
            a = messagebox.showinfo("INFORMATION MESSAGE", "THIS USERNAME HAS ALREADY TAKEN")

    window = Tk()
    window.state("zoomed")
    window.geometry("666x666")

    user = StringVar()
    passw = StringVar()
    name = StringVar()
    add = StringVar()
    num = IntVar()

    Label(window, text='NEW USER LOGIN DETAILS PAGE', font="arial 24 bold").pack(pady=90)

    Label(window, text='ENTER YOUR USER_ID OF YOUR CHOICE').pack()

    usern = Entry(window, textvariable=user)
    usern.pack()

    Label(window, text="ENTER YOUR PASSWORD").pack()

    passwor = Entry(window, textvariable=passw, show='$')
    passwor.pack()

    Label(window, text='ENTER YOUR NAME ').pack()

    cname = Entry(window, textvariable=name)
    cname.pack()

    Label(window, text='ENTER YOUR ADDRESS ').pack()

    address = Entry(window, textvariable=add)
    address.pack()

    Label(window, text='ENTER YOUR PHONE NUMBER ').pack()

    pnum = Entry(window, textvariable=num)
    pnum.pack()

    Button(window, text="Submit Details", command=call_func).pack()

    window.mainloop()


root = Tk()
root.state("zoomed")
root.title("RK PATEL AND COMAPANY STOCK MANAGEMENT SYSTEM")
root.geometry("666x666")
root.minsize(width=666, height=666)

# HEADING LABEL
label = Label(root, text="RK PATEL AND COMAPANY\nSTOCK MANAGEMNET SYSTEM", font="arial 20 bold italic", fg='blue')
label.pack(pady=40)

# LOGIN PAGE LABEL
loginlabel = Label(root, text="LOGIN PAGE", font="algerian 16 italic", fg='blue')
loginlabel.pack()

# STRING VARIABLES FOR USERNAME AND PASSWORD
userval = StringVar()
passval = StringVar()

# CREDENTIAL FIELDS
user_label = Label(root, text="ENTER USERNAME")
pass_label = Label(root, text="ENTER password")
username = Entry(textvariable=userval)
password = Entry(textvariable=passval, show="*")
subButton = Button(text="SUBMIT", command=call_check_cred, cursor='hand2')
password.bind("<Return>", call_check_cred)

# PACKING CREDENTIAL FIELDS
user_label.pack()
username.pack()
pass_label.pack()
password.pack()
subButton.pack()
Label(text='').pack()
Button(text="NEW LOGIN ?", command=call_newlogin).pack()

root.mainloop()
