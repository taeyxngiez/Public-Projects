# Date: 2022-06-13
# Order items from a bakery and use payment method of choice to pay for the total $

import tkinter as tk
import tkinter.messagebox

class BakeryGUI:
    def __init__(self):

        #The Order Window
        self.order_window = tk.Tk()
        self.order_window.title("Ordering")
        self.order_window.geometry("330x250")

        #Frames in the self.order_window
        self.title1_frame = tk.Frame(self.order_window)
        self.num_frame = tk.Frame(self.order_window)
        self.email_frame = tk.Frame(self.order_window)
        self.empty1_frame = tk.Frame(self.order_window)
        self.title2_frame = tk.Frame(self.order_window)
        self.pastries_frame = tk.Frame(self.order_window)
        self.bread_frame = tk.Frame(self.order_window)
        self.drinks_frame = tk.Frame(self.order_window)
        self.empty2_frame = tk.Frame(self.order_window)
        self.bottom_frame = tk.Frame(self.order_window)

        
        #Create label for user info title 
        self.user_info_label = tk.Label(self.title1_frame, \
                                        text = 'User Info')
        #Create the widgets for the num_frame
        self.num_label = tk.Label(self.num_frame, \
                                  text = 'Number: ')
        self.num_entry = tk.Entry(self.num_frame, \
                                  width = 20)

        #Create the widgets for the email_frame
        self.email_label = tk.Label(self.email_frame, \
                                    text = 'Email : ')
        self.email_entry = tk.Entry(self.email_frame, \
                                    width = 20)
        #Create a empty line. 
        self.empty_label1 = tk.Label(self.empty1_frame, \
                                    text = "")
        self.empty_label2 = tk.Label(self.empty2_frame, \
                                     text='')
        #Create a menu title label. 
        self.menu_label = tk.Label(self.title2_frame, \
                                   text = 'Menu')

        #Create Menu Sublabels
        self.pastries_label = tk.Label(self.pastries_frame, text='Pastries')
        self.bread_label = tk.Label(self.bread_frame, text='Breads')
        self.drinks_label = tk.Label(self.drinks_frame, text='Drinks')

        #Pack the top frame widgets and title labels
        self.user_info_label.pack(side = 'left')
        self.num_label.pack(side = 'left')
        self.num_entry.pack(side='left')
        self.email_label.pack(side = 'left')
        self.email_entry.pack(side='left')
        self.empty_label1.pack()
        self.empty_label2.pack()
        self.menu_label.pack(side = 'left')
        self.pastries_label.pack(side='top')
        self.bread_label.pack(side='top')
        self.drinks_label.pack(side='top')
        

        # Use IntVar objects with the Checkbuttons
        self.crois_var = tk.IntVar()
        self.apple_var = tk.IntVar()
        self.eclair_var = tk.IntVar()
        self.none1_var = tk.IntVar()

        self.foca_var = tk.IntVar()
        self.mutli_var = tk.IntVar()
        self.bag_var = tk.IntVar()
        self.none2_var = tk.IntVar()

        self.esp_var = tk.IntVar()
        self.amer_var = tk.IntVar()
        self.cap_var = tk.IntVar()
        self.none3_var = tk.IntVar()

        #Set the IntVar objects to 0
        self.crois_var.set(0)
        self.apple_var.set(0)
        self.eclair_var.set(0)
        self.none1_var.set(0)

        self.foca_var.set(0)
        self.mutli_var.set(0)
        self.bag_var.set(0)
        self.none2_var.set(0)

        self.esp_var.set(0)
        self.amer_var.set(0)
        self.cap_var.set(0)
        self.none3_var.set(0)

        #create checkbuttons
        self.crois_cb = tk.Checkbutton(self.pastries_frame, text='Croissant', \
                                       variable=self.crois_var)
        self.apple_cb = tk.Checkbutton(self.pastries_frame, text='Apple Pie', \
                                       variable=self.apple_var)
        self.eclair_cb = tk.Checkbutton(self.pastries_frame, text='Eclair     ', \
                                       variable=self.eclair_var)
        self.none1_cb = tk.Checkbutton(self.pastries_frame, text='None     ', \
                                       variable=self.none1_var)

        self.foca_cb = tk.Checkbutton(self.bread_frame, text='Focaccia  ', \
                                       variable=self.foca_var)
        self.mutli_cb = tk.Checkbutton(self.bread_frame, text='Multigrain', \
                                       variable=self.mutli_var)
        self.bag_cb = tk.Checkbutton(self.bread_frame, text='Baguette  ', \
                                       variable=self.bag_var)
        self.none2_cb = tk.Checkbutton(self.bread_frame, text='None      ', \
                                       variable=self.none2_var)

        self.esp_cb = tk.Checkbutton(self.drinks_frame, text='Espresso  ', \
                                       variable=self.esp_var)
        self.amer_cb = tk.Checkbutton(self.drinks_frame, text='Americano', \
                                       variable=self.amer_var)
        self.cap_cb = tk.Checkbutton(self.drinks_frame, text='Cappuccino', \
                                       variable=self.cap_var)
        self.none3_cb = tk.Checkbutton(self.drinks_frame, text='None      ', \
                                       variable=self.none3_var)

        #create ok and quit buttons
        self.quit_button2 = tk.Button(self.bottom_frame, \
                                    text = 'Exit',
                                    command = self.order_window.destroy)
        self.quit_button2.pack(side='right')

        self.ok_button = tk.Button(self.bottom_frame, text='OK', \
                                   command=self.payment_window)
        self.ok_button.pack(side='right')


        #Packing checkbuttons
        self.crois_cb.pack(side='top')
        self.apple_cb.pack(side='top')
        self.eclair_cb.pack(side='top')
        self.none1_cb.pack(side='top')
        self.foca_cb.pack(side='top')
        self.mutli_cb.pack(side='top')
        self.bag_cb.pack(side='top')
        self.none2_cb.pack(side='top')
        self.esp_cb.pack(side='top')
        self.amer_cb.pack(side='top')
        self.cap_cb.pack(side='top')
        self.none3_cb.pack(side='top')
        
        #Pack the frames
        self.title1_frame.pack()
        self.num_frame.pack()
        self.email_frame.pack()
        self.empty1_frame.pack()
        self.title2_frame.pack()
        self.pastries_frame.pack(side='left')
        self.bread_frame.pack(side='left')
        self.drinks_frame.pack(side='left')
        self.empty2_frame.pack()
        self.bottom_frame.pack(side='bottom')

        
        #Start the mainloop
        tk.mainloop()


    #The payment window is the callback function for the ok button
    def payment_window(self):
        
        #Validate phone number
        num_length = len(self.num_entry.get())
        if num_length > 10 or num_length < 10:
            tkinter.messagebox.showinfo("ERROR", "Invalid phone number.")


        self.subtotal = 0.0
        self.total = 0.0

        #Determine are chosen to determine subtotal
        if self.crois_var.get() == 1:
            self.subtotal += 4.00
        if self.apple_var.get() == 1:
            self.subtotal += 5.00
        if self.eclair_var.get() == 1:
            self.subtotal += 4.50
        if self.none1_var.get() == 1:
            self.subtotal += 0.00

        if self.foca_var.get() == 1:
            self.subtotal += 4.00
        if self.mutli_var.get() == 1:
            self.subtotal += 3.00
        if self.bag_var.get() == 1:
            self.subtotal += 3.50
        if self.none2_var.get() == 1:
            self.subtotal += 0.00

        if self.esp_var.get() == 1:
            self.subtotal += 2.00
        if self.amer_var.get() == 1:
            self.subtotal += 3.00
        if self.cap_var.get() == 1:
            self.subtotal += 2.50
        if self.none3_var.get() == 1:
            self.subtotal += 0.00

        #Processing to find total
        self.total = (self.subtotal * 0.13) + self.subtotal


        #Create payment window
        self.pay_window = tk.Tk()
        self.pay_window.title("Payment")
        self.pay_window.geometry("300x300")

        #Create the frames
        self.sub_frame = tk.Frame(self.pay_window)
        self.total_frame = tk.Frame(self.pay_window)
        self.paymethod_frame = tk.Frame(self.pay_window)
        self.bottom_frame = tk.Frame(self.pay_window)

        #Create Labels
        self.sub_label = tk.Label(self.sub_frame, text='Subtotal: ')
        self.price1_label = tk.Label(self.sub_frame, \
                            text=str(format(self.subtotal, '.2f')))

        self.total_label = tk.Label(self.total_frame, text='Total: ')
        self.price2_label = tk.Label(self.total_frame, text=str(format(self.total, '.2f')))

        self.pay_label = tk.Label(self.paymethod_frame, text='Payment Method:')
        

        #Create Radio Buttons for payment method
        self.pay_var = tk.IntVar()        

        self.pay_var.set(1)


        self.debit_rb = tk.Radiobutton(self.paymethod_frame, text='Debit', \
                                       variable=self.pay_var, value=1)
        self.credit_rb = tk.Radiobutton(self.paymethod_frame, text='Credit', \
                                       variable=self.pay_var, value=2)
        self.paypal_rb = tk.Radiobutton(self.paymethod_frame, text='Paypal', \
                                       variable=self.pay_var, value=3)

        
        #Create quit and pay now button
        self.quit_button3 = tk.Button(self.bottom_frame, text='Exit', \
                                      command=self.pay_window.destroy)
        self.paynow_button = tk.Button(self.bottom_frame, text='Pay Now', \
                                       command=self.thanks_message)


        #Packing the widgets and frames
        self.sub_label.pack(side='left')
        self.price1_label.pack(side='left')
        self.total_label.pack(side='left')
        self.price2_label.pack(side='left')
        self.pay_label.pack(side='top')
        self.quit_button3.pack(side='left')
        self.paynow_button.pack(side='left')
        self.debit_rb.pack(side='top')
        self.credit_rb.pack(side='top')
        self.paypal_rb.pack(side='top')

        self.sub_frame.pack()
        self.total_frame.pack()
        self.paymethod_frame.pack()
        self.bottom_frame.pack()
        
        #Start the mainloop
        tk.mainloop()


    #Display message box showing thanks
    def thanks_message(self):
        tk.messagebox.showinfo("Thanks", "Thank you for ordering!")
        
#Create instance for BakeryGUI class
bakery = BakeryGUI()









