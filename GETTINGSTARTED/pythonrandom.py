def main():
    tasks = []

    while True:
        print("\n----- To.Do List -----")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Tasks as Done")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter your task: ")
                task.append({"Task": task, "done": False})
                print("Task Added")
                
        elif choice == '2':
            print("\n Tasks: ")
            for index, task in enumerate(tasks):
                status = "Done" if task["Done"] else "Not Done"
                print(f"{index + 1}. {task["task"]} - {status}")
                
        elif choice == '3':
            task_index = int(input("Enter the task number to mark done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Done"] = True
                print("Task marked as done")
            else: 
                print("Invalid task number") 
                
        elif choice =='4':
            print("Exiting the To Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
                         
            
        


