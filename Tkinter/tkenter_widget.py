import tkinter as tk
window = tk.Tk()

window.title('tkinter widgets')

# Setting the default size of window
window.minsize(width = 500, height = 400)

#label
label1 = tk.Label(text='Widgets',font = ('Arial',12))
label1.pack()



# Entry
input1 = tk.Entry(width=30)
input1.pack()

#button
button1 =tk.Button(text = 'click me')
button1.pack()


#Entries
entry = tk.Entry(width = 30)
#Add some text
entry.insert(tk.END,string='some text')
# Gets text in entry
print(entry.get())
entry.pack()

#Text
text =tk.Text(height =5,width =30)
#puts cursor on text box
text.focus()

#Adds some text to begin with
text.insert(tk.END,"Example of multi-line text entry.")


# Get's current value in textbox at line 1, character 0
print(text.get('1.0',tk.END))

# '1.0' starting form line1 and character 0
# tk.END means index at end
 
#spinbox

def spinbox_use():
    #get current value of spinbox
    print(spinbox.get())


# creating a spinbox
spinbox = tk.Spinbox(from_= 100, to= 111, width = 5,command = spinbox_use)
spinbox.pack()



#SCALE
# Called with current scale value.

def scale_used(value):
    print(value)
scale = tk.Scale(from_=100,to =120,command= scale_used)
scale.pack()


#CHECK BUTTON
def check():
    #Prints 1 if button checked else 0
    print(check_state.get())

#creatin variable to hold on to check_state, 0 is off, 1 is on

check_state = tk.IntVar()  # this is the tinkter class type
# and will help in keepcheck of that value
checkbutton = tk.Checkbutton(text =  'Is On?', variable = check_state,
                           command= check)
check_state.get()
checkbutton.pack()



#RADIO BUTTON
def radio():
    print(radio_state.get())

radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text = 'Option1',value =1,variable = radio_state,command = radio)

radiobutton2  = tk.Radiobutton(text ='Option2',value = 2,variable = radio_state,command = radio)
radiobutton1.pack()
radiobutton2.pack()




#List Box 
def listbox_used(event):
    #Get current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height = 5)
fruits = ['Apple','Pearl','Orange','Mango','Papaya','Banana','Guvava','strawberry']

for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind('<<ListboxSelect>>',listbox_used)
listbox.pack()




window.mainloop()