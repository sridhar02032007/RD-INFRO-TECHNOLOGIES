contacts=[]

def add_contact():
    name= input("enter name:")
    phone=input("enter phone number:")
    email=input("enter email:")
    address=input("enter address:")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("no contacts found.\n")
    else:
        print("\n---contact list ---")
        for i,contact in enumerate(contacts,start=1):
            print(f"{i}.{contact['name']} - {contact['phone']}")
        print()

def search_contact():
    query=input("enter name or phone number to search")
    found = False
    for contact in contacts:
        if contact["name"]==query or contact ["phone"] == query:
            print("\n--- contact found---")
            print(f"name: {contact['name']}")
            print(f"phone:{contact['phone']}")
            print(f"email:{contact['email']}")
            print(f"address:{contact['address']}\n")
            found =True
            break
        if not found:
            print("contact not found .")



def update_contact():
    name= input("enter the name of the contact to update:")
    for contact in contacts:
        if contact["name"]==name:
            print("leave field blank to keep current value.")
            new_phone=input(f"enter new phone (current:{contact['phone']}):")or contact['phone']
            new_email=input(f"enter  new email (current:{contact['email']}):")or contact['email']
            new_address=input(f"enter new address (current:{contact['address']}")or contact['address']

            contact["phone"]=new_phone
            contact["email"]=new_email
            contact["address"]=new_address

            print("contact updated successfully.\n")
            return
        print("contact not found.\n")


def delete_contact():
    name =input(" enter the name of the contact to delete:")
    for contact in contacts:
        if contact ["name"]==name:
            contact.remove(contact)
            print("contact deleted success fully.\n")
            return
        print("contact not found")

def main():
    while True:
        print("===contact book ===")
        print("1. add contact")
        print("2. view contact list")
        print("3.search contact")
        print("4. update contact")
        print("5. delete contact")
        print("6. exit")

        choice = input("enter your choice (1-6):")

        if choice =="1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            search_contact()

        elif choice =="4":
            update_contact()

        elif choice =="5":
            delete_contact()

        elif choice =="6":
            print("exiting contact book.good bye!")
            break
        else:
            print("invalid chice .please try again .\n")


if __name__=="__main__":
    main()




































        
            


































            
            
