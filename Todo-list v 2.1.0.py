#Initialization
todo = []
checklists = []
from tkinter import *
import customtkinter

#GUI

#Setting theme and coloUr options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#Yes, i took this from the doccumentation >:)

#GUI INITIALIZATION
app = customtkinter.CTk()

app.title('WOW VERY GOOD AND RELIABLE TODO LIST W.V.G.A.R.T.L') #app title
app.geometry('600x600') #window size

#Function to add stuff into the list
def addthing(event):
  newtext = Enterbox.get() #Gets text from the box
  todo.append(newtext)
  Enterbox.delete(0, 'end') #Deletes the text inside of enterbox after pressing enter
  newcheckbox = customtkinter.CTkCheckBox(checkboxframe, text=newtext, command=lambda: clearcheckboxwhentickedcommand(newcheckbox, newtext))#Makes new checkbox
  checklists.append(newcheckbox)
  newcheckbox.pack(padx=10, pady=5, anchor=W) #Adds new checkbox

#function for the clearbutton thing
def clearlistbuttoncommand():
  todo.clear()
  checklists.clear()
  #Destroys checkboxes
  for widget in checkboxframe.winfo_children():
    widget.destroy()

#Clear list button code
clearlistbutton = customtkinter.CTkButton(app, text="Clear all", command=clearlistbuttoncommand)
clearlistbutton.grid(row=1, column=1, padx=10, pady=10)

#function to make the checkbox delete itself when ticked
def clearcheckboxwhentickedcommand(newcheckbox, newtext):
  checklists.remove(newcheckbox)
  newcheckbox.destroy()
  todo.remove(newtext)

#Frame for the checkboxes
checkboxframe = customtkinter.CTkFrame(app)
checkboxframe.grid(row=0, column=0, columnspan=2, padx=10, sticky=NSEW)

#Enterbox code
Enterbox = customtkinter.CTkEntry(app, placeholder_text="Enter items here: ")
Enterbox.bind("<Return>", addthing) #Binds the enter key to the addthing function
Enterbox.grid(row=1, column=0, columnspan=1, padx=10, sticky=EW)

# Make the grid cell expandable
app.grid_rowconfigure(0, weight=1)  # Textbox row gets extra space
app.grid_rowconfigure(1, weight=0)  # Entry box stays fixed
app.grid_columnconfigure(0, weight=1)

app.mainloop()