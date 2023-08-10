import tkinter

window = tkinter.Tk()

#setting the title
window.title('My First GUI program')

# Setting the default size of window
window.minsize(width = 500, height = 400)

# Creating a label
mylabel = tkinter.Label(text = 'Greetings',font = ('Arial',32,'italic'))
mylabel.pack()# this will pack it at center as default on screen

mylabel2 = tkinter.Label(text= 'Hi')
mylabel2.pack(side = 'left')  # or bottom,top etc
mylabel2['text'] = 'Jai Siya Ram'

# we can also do this
mylabel2.config(text = 'newly typed ')
#Buttons
def button_clicks():
    print("Wait gor a moment")
button = tkinter.Button(text='click_on',command = button_clicks)
button.pack()



# now lets combine entry with button
def button_get():
    new = input.get()
    mylabel2.config(text = new)

button2 = tkinter.Button(text = 'click it',command=button_get)
button2.pack()


 #Entry
input = tkinter.Entry(width = 40) # width gives the size of entry 
input.pack()
print(input.get())
#print(input.get()) # this will provide whatever sent into that box




# this will make sure to keep window running and listen the user cmd
# this must be at hte end
window.mainloop() 