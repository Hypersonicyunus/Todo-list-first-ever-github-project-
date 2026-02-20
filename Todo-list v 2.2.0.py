#Initialization
todocheckboxes = []
completedcheckboxes = []
from tkinter import *
import customtkinter
from PIL import Image

#GUI

#Setting theme and coloUr options
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#Yes, i took this from the doccumentation >:)

#GUI INITIALIZATION
app = customtkinter.CTk()


app.title('SimpleTodo') #app title
app.geometry('600x600') #window size

#Function to add stuff into the list
def addthing(event):
  newtext = Enterbox.get() #Gets text from the box
  if newtext == "":
    return
  Enterbox.delete(0, 'end') #Deletes the text inside of enterbox after pressing enter
  todo_checkbox = customtkinter.CTkCheckBox(todocheckboxframe, text=newtext, command=lambda: movecheckboxtocompletedcommand(todo_checkbox, newtext))#Makes new checkbox
  todocheckboxes.append(todo_checkbox)
  todo_checkbox.pack(padx=10, pady=10, anchor=W) #Adds new checkbox

#function for the clearbutton thing
def clearlistbuttoncommand():
  todocheckboxes.clear()
  completedcheckboxes.clear()
  #Destroys checkboxes
  for widget in todocheckboxframe.winfo_children():
    if isinstance(widget, customtkinter.CTkCheckBox): #Checks if the widgets are checkboxes
      widget.destroy() #destroys them

  for widget in completedcheckboxframe.winfo_children():
    if isinstance(widget, customtkinter.CTkCheckBox): #Checks if the widgets are checkboxes
      widget.destroy() #destroys them
    
#Code for creating the clearlist button
clearlistbutton = customtkinter.CTkButton(app, text="Clear all", command=clearlistbuttoncommand)
clearlistbutton.grid(row=2, column=1, padx=10, pady=10)



#function to make the checkbox move to the completed frame when ticked
def movecheckboxtocompletedcommand(todo_checkbox, newtext):
  todocheckboxes.remove(todo_checkbox)
  todo_checkbox.destroy()
  #Code to move the completed checkbox to the completed checkbox section
  completedcheckbox = customtkinter.CTkCheckBox(completedcheckboxframe, text= newtext, command= lambda: movecheckboxtoTodocommand(completedcheckbox, newtext))
  completedcheckboxes.append(completedcheckbox)
  completedcheckbox.pack(padx=10, pady=10, anchor=W)
  completedcheckbox.select()

#function to move the completed checkbox back to todo frame when unticked
def movecheckboxtoTodocommand(completedcheckbox, newtext):
  completedcheckboxes.remove(completedcheckbox)
  completedcheckbox.destroy()
  new_todo_checkbox = customtkinter.CTkCheckBox(todocheckboxframe, text= newtext, command= lambda: movecheckboxtocompletedcommand(new_todo_checkbox, newtext))
  new_todo_checkbox.pack(padx=10, pady=10, anchor=W)
  todocheckboxes.append(new_todo_checkbox)

#Frame for the todocheckboxes
todocheckboxframe = customtkinter.CTkScrollableFrame(app)
todocheckboxframe.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)

#Label for the todocheckbox
checkboxframelabel = customtkinter.CTkLabel(todocheckboxframe, text="To do")
checkboxframelabel.pack(pady=5)

#Frame for the completed checkboxes
completedcheckboxframe = customtkinter.CTkScrollableFrame(app)
completedcheckboxframe.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)

#Label for the completed checkbox frame
completedcheckboxframelabel= customtkinter.CTkLabel(completedcheckboxframe, text="Completed")
completedcheckboxframelabel.pack(pady=5)

#Enterbox code
Enterbox = customtkinter.CTkEntry(app, placeholder_text="Enter items here: ")
Enterbox.bind("<Return>", addthing) #Binds the enter key to the addthing function
Enterbox.grid(row=2, column=0, columnspan=1, padx=10, sticky=EW)

# Make the grid cell expandable
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1) 
app.grid_columnconfigure(0, weight=1)

app.mainloop()