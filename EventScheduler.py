import re

class EventScheduler:
    """Initialize an EventScheduler instance with provided attributes."""
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
    
    """Get the title of the event."""
    def get_title(self):
        return self.title

    """Set the title of the event."""
    def set_title(self, title):
        self.title = title

    """Get the description of the event."""
    def get_description(self):
        return self.description

    """Set the description of the event."""
    def set_description(self, description):
        self.description = description

    """Get the date of the event."""
    def get_date(self):
        return self.date

    """Set the date of the event after validating the format."""
    def set_date(self, date):
        if self.validate_date_format(date):
            self.date = date
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    """Get the time of the event."""
    def get_time(self):
        return self.time

    """Set the time of the event after validating the format."""
    def set_time(self, time):
        if self.validate_time_format(time):
            self.time = time
        else:
            print("Invalid time format. Please use HH:MM.")

    """Validate if the provided date follows the YYYY-MM-DD format."""
    def validate_date_format(self, date):
        date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
        return bool(date_pattern.match(date))

    """Validate if the provided time follows the HH:MM format."""
    def validate_time_format(self, time):
        time_pattern = re.compile(r"\d{2}:\d{2}")
        return bool(time_pattern.match(time))

    """Return a string representation of the EventScheduler instance."""
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDate: {self.date}\nTime: {self.time}"