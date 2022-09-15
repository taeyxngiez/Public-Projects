import tkinter

#create class
class PropertyTaxGUI:
    
    def __init__(self):

        #create the window
        self.main_window = tkinter.Tk()

        self.property_frame = tkinter.Frame(self.main_window)
        self.value_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)



        self.property_label = tkinter.Label(self.property_frame, \
                                            text='Enter the property value: $')
        self.property_entry = tkinter.Entry(self.property_frame, \
                                            width=10)

        self.property_label.pack(side='left')
        self.property_entry.pack(side='left')


        self.assessmentval_label = tkinter.Label(self.value_frame, \
                                                 text='Assessment Value:')
        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.value_frame, \
                                         textvariable=self.value)


        self.propertytax_label = tkinter.Label(self.tax_frame, \
                                               text='Property Tax:')
        self.tax = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.tax_frame, \
                                       textvariable=self.tax)

        self.assessmentval_label.pack(side='left')
        self.propertytax_label.pack(side='left')
        self.value_label.pack(side='left')
        self.tax_label.pack(side='left')


        self.cal_button = tkinter.Button(self.bottom_frame, \
                                         text='Calculate', \
                                         command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)

        self.cal_button.pack(side='left')
        self.quit_button.pack(side='left')



        self.property_frame.pack()
        self.value_frame.pack()
        self.tax_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    #create the functions for the calculations
    def calculate(self):
        self.property = float(self.property_entry.get())
        self.assessmentval = format(self.property*0.6, '.2f')
        self.propertytax = format(float(self.assessmentval)*0.0064, '.2f')
        self.value.set('$' + self.assessmentval)
        self.tax.set('$' + self.propertytax)


#create the instance
conv = PropertyTaxGUI()

