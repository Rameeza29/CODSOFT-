contacts = []
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        while True:
            phone = input("Enter 10-digit phone number: ")
            if len(phone) == 10 and phone.isdigit():
                break
            else:
                print("Invalid! Enter exactly 11 digits.")

        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        print("Contact added!")
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for c in contacts:
                print("\nName:", c["name"])
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                print("Address:", c["address"])
    elif choice == "3":
        search = input("Enter name to search: ").lower()
        found = False
        for c in contacts:
            if c["name"].lower() == search:
                print("\nContact found:")
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                print("Address:", c["address"])
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == "4":
        search = input("Enter name to update: ").lower()
        for c in contacts:
            if c["name"].lower() == search:
                while True:
                    phone = input("New 10-digit phone number: ")
                    if len(phone) == 10 and phone.isdigit():
                        c["phone"] = phone
                        break
                    else:
                        print("Invalid! Enter exactly 11 digits.")

                c["email"] = input("New email: ")
                c["address"] = input("New address: ")
                print("Contact updated!")
                break
        else:
            print("Contact not found.")
    elif choice == "5":
        search = input("Enter name to delete: ").lower()

        for c in contacts:
            if c["name"].lower() == search:
                contacts.remove(c)
                print("Contact deleted!")
                break
        else:
            print("Contact not found.")
    elif choice == "6":
        print("bye...")
        break
    else:
        print("Invalid choice!")