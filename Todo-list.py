#Initialization
todo = []
exit = False


#Commands
def display_help():
    print("Here are a list of commands: !help !clear")

def clear_todo():
    todo.clear()
    print("To Do list cleared!")

#Command dictionary
commands = {
"!help": display_help,
"!clear": clear_todo
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