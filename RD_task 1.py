class ToDoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task'{task}'added.")
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task'{task}'removed.")
        else:
            print(f"Task'{task}'not found.")
    def view_tasks(self):
        if self.task:
            print("To-Do List:")
            for idx,task in enumerate (self.task,1):
                print(f"{idx}.{task}")
        else:
            print("your to-do list is empty.")
def main():
    todo_list = ToDoList()

    while True:
        print("\n To-Do List Menu:")
        print("1. add a task")
        print("2.remove a task")
        print("3. view task")
        print("4. exit")
        choice= input(" choose an option:")

        if choice == '1':
            task= input("enter the task:")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("enter the task to remove :")
            todo_list.remove_task(task)
        elif choice=='3':
            todo_list.view_task()
        elif choice =='4':
            print("goodbye")
            break
        else:
            print(" invalid choice. please try again.")

if __name__=="__main__":
    main()
            
