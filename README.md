# Junior-Developer-Intern-Challenge

# Event Scheduler Console Application

## Overview
The Event Scheduler Console Application is a simple command-line tool designed to help you manage events efficiently. It allows you to create, search, delete, and display events using a text-based interface.

## Features
- **Data Storage:**
  - Events are stored in a simple in-memory structure.
  - No need for external database or file storage.

- **Event Creation:**
  - Add new events with title, description, date, and time.
  - Date and time formats are validated for accuracy.

- **Listing Events:**
  - Display all events sorted by date and time.
  - Detailed information about each event is presented.

- **Deleting Events:**
  - Remove events based on their title.
  - Informative messages for non-existing events.

- **User Interface:**
  - Text-based interface for easy interaction.
  - Options to create, view, and delete events.

## Code Structure
- **EventScheduler Class:**
  - Manages individual events.
  - Handles event attributes, validation, and formatting.

- **MyList Class:**
  - Manages a list of events.
  - Provides functions for event manipulation.

- **TestEventSchedulerApp:**
  - Main application logic.
  - Displays a menu and calls corresponding functions.

## Usage
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/TshimbiluniRSA/Junior-Developer-Intern-Challenge
