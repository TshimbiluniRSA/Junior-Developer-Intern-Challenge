from EventScheduler import EventScheduler

class MyList:
    """Initialize a MyList instance with an empty list of events."""
    def __init__(self):
        self.events = []
            
    """Print a message as part of the results."""
    def _print_results(self, message):
        print("\nResults:")
        print(message + "\n")
        
    """Create a new event and append it to the list of events."""
    def create_event(self, title, description, date, time):
        new_event = EventScheduler(title, description, date, time)
        self.events.append(new_event)
        self._print_results("Event created successfully!")

    """Delete an event based on its title."""
    def delete_event(self, title):
        for event in self.events:
            if event.get_title() == title:
                self.events.remove(event)
                self._print_results(f"Event with title '{title}' deleted successfully!")
                return
        self._print_results(f"Event with title '{title}' not found.")

    """Search for an event based on its title."""
    def search_event(self, title):
        for event in self.events:
            if event.get_title() == title:
                self._print_results("Event found:")
                print(event)
                return
        self._print_results(f"Event with title '{title}' not found.")

    """Display all events in the list, sorted by date and time."""
    def display_all_events(self):
        if not self.events:
            self._print_results("No events found.")
        else:
            self._print_results("All events:") 
            for event in self.events:
                print(event)
