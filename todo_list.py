lst = ["sleep", "code", "Write"]

while True:
    k = "------ TO-DO LIST MENU ------\n1. Add Task\n2.Update Tasks\n3. View Task\n4. Delete Task\n5. Exit"
    print(k)
    ch = int(input("Enter your choice: "))

    if ch == 1:
        h = input("Enter a task to add: ")
        lst.append(h)
        print(lst)

    elif ch == 2:
        y = int(input("Enter a task number to update: "))
        if y <= len(lst) and y >= 1:
            lst[y - 1] = input("Enter a task name to replace: ")
            print(lst)
        else:
            print("Invalid task number")

    elif ch == 3:
        print(lst)

    elif ch == 4:
        u = int(input("Enter a task num to delete"))
        if u <= len(lst) and u >= 1:
            n = u - 1
            lst.pop(n)
            print(lst)
        else:
            print("Invalid task num")

    elif ch == 5:
        print("Exit program")
        break

    else:
        print("Enter num blw the choice range")