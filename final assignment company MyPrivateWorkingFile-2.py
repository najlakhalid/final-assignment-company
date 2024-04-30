#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk  # Importing the tkinter library for GUI
from tkinter import ttk, messagebox  # Importing specific modules from tkinter for GUI components
import pickle  # Importing the pickle module for object serialization

# Employee Class
class Employee:
    def __init__(self, emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        # Constructor method for initializing employee attributes
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id

# EmployeeManagementSystem Class
class EmployeeManagementSystem:
    def __init__(self):
        # Constructor method for initializing EmployeeManagementSystem attributes
        self.employees = []
        self.load_from_file()

    # Create Employee
    def create_employee(self, emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        # Method for creating a new employee object and appending it to the employees list
        employee = Employee(emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)
        self.employees.append(employee)
        self.save_to_file()
        messagebox.showinfo("Success", "Employee created successfully.")

    # Read all Employees
    def read_employees(self):
        # Method for retrieving information of all employees and displaying it in a messagebox
        employee_info = ""
        for employee in self.employees:
            employee_info += f"ID: {employee.emp_id}, Name: {employee.name}, Department: {employee.department}, Job Title: {employee.job_title}, Basic Salary: {employee.basic_salary}, Age: {employee.age}, Date of Birth: {employee.date_of_birth}, Passport Details: {employee.passport_details}, Manager ID: {employee.manager_id}\n"
        messagebox.showinfo("Employees", employee_info)

    # Update Employee
    def update_employee(self, emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        # Method for updating information of an existing employee
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.name = name
                employee.department = department
                employee.job_title = job_title
                employee.basic_salary = basic_salary
                employee.age = age
                employee.date_of_birth = date_of_birth
                employee.passport_details = passport_details
                employee.manager_id = manager_id
                self.save_to_file()
                messagebox.showinfo("Success", "Employee updated successfully.")
                return
        messagebox.showerror("Error", "Employee not found.")

    # Delete an Employee
    def delete_employee(self, emp_id):
        # Method for deleting an employee from the employees list
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                self.save_to_file()
                messagebox.showinfo("Success", "Employee deleted successfully.")
                return
        messagebox.showerror("Error", "Employee not found.")

    # Search Employee
    def search_employee(self, emp_id):
        # Method for searching an employee by employee ID
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

    def save_to_file(self):
        # Method for serializing the employees list and saving it to a file
        with open("employees.pickle", "wb") as file:
            pickle.dump(self.employees, file)

    def load_from_file(self):
        # Method for deserializing the employees list from a file
        try:
            with open("employees.pickle", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

# Client Class
class Client:
    def __init__(self, client_id, name, address, contact, budget):
        # Constructor method for initializing client attributes
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact = contact
        self.budget = budget

# ClientManagementSystem Class
class ClientManagementSystem:
    def __init__(self):
        # Constructor method for initializing ClientManagementSystem attributes
        self.clients = []
        self.load_from_file()

    # Create Client
    def create_client(self, client_id, name, address, contact, budget):
        # Method for creating a new client object and appending it to the clients list
        client = Client(client_id, name, address, contact, budget)
        self.clients.append(client)
        self.save_to_file()
        messagebox.showinfo("Success", "Client created successfully.")

    # Read all Clients
    def read_clients(self):
        # Method for retrieving information of all clients and displaying it in a messagebox
        client_info = ""
        for client in self.clients:
            client_info += f"ID: {client.client_id}, Name: {client.name}, Address: {client.address}, Contact: {client.contact}, Budget: {client.budget}\n"
        messagebox.showinfo("Clients", client_info)

    # Update Client
    def update_client(self, client_id, name, address, contact, budget):
        # Method for updating information of an existing client
        for client in self.clients:
            if client.client_id == client_id:
                client.name = name
                client.address = address
                client.contact = contact
                client.budget = budget
                self.save_to_file()
                messagebox.showinfo("Success", "Client updated successfully.")
                return
        messagebox.showerror("Error", "Client not found.")

    # Delete a Client
    def delete_client(self, client_id):
        # Method for deleting a client from the clients list
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                self.save_to_file()
                messagebox.showinfo("Success", "Client deleted successfully.")
                return
        messagebox.showerror("Error", "Client not found.")

    # Search Client
    def search_client(self, client_id):
        # Method for searching a client by client ID
        for client in self.clients:
            if int(client.client_id) == int(client_id):
                return client
        return None

    def save_to_file(self):
        # Method for serializing the clients list and saving it to a file
        with open("clients.pickle", "wb") as file:
            pickle.dump(self.clients, file)

    def load_from_file(self):
        # Method for deserializing the clients list from a file
        try:
            with open("clients.pickle", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []
            
# Venue Class
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Constructor method for initializing venue attributes
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

# VenueManagementSystem Class
class VenueManagementSystem:
    def __init__(self):
        # Constructor method for initializing VenueManagementSystem attributes
        self.venues = []
        self.load_from_file()

    # Create Venue
    def create_venue(self, venue_id, name, address, contact, min_guests, max_guests):
        # Method for creating a new venue object and appending it to the venues list
        venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        self.venues.append(venue)
        self.save_to_file()
        messagebox.showinfo("Success", "Venue created successfully.")

    # Read all Venues
    def read_venues(self):
        # Method for retrieving information of all venues and displaying it in a messagebox
        venue_info = ""
        for venue in self.venues:
            venue_info += f"ID: {venue.venue_id}, Name: {venue.name}, Address: {venue.address}, Contact: {venue.contact}, Min Guests: {venue.min_guests}, Max Guests: {venue.max_guests}\n"
        messagebox.showinfo("Venues", venue_info)

    # Update Venue
    def update_venue(self, venue_id, name, address, contact, min_guests, max_guests):
        # Method for updating information of an existing venue
        for venue in self.venues:
            if venue.venue_id == venue_id:
                venue.name = name
                venue.address = address
                venue.contact = contact
                venue.min_guests = min_guests
                venue.max_guests = max_guests
                self.save_to_file()
                messagebox.showinfo("Success", "Venue updated successfully.")
                return
        messagebox.showerror("Error", "Venue not found.")

    # Delete a Venue
    def delete_venue(self, venue_id):
        # Method for deleting a venue from the venues list
        for venue in self.venues:
            if venue.venue_id == venue_id:
                self.venues.remove(venue)
                self.save_to_file()
                messagebox.showinfo("Success", "Venue deleted successfully.")
                return
        messagebox.showerror("Error", "Venue not found.")

    # Search Venue
    def search_venue(self, venue_id):
        # Method for searching a venue by venue ID
        for venue in self.venues:
            if int(venue.venue_id) == int(venue_id):
                return venue
        return None

    def save_to_file(self):
        # Method for serializing the venues list and saving it to a file
        with open("venues.pickle", "wb") as file:
            pickle.dump(self.venues, file)

    def load_from_file(self):
        # Method for deserializing the venues list from a file
        try:
            with open("venues.pickle", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = []
            
# Guest Class
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        # Constructor method for initializing guest attributes
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        

# GuestManagementSystem Class
class GuestManagementSystem:
    def __init__(self):
        # Constructor method for initializing GuestManagementSystem attributes
        self.guests = []
        self.load_from_file()

    # Create Guest
    def create_guest(self, guest_id, name, address, contact_details):
        # Method for creating a new guest object and appending it to the guests list
        guest = Guest(guest_id, name, address, contact_details)
        self.guests.append(guest)
        self.save_to_file()
        messagebox.showinfo("Success", "Guest created successfully.")

    # Read all Guests
    def read_guests(self):
        # Method for retrieving information of all guests and displaying it in a messagebox
        guest_info = ""
        for guest in self.guests:
            guest_info += f"ID: {guest.guest_id}, Name: {guest.name}, Address: {guest.address}, Contact Details: {guest.contact_details}\n"
        messagebox.showinfo("Guests", guest_info)

    # Update Guest
    def update_guest(self, guest_id, name, address, contact_details):
        # Method for updating information of an existing guest
        for guest in self.guests:
            if guest.guest_id == guest_id:
                guest.name = name
                guest.address = address
                guest.contact_details = contact_details
                self.save_to_file()
                messagebox.showinfo("Success", "Guest updated successfully.")
                return
        messagebox.showerror("Error", "Guest not found.")

    # Delete a Guest
    def delete_guest(self, guest_id):
        # Method for deleting a guest from the guests list
        for guest in self.guests:
            if guest.guest_id == guest_id:
                self.guests.remove(guest)
                self.save_to_file()
                messagebox.showinfo("Success", "Guest deleted successfully.")
                return
        messagebox.showerror("Error", "Guest not found.")
        
    # Search Guest
    def search_guest(self, guest_id):
        # Method for searching a guest by guest ID
        for guest in self.guests:
            if int(guest.guest_id) == int(guest_id):
                return guest
        return None

    def save_to_file(self):
        # Method for serializing the guests list and saving it to a file
        with open("guests.pickle", "wb") as file:
            pickle.dump(self.guests, file)

    def load_from_file(self):
        # Method for deserializing the guests list from a file
        try:
            with open("guests.pickle", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []
            
# Supplier Class
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        # Constructor method for initializing supplier attributes
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

# SupplierManagementSystem Class
class SupplierManagementSystem:
    def __init__(self):
        # Constructor method for initializing SupplierManagementSystem attributes
        self.suppliers = []
        self.load_from_file()

    # Create Supplier
    def create_supplier(self, supplier_id, name, address, contact_details):
        # Method for creating a new supplier object and appending it to the suppliers list
        supplier = Supplier(supplier_id, name, address, contact_details)
        self.suppliers.append(supplier)
        self.save_to_file()
        messagebox.showinfo("Success", "Supplier created successfully.")

    # Read all Suppliers
    def read_suppliers(self):
        # Method for retrieving information of all suppliers and displaying it in a messagebox
        supplier_info = ""
        for supplier in self.suppliers:
            supplier_info += f"ID: {supplier.supplier_id}, Name: {supplier.name}, Address: {supplier.address}, Contact Details: {supplier.contact_details}\n"
        messagebox.showinfo("Suppliers", supplier_info)

    # Update Supplier
    def update_supplier(self, supplier_id, name, address, contact_details):
        # Method for updating information of an existing supplier
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                supplier.name = name
                supplier.address = address
                supplier.contact_details = contact_details
                self.save_to_file()
                messagebox.showinfo("Success", "Supplier updated successfully.")
                return
        messagebox.showerror("Error", "Supplier not found.")

    # Delete a Supplier
    def delete_supplier(self, supplier_id):
        # Method for deleting a supplier from the suppliers list
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                self.suppliers.remove(supplier)
                self.save_to_file()
                messagebox.showinfo("Success", "Supplier deleted successfully.")
                return
        messagebox.showerror("Error", "Supplier not found.")
        
    # Search Supplier
    def search_supplier(self, supplier_id):
        # Method for searching a supplier by supplier ID
        for supplier in self.suppliers:
            if int(supplier.supplier_id) == int(supplier_id):
                return supplier
        return None

    # Save Suppliers to File
    def save_to_file(self):
        # Method for serializing the suppliers list and saving it to a file
        with open("suppliers.pickle", "wb") as file:
            pickle.dump(self.suppliers, file)

    # Load Suppliers from File
    def load_from_file(self):
        # Method for deserializing the suppliers list from a file
        try:
            with open("suppliers.pickle", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []
            
            
# Event Class
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice):
        # Constructor method for initializing event attributes
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_id = venue_id
        self.client_id = client_id
        self.estimated_cost = estimated_cost
        self.actual_cost = actual_cost
        self.status = status
        self.invoice = invoice

# EventManagementSystem Class
class EventManagementSystem:
    def __init__(self):
        # Constructor method for initializing EventManagementSystem attributes
        self.events = []
        self.load_from_file()

    # Create Event
    def create_event(self, event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice):
        # Method for creating a new event object and appending it to the events list
        event = Event(event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice)
        self.events.append(event)
        self.save_to_file()
        messagebox.showinfo("Success", "Event created successfully.")

    # Read all Events
    def read_events(self):
        # Method for retrieving information of all events and displaying it in a messagebox
        event_info = ""
        for event in self.events:
            event_info += f"ID: {event.event_id}, Type: {event.event_type}, Theme: {event.theme}, Date: {event.date}, Time: {event.time}, Duration: {event.duration}, Venue ID: {event.venue_id}, Client ID: {event.client_id}, Estimated Cost: {event.estimated_cost}, Actual Cost: {event.actual_cost}, Status: {event.status}, Invoice: {event.invoice}\n"
        messagebox.showinfo("Events", event_info)

    # Update Event
    def update_event(self, event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice):
        # Method for updating information of an existing event
        for event in self.events:
            if event.event_id == event_id:
                event.event_type = event_type
                event.theme = theme
                event.date = date
                event.time = time
                event.duration = duration
                event.venue_id = venue_id
                event.client_id = client_id
                event.estimated_cost = estimated_cost
                event.actual_cost = actual_cost
                event.status = status
                event.invoice = invoice
                self.save_to_file()
                messagebox.showinfo("Success", "Event updated successfully.")
                return
        messagebox.showerror("Error", "Event not found.")

    # Delete Event
    def delete_event(self, event_id):
        # Method for deleting an event from the events list
        for event in self.events:
            if event.event_id == event_id:
                self.events.remove(event)
                self.save_to_file()
                messagebox.showinfo("Success", "Event deleted successfully.")
                return
        messagebox.showerror("Error", "Event not found.")

    # Search Event
    def search_event(self, event_id):
        # Method for searching an event by event ID
        for event in self.events:
            if int(event.event_id) == int(event_id):
                return event
        return None

    # Save Events to File
    def save_to_file(self):
        # Method for serializing the events list and saving it to a file
        with open("events.pickle", "wb") as file:
            pickle.dump(self.events, file)

    # Load Events from File
    def load_from_file(self):
        # Method for deserializing the events list from a file
        try:
            with open("events.pickle", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []
            
# Event_Guest Class
class Event_Guest:
    def __init__(self, id, event_id, guest_id):
        # Constructor method for initializing Event_Guest attributes
        self.id = id
        self.event_id = event_id
        self.guest_id = guest_id

# Event_GuestManagementSystem Class
class Event_GuestManagementSystem:
    def __init__(self):
        # Constructor method for initializing Event_GuestManagementSystem attributes
        self.event_guests = []
        self.load_from_file()

    # Create Event_Guest
    def create_event_guest(self, id, event_id, guest_id):
        # Method for creating a new event guest object and appending it to the event guests list
        event_guest = Event_Guest(id, event_id, guest_id)
        self.event_guests.append(event_guest)
        self.save_to_file()
        messagebox.showinfo("Success", "Event Guest created successfully.")

    # Read all Event Guests
    def read_event_guests(self):
        # Method for retrieving information of all event guests and displaying it in a messagebox
        event_guest_info = ""
        for event_guest in self.event_guests:
            event_guest_info += f"ID: {event_guest.id}, Event ID: {event_guest.event_id}, Guest ID: {event_guest.guest_id}\n"
        messagebox.showinfo("Event Guests", event_guest_info)

    # Update Event Guest
    def update_event_guest(self, id, event_id, guest_id):
        # Method for updating information of an existing event guest
        for event_guest in self.event_guests:
            if event_guest.id == id:
                event_guest.event_id = event_id
                event_guest.guest_id = guest_id
                self.save_to_file()
                messagebox.showinfo("Success", "Event Guest updated successfully.")
                return
        messagebox.showerror("Error", "Event Guest not found.")

    # Delete Event Guest
    def delete_event_guest(self, id):
        # Method for deleting an event guest from the event guests list
        for event_guest in self.event_guests:
            if event_guest.id == id:
                self.event_guests.remove(event_guest)
                self.save_to_file()
                messagebox.showinfo("Success", "Event Guest deleted successfully.")
                return
        messagebox.showerror("Error", "Event Guest not found.")

    # Save Event Guests to File
    def save_to_file(self):
        # Method for serializing the event guests list and saving it to a file
        with open("event_guests.pickle", "wb") as file:
            pickle.dump(self.event_guests, file)

    # Load Event Guests from File
    def load_from_file(self):
        # Method for deserializing the event guests list from a file
        try:
            with open("event_guests.pickle", "rb") as file:
                self.event_guests = pickle.load(file)
        except FileNotFoundError:
            self.event_guests = []

# Event_Supplier Class
class Event_Supplier:
    def __init__(self, id, event_id, supplier_id):
        # Constructor method for initializing Event_Supplier attributes
        self.id = id
        self.event_id = event_id
        self.supplier_id = supplier_id

# Event_SupplierManagementSystem Class
class Event_SupplierManagementSystem:
    def __init__(self):
        # Constructor method for initializing Event_SupplierManagementSystem attributes
        self.event_suppliers = []
        self.load_from_file()

    # Create Event Supplier
    def create_event_supplier(self, id, event_id, supplier_id):
        # Method for creating a new event supplier object and appending it to the event suppliers list
        event_supplier = Event_Supplier(id, event_id, supplier_id)
        self.event_suppliers.append(event_supplier)
        self.save_to_file()
        messagebox.showinfo("Success", "Event Supplier created successfully.")

    # Read all Event Suppliers
    def read_event_suppliers(self):
        # Method for retrieving information of all event suppliers and displaying it in a messagebox
        event_supplier_info = ""
        for event_supplier in self.event_suppliers:
            event_supplier_info += f"ID: {event_supplier.id}, Event ID: {event_supplier.event_id}, Supplier ID: {event_supplier.supplier_id}\n"
        messagebox.showinfo("Event Suppliers", event_supplier_info)

    # Update Event Supplier
    def update_event_supplier(self, id, event_id, supplier_id):
        # Method for updating information of an existing event supplier
        for event_supplier in self.event_suppliers:
            if event_supplier.id == id:
                event_supplier.event_id = event_id
                event_supplier.supplier_id = supplier_id
                self.save_to_file()
                messagebox.showinfo("Success", "Event Supplier updated successfully.")
                return
        messagebox.showerror("Error", "Event Supplier not found.")

    # Delete Event Supplier
    def delete_event_supplier(self, id):
        # Method for deleting an event supplier from the event suppliers list
        for event_supplier in self.event_suppliers:
            if event_supplier.id == id:
                self.event_suppliers.remove(event_supplier)
                self.save_to_file()
                messagebox.showinfo("Success", "Event Supplier deleted successfully.")
                return
        messagebox.showerror("Error", "Event Supplier not found.")

    # Save Event Suppliers to File
    def save_to_file(self):
        # Method for serializing the event suppliers list and saving it to a file
        with open("event_suppliers.pickle", "wb") as file:
            pickle.dump(self.event_suppliers, file)

    # Load Event Suppliers from File
    def load_from_file(self):
        # Method for deserializing the event suppliers list from a file
        try:
            with open("event_suppliers.pickle", "rb") as file:
                self.event_suppliers = pickle.load(file)
        except FileNotFoundError:
            self.event_suppliers = []
            

class ManagementGUI:
    def __init__(self, root):
        # Initialize the management GUI with root window
        self.root = root
        # Initialize instances of management systems
        self.employee_management = EmployeeManagementSystem()
        self.client_management = ClientManagementSystem()
        self.venue_management = VenueManagementSystem()  
        self.guest_management = GuestManagementSystem()
        self.supplier_management = SupplierManagementSystem()
        self.event_management = EventManagementSystem()
        self.event_guest_management = Event_GuestManagementSystem()
        self.event_supplier_management = Event_SupplierManagementSystem()
        self.event_id_values = []  
        self.guest_id_values = []  
        self.supplier_id_values = []  
        self.create_gui()

    def create_gui(self):
        # Create the GUI components
        notebook = ttk.Notebook(self.root)
        notebook.pack(side="left", fill="both", expand=True)

        # Create tabs for each management system
        self.employee_tab = ttk.Frame(notebook)
        notebook.add(self.employee_tab, text="Employee")

        self.client_tab = ttk.Frame(notebook)
        notebook.add(self.client_tab, text="Client")

        self.venue_tab = ttk.Frame(notebook)  
        notebook.add(self.venue_tab, text="Venue")  
        
        self.guest_tab = ttk.Frame(notebook)  
        notebook.add(self.guest_tab, text="Guest")  
        
        self.supplier_tab = ttk.Frame(notebook)  
        notebook.add(self.supplier_tab, text="Supplier")  
        
        self.event_tab = ttk.Frame(notebook)  
        notebook.add(self.event_tab, text="Event")

        self.event_guest_tab = ttk.Frame(notebook)
        notebook.add(self.event_guest_tab, text="Event Guests")

        self.event_supplier_tab = ttk.Frame(notebook)
        notebook.add(self.event_supplier_tab, text="Event Suppliers")

        # Bind tab change event to a method
        notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def on_tab_changed(self, event):
        # Event handler for tab change
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

        if tab_text == "Employee":
            self.create_employee_gui()
        elif tab_text == "Client":
            self.create_client_gui()
        elif tab_text == "Venue": 
            self.create_venue_gui()
        elif tab_text == "Guest":  
            self.create_guest_gui()
        elif tab_text == "Supplier":  
            self.create_supplier_gui()
        elif tab_text == "Event": 
            self.create_event_gui()
        elif tab_text == "Event Guests":
            self.create_event_guest_gui()
        elif tab_text == "Event Suppliers":
            self.create_event_supplier_gui()

    def create_event_gui(self):
        # Create GUI for managing events
        self.event_crud_container = tk.Frame(self.event_tab)
        self.event_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Labels and entries for event attributes
        self.event_id_label = tk.Label(self.event_crud_container, text="Event ID:")
        self.event_type_label = tk.Label(self.event_crud_container, text="Type:")
        self.theme_label = tk.Label(self.event_crud_container, text="Theme:")
        self.date_label = tk.Label(self.event_crud_container, text="Date:")
        self.time_label = tk.Label(self.event_crud_container, text="Time:")
        self.duration_label = tk.Label(self.event_crud_container, text="Duration:")
        self.venue_id_label = tk.Label(self.event_crud_container, text="Venue ID:")
        self.client_id_label = tk.Label(self.event_crud_container, text="Client ID:")
        self.estimated_cost_label = tk.Label(self.event_crud_container, text="Estimated Cost:")
        self.actual_cost_label = tk.Label(self.event_crud_container, text="Actual Cost:")
        self.status_label = tk.Label(self.event_crud_container, text="Status:")
        self.invoice_label = tk.Label(self.event_crud_container, text="Invoice:")

        self.event_id_entry = tk.Entry(self.event_crud_container)
        self.event_type_entry = tk.Entry(self.event_crud_container)
        self.theme_entry = tk.Entry(self.event_crud_container)
        self.date_entry = tk.Entry(self.event_crud_container)
        self.time_entry = tk.Entry(self.event_crud_container)
        self.duration_entry = tk.Entry(self.event_crud_container)
        self.venue_id_entry = ttk.Combobox(self.event_crud_container, state="readonly")
        self.client_id_entry = ttk.Combobox(self.event_crud_container, state="readonly")
        self.estimated_cost_entry = tk.Entry(self.event_crud_container)
        self.actual_cost_entry = tk.Entry(self.event_crud_container)
        self.status_entry = tk.Entry(self.event_crud_container)
        self.invoice_entry = tk.Entry(self.event_crud_container)

        # Buttons for event management
        self.create_event_button = tk.Button(self.event_crud_container, text="Create Event", command=self.create_event)
        self.read_event_button = tk.Button(self.event_crud_container, text="Read Events", command=self.read_events)
        self.update_event_button = tk.Button(self.event_crud_container, text="Update Event", command=self.update_event)
        self.delete_event_button = tk.Button(self.event_crud_container, text="Delete Event", command=self.delete_event)
        self.search_event_button = tk.Button(self.event_crud_container, text="Search Event", command=self.search_event)

        # Populate venue and client IDs
        self.populate_venue_client_ids()

        # Grid layout for GUI components
        self.event_id_label.grid(row=0, column=0, sticky="e")
        self.event_type_label.grid(row=1, column=0, sticky="e")
        self.theme_label.grid(row=2, column=0, sticky="e")
        self.date_label.grid(row=3, column=0, sticky="e")
        self.time_label.grid(row=4, column=0, sticky="e")
        self.duration_label.grid(row=5, column=0, sticky="e")
        self.venue_id_label.grid(row=6, column=0, sticky="e")
        self.client_id_label.grid(row=7, column=0, sticky="e")
        self.estimated_cost_label.grid(row=8, column=0, sticky="e")
        self.actual_cost_label.grid(row=9, column=0, sticky="e")
        self.status_label.grid(row=10, column=0, sticky="e")
        self.invoice_label.grid(row=11, column=0, sticky="e")

        self.event_id_entry.grid(row=0, column=1, pady=5)
        self.event_type_entry.grid(row=1, column=1, pady=5)
        self.theme_entry.grid(row=2, column=1, pady=5)
        self.date_entry.grid(row=3, column=1, pady=5)
        self.time_entry.grid(row=4, column=1, pady=5)
        self.duration_entry.grid(row=5, column=1, pady=5)
        self.venue_id_entry.grid(row=6, column=1, pady=5)
        self.client_id_entry.grid(row=7, column=1, pady=5)
        self.estimated_cost_entry.grid(row=8, column=1, pady=5)
        self.actual_cost_entry.grid(row=9, column=1, pady=5)
        self.status_entry.grid(row=10, column=1, pady=5)
        self.invoice_entry.grid(row=11, column=1, pady=5)

        self.create_event_button.grid(row=12, column=1, columnspan=2, pady=10)
        self.read_event_button.grid(row=12, column=3, columnspan=2, pady=5)
        self.update_event_button.grid(row=12, column=5, columnspan=2, pady=5)
        self.delete_event_button.grid(row=12, column=7, columnspan=2, pady=5)
        self.search_event_button.grid(row=12, column=9, columnspan=2, pady=5)

        # Treeview for displaying events
        self.event_tree = ttk.Treeview(self.event_tab, columns=("ID", "Type", "Theme", "Date", "Time", "Duration", "Venue ID", "Client ID", "Estimated Cost", "Actual Cost", "Status", "Invoice"), show="headings")
        
        # Configure treeview columns
        for col in self.event_tree["columns"]:
            self.event_tree.heading(col, text=col)
        
        # Set column widths
        column_width = 100  
        for col in self.event_tree["columns"]:
            self.event_tree.column(col, width=column_width, minwidth=column_width)
        
        # Grid layout for treeview
        self.event_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Scrollbar for treeview
        vsb = ttk.Scrollbar(self.event_tab, orient="vertical", command=self.event_tree.yview)
        self.event_tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
        
    def create_guest_gui(self):
        # Create the GUI container for guest management
        self.guest_crud_container = tk.Frame(self.guest_tab)
        self.guest_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Labels for guest attributes
        self.guest_id_label = tk.Label(self.guest_crud_container, text="Guest ID:")
        self.guest_name_label = tk.Label(self.guest_crud_container, text="Name:")
        self.guest_address_label = tk.Label(self.guest_crud_container, text="Address:")
        self.guest_contact_label = tk.Label(self.guest_crud_container, text="Contact Details:")
    
        # Entry fields for guest attributes
        self.guest_id_entry = tk.Entry(self.guest_crud_container)
        self.guest_name_entry = tk.Entry(self.guest_crud_container)
        self.guest_address_entry = tk.Entry(self.guest_crud_container)
        self.guest_contact_entry = tk.Entry(self.guest_crud_container)
    
        # Buttons for guest management
        self.create_guest_button = tk.Button(self.guest_crud_container, text="Create Guest", command=self.create_guest)
        self.read_guest_button = tk.Button(self.guest_crud_container, text="Read Guests", command=self.read_guests)
        self.update_guest_button = tk.Button(self.guest_crud_container, text="Update Guest", command=self.update_guest)
        self.delete_guest_button = tk.Button(self.guest_crud_container, text="Delete Guest", command=self.delete_guest)
        self.search_guest_button = tk.Button(self.guest_crud_container, text="Search Guest", command=self.search_guest)
    
        # Grid layout for guest management components
        self.guest_id_label.grid(row=0, column=0, sticky="e")
        self.guest_name_label.grid(row=1, column=0, sticky="e")
        self.guest_address_label.grid(row=2, column=0, sticky="e")
        self.guest_contact_label.grid(row=3, column=0, sticky="e")
    
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.guest_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.guest_address_entry.grid(row=2, column=1, padx=5, pady=5)
        self.guest_contact_entry.grid(row=3, column=1, padx=5, pady=5)
    
        self.create_guest_button.grid(row=4, column=1, columnspan=2, pady=10)
        self.read_guest_button.grid(row=4, column=3, columnspan=2, pady=10)
        self.update_guest_button.grid(row=4, column=5, columnspan=2, pady=10)
        self.delete_guest_button.grid(row=4, column=7, columnspan=2, pady=10)
        self.search_guest_button.grid(row=4, column=9, columnspan=2, pady=10)
        
        # Treeview for displaying guests
        self.guest_tree = ttk.Treeview(self.guest_tab, columns=("ID", "Name", "Address", "Contact Details"), show="headings")
        self.guest_tree.heading("ID", text="ID")
        self.guest_tree.heading("Name", text="Name")
        self.guest_tree.heading("Address", text="Address")
        self.guest_tree.heading("Contact Details", text="Contact Details")
    
        # Scrollbar for guest treeview
        vsb = ttk.Scrollbar(self.guest_tab, orient="vertical", command=self.guest_tree.yview)
        self.guest_tree.configure(yscrollcommand=vsb.set)
    
        # Grid layout for guest treeview
        self.guest_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
    
    def create_supplier_gui(self):
        # Create the GUI container for supplier management
        self.supplier_crud_container = ttk.Frame(self.supplier_tab)
        self.supplier_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Labels for supplier attributes
        self.supplier_id_label = ttk.Label(self.supplier_crud_container, text="Supplier ID:")
        self.supplier_name_label = ttk.Label(self.supplier_crud_container, text="Name:")
        self.supplier_address_label = ttk.Label(self.supplier_crud_container, text="Address:")
        self.supplier_contact_label = ttk.Label(self.supplier_crud_container, text="Contact Details:")
    
        # Entry fields for supplier attributes
        self.supplier_id_entry = ttk.Entry(self.supplier_crud_container)
        self.supplier_name_entry = ttk.Entry(self.supplier_crud_container)
        self.supplier_address_entry = ttk.Entry(self.supplier_crud_container)
        self.supplier_contact_entry = ttk.Entry(self.supplier_crud_container)
    
        # Buttons for supplier management
        self.create_supplier_button = ttk.Button(self.supplier_crud_container, text="Create Supplier", command=self.create_supplier)
        self.read_supplier_button = ttk.Button(self.supplier_crud_container, text="Read Suppliers", command=self.read_suppliers)
        self.update_supplier_button = ttk.Button(self.supplier_crud_container, text="Update Supplier", command=self.update_supplier)
        self.delete_supplier_button = ttk.Button(self.supplier_crud_container, text="Delete Supplier", command=self.delete_supplier)
        self.search_supplier_button = ttk.Button(self.supplier_crud_container, text="Search Supplier", command=self.search_supplier)
    
        # Grid layout for supplier management components
        self.supplier_id_label.grid(row=0, column=0, sticky="e")
        self.supplier_name_label.grid(row=1, column=0, sticky="e")
        self.supplier_address_label.grid(row=2, column=0, sticky="e")
        self.supplier_contact_label.grid(row=3, column=0, sticky="e")
    
        self.supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)
        self.supplier_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.supplier_address_entry.grid(row=2, column=1, padx=5, pady=5)
        self.supplier_contact_entry.grid(row=3, column=1, padx=5, pady=5)
    
        self.create_supplier_button.grid(row=4, column=1, columnspan=2, pady=10)
        self.read_supplier_button.grid(row=4, column=3, columnspan=2, pady=10)
        self.update_supplier_button.grid(row=4, column=5, columnspan=2, pady=10)
        self.delete_supplier_button.grid(row=4, column=7, columnspan=2, pady=10)
        self.search_supplier_button.grid(row=4, column=9, columnspan=2, pady=10)
        
        # Treeview for displaying suppliers
        self.supplier_tree = ttk.Treeview(self.supplier_tab, columns=("ID", "Name", "Address", "Contact Details"), show="headings")
        self.supplier_tree.heading("ID", text="ID")
        self.supplier_tree.heading("Name", text="Name")
        self.supplier_tree.heading("Address", text="Address")
        self.supplier_tree.heading("Contact Details", text="Contact Details")
    
        # Scrollbar for supplier treeview
        vsb = ttk.Scrollbar(self.supplier_tab, orient="vertical", command=self.supplier_tree.yview)
        self.supplier_tree.configure(yscrollcommand=vsb.set)
    
        # Grid layout for supplier treeview
        self.supplier_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
    
    def create_venue_gui(self):
        # Create the GUI container for venue management
        self.venue_crud_container = tk.Frame(self.venue_tab)
        self.venue_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Labels for venue attributes
        self.venue_id_label = tk.Label(self.venue_crud_container, text="Venue ID:")
        self.venue_name_label = tk.Label(self.venue_crud_container, text="Name:")
        self.venue_address_label = tk.Label(self.venue_crud_container, text="Address:")
        self.venue_contact_label = tk.Label(self.venue_crud_container, text="Contact:")
        self.venue_min_guests_label = tk.Label(self.venue_crud_container, text="Min Guests:")
        self.venue_max_guests_label = tk.Label(self.venue_crud_container, text="Max Guests:")
    
        # Entry fields for venue attributes
        self.venue_id_entry = tk.Entry(self.venue_crud_container)
        self.venue_name_entry = tk.Entry(self.venue_crud_container)
        self.venue_address_entry = tk.Entry(self.venue_crud_container)
        self.venue_contact_entry = tk.Entry(self.venue_crud_container)
        self.venue_min_guests_entry = tk.Entry(self.venue_crud_container)
        self.venue_max_guests_entry = tk.Entry(self.venue_crud_container)
    
        # Buttons for venue management
        self.create_venue_button = tk.Button(self.venue_crud_container, text="Create Venue", command=self.create_venue)
        self.read_venue_button = tk.Button(self.venue_crud_container, text="Read Venues", command=self.read_venues)
        self.update_venue_button = tk.Button(self.venue_crud_container, text="Update Venue", command=self.update_venue)
        self.delete_venue_button = tk.Button(self.venue_crud_container, text="Delete Venue", command=self.delete_venue)
        self.search_venue_button = tk.Button(self.venue_crud_container, text="Search Venue", command=self.search_venue)
    
        # Grid layout for venue management components
        self.venue_id_label.grid(row=0, column=0, sticky="e")
        self.venue_name_label.grid(row=1, column=0, sticky="e")
        self.venue_address_label.grid(row=2, column=0, sticky="e")
        self.venue_contact_label.grid(row=3, column=0, sticky="e")
        self.venue_min_guests_label.grid(row=4, column=0, sticky="e")
        self.venue_max_guests_label.grid(row=5, column=0, sticky="e")
    
        self.venue_id_entry.grid(row=0, column=1, pady=5)
        self.venue_name_entry.grid(row=1, column=1, pady=5)
        self.venue_address_entry.grid(row=2, column=1, pady=5)
        self.venue_contact_entry.grid(row=3, column=1, pady=5)
        self.venue_min_guests_entry.grid(row=4, column=1, pady=5)
        self.venue_max_guests_entry.grid(row=5, column=1, pady=5)
    
        self.create_venue_button.grid(row=6, column=1, columnspan=2, pady=10)
        self.read_venue_button.grid(row=6, column=3, columnspan=2, pady=10)
        self.update_venue_button.grid(row=6, column=5, columnspan=2, pady=10)
        self.delete_venue_button.grid(row=6, column=7, columnspan=2, pady=10)
        self.search_venue_button.grid(row=6, column=9, columnspan=2, pady=10)
        
        # Treeview for displaying venues
        self.venue_tree = ttk.Treeview(self.venue_tab, columns=("ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"), show="headings")
        for col in self.venue_tree["columns"]:
            self.venue_tree.heading(col, text=col)
        
        # Set column widths
        column_width = 100 
        for col in self.venue_tree["columns"]:
            self.venue_tree.column(col, width=column_width, minwidth=column_width)
        
        # Scrollbar for venue treeview
        vsb = ttk.Scrollbar(self.venue_tab, orient="vertical", command=self.venue_tree.yview)
        self.venue_tree.configure(yscrollcommand=vsb.set)
    
        # Grid layout for venue treeview
        self.venue_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
    
    def create_event_supplier_gui(self):
        # Create the GUI container for event supplier management
        self.event_supplier_crud_container = tk.Frame(self.event_supplier_tab)
        self.event_supplier_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Labels for event supplier attributes
        tk.Label(self.event_supplier_crud_container, text="Event Supplier ID:").grid(row=0, column=0, sticky="e")
        tk.Label(self.event_supplier_crud_container, text="Event ID:").grid(row=1, column=0, sticky="e")
        tk.Label(self.event_supplier_crud_container, text="Supplier ID:").grid(row=2, column=0, sticky="e")
    
        # Entry fields for event supplier attributes
        self.event_supplier_id_entry = tk.Entry(self.event_supplier_crud_container)
        self.event_supplier_id_entry.grid(row=0, column=1, pady=5)
        self.event_id_entry = ttk.Combobox(self.event_supplier_crud_container, state="readonly", values=self.event_id_values)
        self.event_id_entry.grid(row=1, column=1, pady=5)
        self.supplier_id_entry = ttk.Combobox(self.event_supplier_crud_container, state="readonly", values=self.supplier_id_values)
        self.supplier_id_entry.grid(row=2, column=1, pady=5)
    
        # Populate dropdowns
        self.populate_event_id_dropdown()
        self.populate_supplier_id_dropdown()
    
        # Buttons for event supplier management
        tk.Button(self.event_supplier_crud_container, text="Create Event Supplier", command=self.create_event_supplier).grid(row=3, column=1, columnspan=2, pady=10)
        tk.Button(self.event_supplier_crud_container, text="Read Event Suppliers", command=self.read_event_suppliers).grid(row=3, column=3, columnspan=2, pady=10)
        tk.Button(self.event_supplier_crud_container, text="Update Event Supplier", command=self.update_event_supplier).grid(row=3, column=5, columnspan=2, pady=10)
        tk.Button(self.event_supplier_crud_container, text="Delete Event Supplier", command=self.delete_event_supplier).grid(row=3, column=7, columnspan=2, pady=10)
    
        # Treeview for displaying event suppliers
        self.event_supplier_tree = ttk.Treeview(self.event_supplier_tab, columns=("Event Supplier ID", "Event ID", "Supplier ID"), show="headings")
    
        # Set column headings
        for col in self.event_supplier_tree["columns"]:
            self.event_supplier_tree.heading(col, text=col)
    
        # Set column widths
        column_width = 100
        for col in self.event_supplier_tree["columns"]:
            self.event_supplier_tree.column(col, width=column_width, minwidth=column_width)
    
        # Scrollbar for event supplier treeview
        vsb = ttk.Scrollbar(self.event_supplier_tab, orient="vertical", command=self.event_supplier_tree.yview)
        self.event_supplier_tree.configure(yscrollcommand=vsb.set)
    
        # Grid layout for event supplier treeview
        self.event_supplier_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
    
    def create_event_guest_gui(self):
        # Create the GUI container for event guest management
        self.event_guest_crud_container = tk.Frame(self.event_guest_tab)
        self.event_guest_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Labels for event guest attributes
        tk.Label(self.event_guest_crud_container, text="Event Guest ID:").grid(row=0, column=0, sticky="e")
        tk.Label(self.event_guest_crud_container, text="Event ID:").grid(row=1, column=0, sticky="e")
        tk.Label(self.event_guest_crud_container, text="Guest ID:").grid(row=2, column=0, sticky="e")
    
        # Entry fields for event guest attributes
        self.event_guest_id_entry = tk.Entry(self.event_guest_crud_container)
        self.event_guest_id_entry.grid(row=0, column=1, pady=5)
        self.event_id_entry = ttk.Combobox(self.event_guest_crud_container, state="readonly", values=self.event_id_values)
        self.event_id_entry.grid(row=1, column=1, pady=5)
        self.guest_id_entry = ttk.Combobox(self.event_guest_crud_container, state="readonly", values=self.guest_id_values)
        self.guest_id_entry.grid(row=2, column=1, pady=5)
    
        # Populate dropdowns
        self.populate_event_id_dropdown()
        self.populate_guest_id_dropdown()
    
        # Buttons for event guest management
        tk.Button(self.event_guest_crud_container, text="Create Event Guest", command=self.create_event_guest).grid(row=3, column=1, columnspan=2, pady=10)
        tk.Button(self.event_guest_crud_container, text="Read Event Guests", command=self.read_event_guests).grid(row=3, column=3, columnspan=2, pady=10)
        tk.Button(self.event_guest_crud_container, text="Update Event Guest", command=self.update_event_guest).grid(row=3, column=5, columnspan=2, pady=10)
        tk.Button(self.event_guest_crud_container, text="Delete Event Guest", command=self.delete_event_guest).grid(row=3, column=7, columnspan=2, pady=10)
    
        # Treeview for displaying event guests
        self.event_guest_tree = ttk.Treeview(self.event_guest_tab, columns=("Event Guest ID", "Event ID", "Guest ID"), show="headings")
    
        # Set column headings
        for col in self.event_guest_tree["columns"]:
            self.event_guest_tree.heading(col, text=col)
    
        # Set column widths
        column_width = 100
        for col in self.event_guest_tree["columns"]:
            self.event_guest_tree.column(col, width=column_width, minwidth=column_width)
    
        # Scrollbar for event guest treeview
        vsb = ttk.Scrollbar(self.event_guest_tab, orient="vertical", command=self.event_guest_tree.yview)
        self.event_guest_tree.configure(yscrollcommand=vsb.set)
    
        # Grid layout for event guest treeview
        self.event_guest_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
        
    
    def create_employee_gui(self):
        # Employee CRUD Container
        self.employee_crud_container = tk.Frame(self.employee_tab)
        self.employee_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Populate Manager ID dropdown
        self.populate_manager_id_dropdown()
        
        # Employee Labels
        self.emp_id_label = tk.Label(self.employee_crud_container, text="Employee ID:")
        self.name_label = tk.Label(self.employee_crud_container, text="Name:")
        self.department_label = tk.Label(self.employee_crud_container, text="Department:")
        self.job_title_label = tk.Label(self.employee_crud_container, text="Job Title:")
        self.basic_salary_label = tk.Label(self.employee_crud_container, text="Basic Salary:")
        self.age_label = tk.Label(self.employee_crud_container, text="Age:")
        self.date_of_birth_label = tk.Label(self.employee_crud_container, text="Date of Birth:")
        self.passport_details_label = tk.Label(self.employee_crud_container, text="Passport Details:")
        self.manager_id_label = tk.Label(self.employee_crud_container, text="Manager ID:")
    
        # Employee Entry Fields
        self.emp_id_entry = tk.Entry(self.employee_crud_container)
        self.name_entry = tk.Entry(self.employee_crud_container)
        self.department_entry = tk.Entry(self.employee_crud_container)
        self.job_title_entry = tk.Entry(self.employee_crud_container)
        self.basic_salary_entry = tk.Entry(self.employee_crud_container)
        self.age_entry = tk.Entry(self.employee_crud_container)
        self.date_of_birth_entry = tk.Entry(self.employee_crud_container)
        self.passport_details_entry = tk.Entry(self.employee_crud_container)
    
        # Manager ID Combobox
        self.manager_id_entry = ttk.Combobox(self.employee_crud_container, state="readonly", values=self.manager_id_values)
        self.manager_id_entry.grid(row=8, column=1)
    
        # Employee Buttons
        self.create_emp_button = tk.Button(self.employee_crud_container, text="Create Employee", command=self.create_employee)
        self.read_emp_button = tk.Button(self.employee_crud_container, text="Read Employees", command=self.read_employees)
        self.update_emp_button = tk.Button(self.employee_crud_container, text="Update Employee", command=self.update_employee)
        self.delete_emp_button = tk.Button(self.employee_crud_container, text="Delete Employee", command=self.delete_employee)
        self.search_emp_button = tk.Button(self.employee_crud_container, text="Search Employee", command=self.search_employee)
    
        # Layout for CRUD elements
        self.emp_id_label.grid(row=0, column=0, sticky="e")
        self.name_label.grid(row=1, column=0, sticky="e")
        self.department_label.grid(row=2, column=0, sticky="e")
        self.job_title_label.grid(row=3, column=0, sticky="e")
        self.basic_salary_label.grid(row=4, column=0, sticky="e")
        self.age_label.grid(row=5, column=0, sticky="e")
        self.date_of_birth_label.grid(row=6, column=0, sticky="e")
        self.passport_details_label.grid(row=7, column=0, sticky="e")
        self.manager_id_label.grid(row=8, column=0, sticky="e")
    
        self.emp_id_entry.grid(row=0, column=1,pady=5)
        self.name_entry.grid(row=1, column=1,pady=5)
        self.department_entry.grid(row=2, column=1,pady=5)
        self.job_title_entry.grid(row=3, column=1,pady=5)
        self.basic_salary_entry.grid(row=4, column=1,pady=5)
        self.age_entry.grid(row=5, column=1,pady=5)
        self.date_of_birth_entry.grid(row=6, column=1,pady=5)
        self.passport_details_entry.grid(row=7, column=1,pady=5)
        self.manager_id_entry.grid(row=8, column=1,pady=5)
    
        self.create_emp_button.grid(row=9, column=1, columnspan=2, pady=10)
        self.read_emp_button.grid(row=9, column=3, columnspan=2,pady=10)
        self.update_emp_button.grid(row=9, column=5, columnspan=2,pady=10)
        self.delete_emp_button.grid(row=9, column=7, columnspan=2,pady=10)
        self.search_emp_button.grid(row=9, column=9, columnspan=2,pady=10)
    
        # Treeview to display employees
        self.emp_tree = ttk.Treeview(self.employee_tab, columns=("ID", "Name", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details", "Manager ID"), show="headings")
    
        # Set column headings
        for col in self.emp_tree["columns"]:
            self.emp_tree.heading(col, text=col)
    
        # Set column widths
        column_width = 100  # Adjust this value as needed
        for col in self.emp_tree["columns"]:
            self.emp_tree.column(col, width=column_width, minwidth=column_width)
    
        # Scrollbar
        vsb = ttk.Scrollbar(self.employee_tab, orient="vertical", command=self.emp_tree.yview)
        self.emp_tree.configure(yscrollcommand=vsb.set)
    
        # Grid treeview
        self.emp_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
        # Grid scrollbar
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
    
    
    def create_client_gui(self):
        # Client CRUD Container
        self.client_crud_container = tk.Frame(self.client_tab)
        self.client_crud_container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
        # Client Labels
        self.client_id_label = tk.Label(self.client_crud_container, text="Client ID:")
        self.client_name_label = tk.Label(self.client_crud_container, text="Name:")
        self.client_address_label = tk.Label(self.client_crud_container, text="Address:")
        self.client_contact_label = tk.Label(self.client_crud_container, text="Contact:")
        self.client_budget_label = tk.Label(self.client_crud_container, text="Budget:")
    
        # Client Entry Fields
        self.client_id_entry = tk.Entry(self.client_crud_container)
        self.client_name_entry = tk.Entry(self.client_crud_container)
        self.client_address_entry = tk.Entry(self.client_crud_container)
        self.client_contact_entry = tk.Entry(self.client_crud_container)
        self.client_budget_entry = tk.Entry(self.client_crud_container)
    
        # Client Buttons
        self.create_client_button = tk.Button(self.client_crud_container, text="Create Client", command=self.create_client)
        self.read_client_button = tk.Button(self.client_crud_container, text="Read Clients", command=self.read_clients)
        self.update_client_button = tk.Button(self.client_crud_container, text="Update Client", command=self.update_client)
        self.delete_client_button = tk.Button(self.client_crud_container, text="Delete Client", command=self.delete_client)
        self.search_client_button = tk.Button(self.client_crud_container, text="Search Client", command=self.search_client)
    
        # Layout for CRUD elements
        self.client_id_label.grid(row=0, column=0, sticky="e")
        self.client_name_label.grid(row=1, column=0, sticky="e")
        self.client_address_label.grid(row=2, column=0, sticky="e")
        self.client_contact_label.grid(row=3, column=0, sticky="e")
        self.client_budget_label.grid(row=4, column=0, sticky="e")
    
        self.client_id_entry.grid(row=0, column=1,pady=5)
        self.client_name_entry.grid(row=1, column=1,pady=5)
        self.client_address_entry.grid(row=2, column=1,pady=5)
        self.client_contact_entry.grid(row=3, column=1,pady=5)
        self.client_budget_entry.grid(row=4, column=1,pady=5)
    
        self.create_client_button.grid(row=5, column=1, columnspan=2, pady=10)
        self.read_client_button.grid(row=5, column=3, columnspan=2, pady=10)
        self.update_client_button.grid(row=5, column=5, columnspan=2, pady=10)
        self.delete_client_button.grid(row=5, column=7, columnspan=2, pady=10)
        self.search_client_button.grid(row=5, column=9, columnspan=2, pady=10)
    
        # Treeview to display clients
        self.client_tree = ttk.Treeview(self.client_tab, columns=("ID", "Name", "Address", "Contact", "Budget"), show="headings")
        self.client_tree.heading("ID", text="ID")
        self.client_tree.heading("Name", text="Name")
        self.client_tree.heading("Address", text="Address")
        self.client_tree.heading("Contact", text="Contact")
        self.client_tree.heading("Budget", text="Budget")
        
        # Scrollbar
        vsb = ttk.Scrollbar(self.client_tab, orient="vertical", command=self.client_tree.yview)
        self.client_tree.configure(yscrollcommand=vsb.set)
    
        # Layout for tree view
        self.client_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        vsb.grid(row=1, column=1, padx=5, pady=10, sticky="ns")
        
    def populate_manager_id_dropdown(self):
        """Populates the manager ID dropdown with existing employee IDs."""
        manager_ids = [employee.emp_id for employee in self.employee_management.employees]
        self.manager_id_values = manager_ids   
    
    def create_employee(self):
        """Creates a new employee with the provided details."""
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()
        age = self.age_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()
        manager_id = self.manager_id_entry.get()
    
        # Validation
        if not emp_id or not name or not department or not job_title or not basic_salary or not age or not date_of_birth or not passport_details:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        try:
            emp_id = int(emp_id)
            basic_salary = float(basic_salary)
            age = int(age)
            if manager_id:
                manager_id = int(manager_id)
        except ValueError:
            messagebox.showerror("Error", "Invalid data type for numeric fields.")
            return
    
        self.employee_management.create_employee(emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)
    
    def read_employees(self):
        """Reads and displays all existing employees."""
        for record in self.emp_tree.get_children():
            self.emp_tree.delete(record)
    
        for employee in self.employee_management.employees:
            self.emp_tree.insert("", "end", values=(employee.emp_id, employee.name, employee.department, employee.job_title, employee.basic_salary, employee.age, employee.date_of_birth, employee.passport_details, employee.manager_id))
    
    def update_employee(self):
        """Updates details of an existing employee."""
        emp_id = int(self.emp_id_entry.get())
        name = self.name_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = float(self.basic_salary_entry.get())
        age = int(self.age_entry.get())
        date_of_birth = self.date_of_birth_entry.get()  
        passport_details = self.passport_details_entry.get()
        manager_id = int(self.manager_id_entry.get()) if self.manager_id_entry.get() else None
        self.employee_management.update_employee(emp_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)
    
    def delete_employee(self):
        """Deletes an employee based on the provided ID."""
        emp_id = int(self.emp_id_entry.get())
        if not emp_id:
            messagebox.showerror("Error", "Please enter an employee ID.")
            return
        self.employee_management.delete_employee(emp_id)
    
    def search_employee(self):
        """Searches for an employee based on the provided ID."""
        emp_id = self.emp_id_entry.get()
        if not emp_id:
            messagebox.showerror("Error", "Please enter an employee ID.")
            return
        employee = self.employee_management.search_employee(int(emp_id))
        
        for record in self.emp_tree.get_children():
            self.emp_tree.delete(record)
        if employee:
            # Insert searched employee data into the tree
            self.emp_tree.insert("", "end", values=(employee.emp_id, employee.name, employee.department, employee.job_title, employee.basic_salary, employee.age, employee.date_of_birth, employee.passport_details, employee.manager_id))
        else:
            messagebox.showerror("Error", "Employee not found.")
    
    def create_client(self):
        """Creates a new client with the provided details."""
        client_id = self.client_id_entry.get()
        name = self.client_name_entry.get()
        address = self.client_address_entry.get()
        contact = self.client_contact_entry.get()
        budget = self.client_budget_entry.get()
    
        # Validation
        if not client_id or not name or not address or not contact or not budget:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        self.client_management.create_client(client_id, name, address, contact, budget)
    
    def read_clients(self):
        """Reads and displays all existing clients."""
        for record in self.client_tree.get_children():
            self.client_tree.delete(record)
    
        for client in self.client_management.clients:
            self.client_tree.insert("", "end", values=(client.client_id, client.name, client.address, client.contact, client.budget))
    
    def update_client(self):
        """Updates details of an existing client."""
        client_id = self.client_id_entry.get()
        name = self.client_name_entry.get()
        address = self.client_address_entry.get()
        contact = self.client_contact_entry.get()
        budget = self.client_budget_entry.get()
        self.client_management.update_client(client_id, name, address, contact, budget)
    
    def delete_client(self):
        """Deletes a client based on the provided ID."""
        client_id = self.client_id_entry.get()
        if not client_id:
            messagebox.showerror("Error", "Please enter a client ID.")
            return
        self.client_management.delete_client(client_id)
        
    def search_client(self):
        """Searches for a client based on the provided ID."""
        client_id = self.client_id_entry.get()
        if not client_id:
            messagebox.showerror("Error", "Please enter a Client ID.")
            return
        client = self.client_management.search_client(int(client_id))
        # Clear existing data in the tree
        for record in self.client_tree.get_children():
            self.client_tree.delete(record)
        # Insert searched client data into the tree
        if client:
            self.client_tree.insert("", "end", values=(client.client_id, client.name, client.address, client.contact,client.budget))
        else:
            messagebox.showerror("Error", "Client not found.")
    
    def create_venue(self):
        """Creates a new venue with the provided details."""
        venue_id = self.venue_id_entry.get()
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contact = self.venue_contact_entry.get()
        min_guests = self.venue_min_guests_entry.get()
        max_guests = self.venue_max_guests_entry.get()
    
        # Validation
        if not venue_id or not name or not address or not contact or not min_guests or not max_guests:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        self.venue_management.create_venue(venue_id, name, address, contact, min_guests, max_guests)
    
    def read_venues(self):
        """Reads and displays all existing venues."""
        for record in self.venue_tree.get_children():
            self.venue_tree.delete(record)
    
        for venue in self.venue_management.venues:
            self.venue_tree.insert("", "end", values=(venue.venue_id, venue.name, venue.address, venue.contact, venue.min_guests, venue.max_guests))
    
    def update_venue(self):
        """Updates details of an existing venue."""
        venue_id = self.venue_id_entry.get()
        name = self.venue_name_entry.get()
        address = self.venue_address_entry.get()
        contact = self.venue_contact_entry.get()
        min_guests = self.venue_min_guests_entry.get()
        max_guests = self.venue_max_guests_entry.get()
        self.venue_management.update_venue(venue_id, name, address, contact, min_guests, max_guests)
    
    def delete_venue(self):
        """Deletes a venue based on the provided ID."""
        venue_id = self.venue_id_entry.get()
        if not venue_id:
            messagebox.showerror("Error", "Please enter a venue ID.")
            return
        self.venue_management.delete_venue(venue_id)
        
    def search_venue(self):
        """Searches for a venue based on the provided ID."""
        venue_id = self.venue_id_entry.get()
        if not venue_id:
            messagebox.showerror("Error", "Please enter a Venue ID.")
            return
        venue = self.venue_management.search_venue(int(venue_id))
        for record in self.venue_tree.get_children():
            self.venue_tree.delete(record)
        if venue:
            self.venue_tree.insert("", "end", values=(venue.venue_id, venue.name, venue.address, venue.contact, venue.min_guests, venue.max_guests))
        else:
            messagebox.showerror("Error", "Venue not found.")
            
    def create_guest(self):
        """Creates a new guest with the provided details."""
        guest_id = self.guest_id_entry.get()
        name = self.guest_name_entry.get()
        address = self.guest_address_entry.get()
        contact_details = self.guest_contact_entry.get()
    
        # Validation
        if not guest_id or not name or not address or not contact_details:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        self.guest_management.create_guest(guest_id, name, address, contact_details)
    
    
    def read_guests(self):
        """Reads and displays all existing guests."""
        for record in self.guest_tree.get_children():
            self.guest_tree.delete(record)
    
        for guest in self.guest_management.guests:
            self.guest_tree.insert("", "end", values=(guest.guest_id, guest.name, guest.address, guest.contact_details))
    
    def update_guest(self):
        """Updates details of an existing guest."""
        guest_id = self.guest_id_entry.get()
        name = self.guest_name_entry.get()
        address = self.guest_address_entry.get()
        contact_details = self.guest_contact_entry.get()
        self.guest_management.update_guest(guest_id, name, address, contact_details)
    
    def delete_guest(self):
        """Deletes a guest based on the provided ID."""
        guest_id = self.guest_id_entry.get()
        self.guest_management.delete_guest(guest_id)
        
    def search_guest(self):
        """Searches for a guest based on the provided ID."""
        guest_id = self.guest_id_entry.get()
        if not guest_id:
            messagebox.showerror("Error", "Please enter a Guest ID.")
            return
        guest = self.guest_management.search_guest(int(guest_id))
        # Clear existing data in the tree
        for record in self.guest_tree.get_children():
            self.guest_tree.delete(record)
        if guest:
            # Insert searched guest data into the tree
            self.guest_tree.insert("", "end", values=(guest.guest_id, guest.name, guest.address, guest.contact_details))
        else:
            messagebox.showerror("Error", "Guest not found.")
    
    def create_supplier(self):
        """Creates a new supplier with the provided details."""
        supplier_id = self.supplier_id_entry.get()
        name = self.supplier_name_entry.get()
        address = self.supplier_address_entry.get()
        contact_details = self.supplier_contact_entry.get()
    
        # Validation
        if not supplier_id or not name or not address or not contact_details:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        self.supplier_management.create_supplier(supplier_id, name, address, contact_details)
    
    
    def read_suppliers(self):
        """Reads and displays all existing suppliers."""
        for record in self.supplier_tree.get_children():
            self.supplier_tree.delete(record)
    
        for supplier in self.supplier_management.suppliers:
            self.supplier_tree.insert("", "end", values=(supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details))
    
    def update_supplier(self):
        """Updates details of an existing supplier."""
        supplier_id = self.supplier_id_entry.get()
        name = self.supplier_name_entry.get()
        address = self.supplier_address_entry.get()
        contact_details = self.supplier_contact_entry.get()
        self.supplier_management.update_supplier(supplier_id, name, address, contact_details)
    
    def delete_supplier(self):
        """Deletes a supplier based on the provided ID."""
        supplier_id = self.supplier_id_entry.get()
        self.supplier_management.delete_supplier(supplier_id)
        
    def search_supplier(self):
        """Searches for a supplier based on the provided ID."""
        supplier_id = self.supplier_id_entry.get()
        if not supplier_id:
            messagebox.showerror("Error", "Please enter a Supplier ID.")
            return
        supplier = self.supplier_management.search_supplier(int(supplier_id))
        for record in self.supplier_tree.get_children():
            self.supplier_tree.delete(record)
        if supplier:
            self.supplier_tree.insert("", "end", values=(supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details))
        else:
            messagebox.showerror("Error", "Supplier not found.")
    
    def populate_venue_client_ids(self):
        """Populates venue and client ID dropdowns with existing IDs."""
        # Retrieve venue IDs from VenueManagementSystem
        venue_ids = [venue.venue_id for venue in self.venue_management.venues]
        # Populate the venue_id dropdown with retrieved venue IDs
        self.venue_id_entry['values'] = venue_ids
    
        # Retrieve client IDs from ClientManagementSystem
        client_ids = [client.client_id for client in self.client_management.clients]
        # Populate the client_id dropdown with retrieved client IDs
        self.client_id_entry['values'] = client_ids
    
    def create_event(self):
        """Creates a new event with the provided details."""
        # Retrieve data from entry fields
        event_id = self.event_id_entry.get()
        event_type = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_id = self.venue_id_entry.get()
        client_id = self.client_id_entry.get()
        estimated_cost = self.estimated_cost_entry.get()
        actual_cost = self.actual_cost_entry.get()
        status = self.status_entry.get()
        invoice = self.invoice_entry.get()
    
        # Validation
        if not event_id or not event_type or not theme or not date or not time or not duration or not venue_id or not client_id or not estimated_cost or not actual_cost or not status or not invoice:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        # Call create_event method of EventManagementSystem
        self.event_management.create_event(event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice)
    
    def read_events(self):
        """Reads and displays all existing events."""
        for item in self.event_tree.get_children():
            self.event_tree.delete(item)
    
        events = self.event_management.events
    
        for index, event in enumerate(events, start=1):
            self.event_tree.insert("", "end", values=(
                event.event_id,
                event.event_type,
                event.theme,
                event.date,
                event.time,
                event.duration,
                event.venue_id,
                event.client_id,
                event.estimated_cost,
                event.actual_cost,
                event.status,
                event.invoice
            ))
    
    def update_event(self):
        """Updates details of an existing event."""
        # Retrieve data from entry fields
        event_id = self.event_id_entry.get()
        event_type = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_id = self.venue_id_entry.get()
        client_id = self.client_id_entry.get()
        estimated_cost = self.estimated_cost_entry.get()
        actual_cost = self.actual_cost_entry.get()
        status = self.status_entry.get()
        invoice = self.invoice_entry.get()
    
        # Call update_event method of EventManagementSystem
        self.event_management.update_event(event_id, event_type, theme, date, time, duration, venue_id, client_id, estimated_cost, actual_cost, status, invoice)
    
    def delete_event(self):
        """Deletes an event based on the provided ID."""
        event_id = self.event_id_entry.get()
    
        # Call delete_event method of EventManagementSystem
        self.event_management.delete_event(event_id)
    
    def search_event(self):
        """Searches for an event based on the provided ID."""
        event_id = self.event_id_entry.get()
        if not event_id:
            messagebox.showerror("Error", "Please enter an Event ID.")
            return
        event = self.event_management.search_event(int(event_id))
        # Clear existing data in the tree
        for record in self.event_tree.get_children():
            self.event_tree.delete(record)
        if event:
            self.event_tree.insert("", "end", values=(event.event_id, event.event_type, event.theme, event.date, event.time, event.duration, event.venue_id, event.client_id, event.estimated_cost, event.actual_cost, event.status, event.invoice))
        else:
            messagebox.showerror("Error", "Event not found.")
    
    def create_event_supplier(self):
        """Creates a new event supplier relationship with the provided details."""
        event_supplier_id = self.event_supplier_id_entry.get()
        event_id = self.event_id_entry.get()
        supplier_id = self.supplier_id_entry.get()
    
        # Validation
        if not event_supplier_id or not event_id or not supplier_id:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        # Call create_event_supplier method of EventSupplierManagementSystem
        self.event_supplier_management.create_event_supplier(event_supplier_id, event_id, supplier_id)
    
    
    def read_event_suppliers(self):
        """Reads and displays all existing event suppliers."""
        # Clear existing items in Treeview
        for item in self.event_supplier_tree.get_children():
            self.event_supplier_tree.delete(item)
    
        # Retrieve event suppliers from EventSupplierManagementSystem
        event_suppliers = self.event_supplier_management.event_suppliers
    
        # Populate Treeview with event suppliers
        for event_supplier in event_suppliers:
            self.event_supplier_tree.insert("", "end", values=(
                event_supplier.id,
                event_supplier.event_id,
                event_supplier.supplier_id
            ))
    
    def update_event_supplier(self):
        """Updates details of an existing event supplier relationship."""
        # Retrieve data from entry fields
        event_supplier_id = self.event_supplier_id_entry.get()
        event_id = self.event_id_entry.get()
        supplier_id = self.supplier_id_entry.get()
    
        # Call update_event_supplier method of EventSupplierManagementSystem
        self.event_supplier_management.update_event_supplier(event_supplier_id, event_id, supplier_id)
    
    def delete_event_supplier(self):
        """Deletes an event supplier relationship based on the provided ID."""
        # Retrieve event supplier ID from entry field
        event_supplier_id = self.event_supplier_id_entry.get()
    
        # Call delete_event_supplier method of EventSupplierManagementSystem
        self.event_supplier_management.delete_event_supplier(event_supplier_id)
    
    def create_event_guest(self):
        """Creates a new event guest relationship with the provided details."""
        # Retrieve data from entry fields
        event_guest_id = self.event_guest_id_entry.get()
        event_id = self.event_id_entry.get()
        guest_id = self.guest_id_entry.get()
    
        # Validation
        if not event_guest_id or not event_id or not guest_id:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
        # Call create_event_guest method of EventGuestManagementSystem
        self.event_guest_management.create_event_guest(event_guest_id, event_id, guest_id)
    
    
    def read_event_guests(self):
        """Reads and displays all existing event guests."""
        # Clear existing items in Treeview
        for item in self.event_guest_tree.get_children():
            self.event_guest_tree.delete(item)
    
        # Retrieve event guests from EventGuestManagementSystem
        event_guests = self.event_guest_management.event_guests
    
        # Populate Treeview with event guests
        for event_guest in event_guests:
            self.event_guest_tree.insert("", "end", values=(
                event_guest.id,
                event_guest.event_id,
                event_guest.guest_id
            ))
    
    def update_event_guest(self):
        """Updates details of an existing event guest relationship."""
        # Retrieve data from entry fields
        event_guest_id = self.event_guest_id_entry.get()
        event_id = self.event_id_entry.get()
        guest_id = self.guest_id_entry.get()
    
        # Call update_event_guest method of EventGuestManagementSystem
        self.event_guest_management.update_event_guest(event_guest_id, event_id, guest_id)
    
    def delete_event_guest(self):
        """Deletes an event guest relationship based on the provided ID."""
        # Retrieve event guest ID from entry field
        event_guest_id = self.event_guest_id_entry.get()
    
        # Call delete_event_guest method of EventGuestManagementSystem
        self.event_guest_management.delete_event_guest(event_guest_id)
    
    def populate_event_id_dropdown(self):
        """Populates the event ID dropdown with existing IDs."""
        # Retrieve event IDs from EventManagementSystem
        event_ids = [event.event_id for event in self.event_management.events]
        
        # Populate the event_id dropdown with retrieved event IDs
        self.event_id_entry['values'] = event_ids
    
    def populate_supplier_id_dropdown(self):
        """Populates the supplier ID dropdown with existing IDs."""
        # Retrieve supplier IDs from SupplierManagementSystem
        supplier_ids = [supplier.supplier_id for supplier in self.supplier_management.suppliers]
        
        # Populate the supplier_id dropdown with retrieved supplier IDs
        self.supplier_id_entry['values'] = supplier_ids
    
    def populate_guest_id_dropdown(self):
        """Populates the guest ID dropdown with existing IDs."""
        # Retrieve guest IDs from GuestManagementSystem
        guest_ids = [guest.guest_id for guest in self.guest_management.guests]
        
        # Populate the guest_id dropdown with retrieved guest IDs
        self.guest_id_entry['values'] = guest_ids

    

root = tk.Tk()
root.title("Best Events Company")
app = ManagementGUI(root)
root.mainloop()


# In[ ]:





# In[ ]:




