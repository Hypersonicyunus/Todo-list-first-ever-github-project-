#Initialization
todo = []
exit = False

#Guide

print("To get started, type anything and press enter to add it into the list. If you ever need a list of commands, type !help and enter it.")

#Commands

#display_help function
def display_help():
    print("Here are a list of commands: !help !clear")

#clear_function
def clear_todo():
    todo.clear()
    print("To Do list cleared!")

#Delete_todo function
def delete_todo():
  itemremove = int(input("What item would you like to be removed? (Starting from 1, must be a number only.)"))
  try:
    todo.pop(itemremove - 1)
    print("Succesfully deleted item " + str(itemremove) + "!")
  except:
    print("Invalid command!")

#Command dictionary
commands = {
"!help": display_help,
"!clear": clear_todo,
"!delete": delete_todo
}

while not exit:
    print("Todo List:")
    print(todo)
    
#Code to add new objectives to todo list
    newtodo = input()


#Command execution
    if newtodo in commands:
        commands[newtodo]()   

#Adding tasks 
    else:
        todo.append(newtodo)