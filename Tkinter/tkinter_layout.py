import tkinter as  tk
from datetime import datetime as dt

def button_onclick():
    print(f'Just got clicked at time : {dt.now()}')
    new_text = input.get()
    mylabel.config(text = new_text)


window = tk.Tk()
window.title('Tkinter')
window.minsize(width= 500,height =300)

#label
mylabel = tk.Label(text='Iam a label',font = ('Futura',24,'bold'))
mylabel.config(text = 'Reday for new')
mylabel.grid(column=1,row=1)

#button
button = tk.Button(text = 'enter',command = button_onclick)
#button.pack()

#Pack are really dificult to position at certain area 
#  use PLACE

button.place(x=40,y= 50)
#button.grid(column=1,row=2) 
#DOWNSIDE OF PLAC
#some time it also becomes hard to give coordinates to all 

#Entry
input = tk.Entry(width=23)

#input.pack()

# theiri s another one that is GRID

input.grid(column=2,row=3)
# padding for a specific  label
# input.config(padx=20,pady=20)

#PADDING IN WINDOW  
# WILL GIVE MORE SPACE BETWEEN PROGRAM
window.config(padx=20,pady=20)  # padd to whole window
# remember grid can't be used with pack so dont mix them
window.mainloop()