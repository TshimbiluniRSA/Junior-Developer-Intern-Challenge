from MyList import MyList

"""Print the main menu options for the Event Scheduler application."""
def print_menu():
    print("***********EVENT SCHEDULER CONSOLE APPLICATION***********")
    print("\nChoose the Option to Perform:")
    print("1. Create Event")
    print("2. Search Event")
    print("3. Delete Event")
    print("4. Display All Events")
    print("5. Search Events by Date or Keyword")
    print("0. Exit\n")

"""Get user input for the desired action. Return an integer representing the user's choice."""
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

"""Prompt the user to create a new event and call the corresponding MyList method."""
def create_event(my_list):
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    time = input("Enter event time (HH:MM): ")
    my_list.create_event(title, description, date, time)

"""Prompt the user to search for an event by title and call the corresponding MyList method."""
def search_event(my_list):
    title = input("Enter event title to search: ")
    my_list.search_event(title)

"""Prompt the user to delete an event by title and call the corresponding MyList method."""
def delete_event(my_list):
    title = input("Enter event title to delete: ")
    my_list.delete_event(title)

"""Call the MyList method to display all events in the list."""
def display_all_events(my_list):
    my_list.display_all_events()

"""Search for events by date or keyword and call the corresponding MyList method."""
def search_events(my_list):
    search_query = input("Enter date or keyword to search: ")
    my_list.search_events(search_query)

"""Main function to run the Event Scheduler application."""
def main():
    my_list = MyList()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 0:
            print("\nExiting the Event Scheduler App. Goodbye!")
            break
        elif choice == 1:
            create_event(my_list)
        elif choice == 2:
            search_event(my_list)
        elif choice == 3:
            delete_event(my_list)
        elif choice == 4:
            display_all_events(my_list)
        elif choice == 5:
            search_events(my_list)
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
