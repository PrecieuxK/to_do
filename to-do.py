tasks = [] 
file = open("tasks.txt","w")

def readfromFile():
    try:
        with open("tasks.txt", "r") as file:
            for item in file:
                tasks.append(item.strip())
    except FileNotFoundError:
        pass

def addtoFile():
    with open("tasks.txt", "w") as file:
        for item in tasks:
            file.write(item + "\n")

def addTask(task: str):
        tasks.append(task)
        print(tasks)
        addtoFile()

def removeTask(task: int):
    try:
        if 0 <= task < len(tasks):
            tasks.pop(task)
            print(tasks)
            addtoFile()
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid value.")

def showTask():
    print(tasks)

def clearFile():
    with open("tasks.txt", "w"):
        pass
    tasks = []
    print("Cleared")
    
print("Welcome to the to do list. ")
while True:
    print("1. Add\n")
    print("2. Remove\n")
    print("3. Show\n")
    print("4. Exit\n")
    print("5. Clear List\n")
    action = input("Enter the action: ")
    if action == "1":
        list = input("What do you want to add? -> ")
        addTask(list)
    elif action == "2":
        list = int(input("Which number do you want to remove? ->"))
        removeTask(list)
    elif action == "3":
        showTask()
    elif action == "4":
        exit()
    elif action == "5":
        clearFile()
    else:
        print("Try again.")