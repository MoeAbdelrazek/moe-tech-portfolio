# Simple Contact Manager (CLI Application)
# Author: Moe
# Description: A command-line tool to manage contacts using Python fundamentals.
# Skills Used: Variables, Lists, Loops, Conditionals, Functions, String Handling, Error Handling

# Initialize an empty list to store contacts
contacts = []

# Display the main menu options
def show_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

# Add a new contact to the list
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    # Ensure both fields are filled
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        print(f"Contact '{name}' added.")
    else:
        print("Name and phone cannot be empty.")

# Display all saved contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

# Search for a contact by name (case-insensitive)
def search_contact():
    query = input("Enter name to search: ").strip().lower()
    found = False

    for contact in contacts:
        if query in contact['name'].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True

    if not found:
        print("No matching contact found.")

# Delete a contact by exact name match
def delete_contact():
    name_to_delete = input("Enter name to delete: ").strip().lower()

    for contact in contacts:
        if contact['name'].lower() == name_to_delete:
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted.")
            return

    print("Contact not found.")

# Main loop to handle user interaction
def main():
    while True:
        show_menu()

        try:
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                search_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                print("Exiting Contact Manager. Goodbye.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")

# Start the application
main()