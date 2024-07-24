#task1
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_service_ticket(tickets):
    # Generate a new ticket ID
    ticket_id = f"Ticket{str(len(tickets) + 1).zfill(3)}"
    
    # Collect ticket details from the user
    customer = input("Enter the customer name: ")
    issue = input("Enter the issue description: ")
    status = "open"  # New tickets are initially open

    # Add the new ticket to the dictionary
    tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": status}
    print(f"New ticket {ticket_id} added successfully!")

def update_ticket_status(tickets):
    ticket_id = input("Enter the ticket ID to update: ")
    if ticket_id in tickets:
        new_status = input("Enter the new status (open/closed): ").lower()
        if new_status in ["open", "closed"]:
            tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print("Invalid status. Please enter 'open' or 'closed'.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(tickets):
    filter_status = input("Do you want to filter by status? (yes/no): ").lower()
    if filter_status == "yes":
        status = input("Enter the status to filter by (open/closed): ").lower()
        filtered_tickets = {k: v for k, v in tickets.items() if v["Status"] == status}
        if filtered_tickets:
            for ticket_id, details in filtered_tickets.items():
                print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
        else:
            print(f"No tickets with status '{status}' found.")
    else:
        if tickets:
            for ticket_id, details in tickets.items():
                print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
        else:
            print("No tickets available.")

def main():
    while True:
        print("\nMenu:")
        print("1. Open a new service ticket")
        print("2. Update the status of an existing ticket")
        print("3. Display all tickets or filter by status")
        print("4. Quit")

        try:
            choice = int(input("Select an option (1-4): "))
            if choice == 1:
                add_service_ticket(service_tickets)
            elif choice == 2:
                update_ticket_status(service_tickets)
            elif choice == 3:
                display_tickets(service_tickets)
            elif choice == 4:
                print("Thank you for using the service ticket tracker. Goodbye!")
                break
            else:
                print("Please select a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Returning to menu...")

if __name__ == "__main__":
    main()
