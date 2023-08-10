import tkinter as tk

window = tk.Tk()

window.minsize(height=200,width=400)

#title
window.title("Mile to Km Converter")
# change bg color
new_color = "#FDFDFD"  # Replace this with the color code of your choice
window.config(bg=new_color)


# function
def Calculator():
    mile = input1.get()   
    km = int(mile)*1.609
    newkm= f'{km}'
    label.config(text = newkm)


#entry <Mile>
input1 = tk.Entry(width = 15)
input1.insert(tk.END,string=0)
input1.grid(column = 2 ,row=1)

#label
label1 = tk.Label(text = 'Mile',font=('Arial',15))
label1.grid(column=3,row=1)

#label
label2 = tk.Label(text = 'is equal to ',font=('Futura',15,'bold'))
label2.grid(column=1,row=2)

# #entry <Km>
# input2 = tk.Entry(width=15)
# input2.insert(tk.END,string=0)
# input2.grid(column = 2,row = 3)


#label
label = tk.Label(text = '0',font=('Arial',15))
label.grid(column=2,row=3)

#label
label3 = tk.Label(text = 'Km ',font=('Arial',15))
label3.grid(column=3,row=3)

#button
button1 = tk.Button(text = 'Calculate',command = Calculator)
button1.grid(column = 3 , row =4)


window.config(padx=10,pady=20)
window.mainloop()

