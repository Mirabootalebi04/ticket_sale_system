
class Event:
    '''
    represents an event
    '''
    def __init__ (self, title, total_capacity, date): 
        self.title = title 
        self.total_capacity = total_capacity 
        self.remaining_capacity = total_capacity 
        self.date = date

class Ticket:
    '''
    represents a reserved ticket by user ID and event title.
    ''' 
    def __init__ (self, national_id, event_title): 
        self.national_id = national_id 
        self.event_title = event_title

class EventManager: 
    '''
    handles creation, lookup, listing and management of all events
    '''
    def __init__ (self): 
        self.events = [] # list of event objects
    
    def create_event(self, title, capacity, date):
        event = Event(title, capacity, date)
        self.events.append(event)
    
    def list_events(self):
        for event in self.events:
            print(f"{event.title} | {event.date} | Total: {event.total_capacity} | Left: {event.remaining_capacity}")
    
    def find_event(self, title):
        for event in self.events:
            if event.title == title:
                return event
        return None

class TicketManager: 
    '''
    handles creating, viewing and canceling tickets by user ID and event title. 
    '''
    def __init__(self): 
        self.tickets = [] # list of ticket objects 
    
    def reserve_ticket(self, national_id, event):
        if event.remaining_capacity > 0:
            ticket = Ticket(national_id, event.title)
            self.tickets.append(ticket)
            event.remaining_capacity -= 1
            return True
        return False
    
    def cancel_ticket(self, national_id, event_title):
        for ticket in self.tickets:
            if ticket.national_id == national_id and ticket.event_title == event_title:
                self.tickets.remove(ticket)
                return True
        return False
    
    def view_tickets(self, national_id):
        user_tickets = [t for t in self.tickets if t.national_id == national_id]
        if user_tickets:
            for t in user_tickets:
                print(f"Reserved: {t.event_title} | {Event().self.date}")
        else:
            print("No reservations found.")

# ---system---
class TicketSalesSystem:
    '''
    the main controller: handles the user interface, admin login, and connects event/ticket managers together.'''
    def __init__(self): 
        self.event_manager = EventManager() 
        self.ticket_manager = TicketManager()
    
    def admin_login(self):
        username = input("Admin username: ")
        password = input("Admin password: ")
        return username == "lala" and password == "1234"
    
    def admin_menu(self):
        while True:
            print("\n[Admin Menu]\n1. Create Event\n2. View Events\n3. Logout")
            choice = input("choose the number : ")
            if choice == "1":
                title = input("Event title: ")
                capacity = int(input("Total capacity: "))
                date = input("Event date (YYYY-MM-DD): ")
                self.event_manager.create_event(title, capacity, date)
                print(f"Event created successfully.\n{title} | {date} | Total: {capacity}")
            elif choice == "2":
                self.event_manager.list_events()
            elif choice == "3":
                break
    
    def user_menu(self):
        while True:
            print("\n[User Menu]\n1. List Events\n2. Reserve Ticket\n3. View My Tickets\n4. Exit")
            choice = input("choose the number : ")
            if choice == "1":
                self.event_manager.list_events()
            elif choice == "2":
                self.event_manager.list_events()
                title = input("Enter event title you want to reserve : ")
                event = self.event_manager.find_event(title)
                if not event:
                    print("Event not found.")
                    continue
                n_id = input("Enter your national ID: ")
                if self.ticket_manager.reserve_ticket(n_id, event):
                    print("Ticket reserved successfully.")
                else:
                    print("No tickets left.")
            elif choice == "3":
                n_id = input("Enter your national ID: ")
                self.ticket_manager.view_tickets(n_id)
            elif choice == "4":
                break
    
    def run(self):
        while True:
            print("\n--- Ticket Sales System ---\n1. Admin Login\n2. User Access\n3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                if self.admin_login():
                    self.admin_menu()
                else:
                    print("Invalid credentials.")
            elif choice == "2":
                self.user_menu()
            elif choice == "3":
                print("Goodbye!")
                break

if __name__ == "__main__": 
    system = TicketSalesSystem() 
    system.run()
