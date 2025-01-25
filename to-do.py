tasks = [] 

if __name__ == "__main__":
    pass
def addTask(task: str):
    try:
        tasks.append(task)
        print(tasks)
    except ValueError:
        print("Invalid Value.")

def removeTask(task: int):
    try:
        if 0 <= task < len(tasks):
            tasks.pop(task)
            print(tasks)
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid value.")
def showTask():
    print(tasks)


print("Welcome to the to do list. ")
while True:
    print("1. Add\n")
    print("2. Remove\n")
    print("3. Show\n")
    print("4. Exit\n")
    action = int(input("Enter the action: "))
    if action == 1:
        list = input("What do you want to add? -> ")
        addTask(list)
    elif action == 2:
        list = int(input("Which number do you want to remove? ->"))
        removeTask(list)
    elif action == 3:
        showTask()
    elif action == 4:
        exit()
    else:
        print()