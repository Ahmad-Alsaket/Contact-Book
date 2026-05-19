import json

def add_contact(contacts):
    
    name = input("add name : ")
    phone = input("add phone number : ")
    email = input("add email : ")
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    
    return contacts
    
    
def list_contacts(contacts):
    for index,contact in enumerate(contacts, start=1):
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        
        print(f"{index}. {name} | {phone} | {email} ")
        
        
        
        
def search_contacts():
    
def delete_contact():
    
def update_contact():
    
    


def load():
    try:
        with open("data.json") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []
    
def save(data):
    try:
        with open("data.json","w") as f:
            json.dump(data,f)  
    except FileNotFoundError:
        print("error file not found")
    
def menu():
    print("\n========= CONTACT BOOK =========")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    return choice
    
def main():
    contacts = load()
    while True:
        choice = menu()
        
        if choice == '1':
            new = add_contact(contacts)
            contacts = new
            
        elif choice == '2':
            list_contacts(contacts)
            
        elif choice == '3':
            search_contacts()
            
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            exit()


if __name__ == "__main__":
    main()
