package main

import (
	"bufio"
	"fmt"
	"os"
	// "strings"
)

type Task struct {
	description string
	completed   bool
}

type TodoList struct {
	tasks []Task
}

func (list *TodoList) addTask(description string) {
	task := Task{description: description, completed: false}
	list.tasks = append(list.tasks, task)
	fmt.Println("Task added successfully!")
}

func (list *TodoList) listTasks() {
	if len(list.tasks) == 0 {
		fmt.Println("No tasks found.")
		return
	}

	fmt.Println("Tasks:")
	for i, task := range list.tasks {
		status := " "
		if task.completed {
			status = "✔"
		}
		fmt.Printf("%d. [%s] %s\n", i+1, status, task.description)
	}
}

func (list *TodoList) completeTask(index int) {
	if index < 0 || index >= len(list.tasks) {
		fmt.Println("Invalid task number.")
		return
	}

	list.tasks[index].completed = true
	fmt.Println("Task marked as completed!")
}

func main() {
	todoList := TodoList{}
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Simple Todo List")
	fmt.Println("----------------")

	for {
		fmt.Println("\n1. Add Task")
		fmt.Println("2. List Tasks")
		fmt.Println("3. Mark Task as Completed")
		fmt.Println("4. Exit")
		fmt.Print("\nEnter your choice: ")

		scanner.Scan()
		choice := scanner.Text()

		switch choice {
		case "1":
			fmt.Print("Enter task description: ")
			scanner.Scan()
			description := scanner.Text()
			todoList.addTask(description)
		case "2":
			todoList.listTasks()
		case "3":
			fmt.Print("Enter task number to mark as completed: ")
			scanner.Scan()
			indexStr := scanner.Text()
			index := 0
			fmt.Sscan(indexStr, &index)
			todoList.completeTask(index - 1)
		case "4":
			fmt.Println("Exiting...")
			os.Exit(0)
		default:
			fmt.Println("Invalid choice. Please choose a valid option.")
		}
	}
}