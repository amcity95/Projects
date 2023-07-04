#Custom functions for each action.
def read(file_path:str):
    with open(file_path, "r") as file:
        todo = file.readlines()
        return todo

def write(file_path:str):
    with open(file_path, "w") as file:
        file.writelines(todo)
#Looping to load one of the procedures.
while True:
    choice = input("make an action: ")
    choice.strip()

    if choice.startswith("add"):

        the_choice = choice.strip("add ") + "\n"
        todo = read("liste.txt")
        todo.append(the_choice)
        write("liste.txt")
        print("done")

    elif choice.startswith("show"):
        todo = read("liste.txt")
        file_final = [item.strip("\n") for item in todo]
        for n, i in enumerate(file_final):
            print(f"{n + 1}-{i}")

    elif choice.startswith("remove"):

        try:
            choice_made_to_remove = choice.strip("remove ")
            todo = read("liste.txt")
            todo.pop(int(choice_made_to_remove) - 1)
            write("liste.txt")
            print("Done!")

        except:
            print("Something went wrong with your prompt, try to be sure about the index in list must be a number.")

    elif choice.startswith("edit"):

        try:
            todo = read("liste.txt")
            choice_1 = choice.strip("edit ")
            choice_2 = int(choice_1) - 1
            choice_made_to_edit = todo[int(choice_2)]
            editing = input(f"so you want to edit {choice_made_to_edit} with: ") + "\n"
            todo[(int(choice_1) - 1)] = editing
            write("liste.txt")
        except:
            "Something went wrong, probably choose the index in list."
        print("Done!")

    elif  choice.startswith("exit"):
        break
    else:
        print("Not valid command.")
print("Bye")
