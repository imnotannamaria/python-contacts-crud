from contact import Contact

contact_id = 0
contact_list = []

def should_end_program():
  print("Do you want to exit the program?\n"
        "1 - Yes\n"
        "2 - No\n")

  end_program_choice = input("Choose an option: ")

  if end_program_choice == "1":
    end_program()
  elif end_program_choice == "2":
    return
  else:
    print("Invalid option. Please choose a valid option.\n")
    should_end_program()

def end_program():
  print("Exiting program...")
  exit()

while True:
    print("Hello, ✨\n"
          "Welcome to Contacts CRUD\n"   
          "1 - Add a contact\n"
          "2 - View the list of registered contacts\n"
          "3 - Edit a contact\n"
          "4 - Mark a contact as a favorite\n"
          "5 - Unmark a contact as a favorite\n"
          "6 - View a list of favorite contacts\n"
          "7 - Delete a contact\n"
          "8 - Exit")

    menu_choice = input("Choose an option from the menu above: ")

    if menu_choice == "1":
        contact_id += 1
        name = input("Tell me, whats the contact name?! ")
        email = input("And the contact email?!  ")
        phone = input("Phone number?!  ")
        favorite = input("Is the contact a favorite? (y/n) ")

        if favorite == "y":
          favorite = True
        else:
          favorite = False

        contact_list.append(Contact(contact_id, name, email, phone, favorite))
        print("Contact added!\n")

        should_end_program()
    elif menu_choice == "2":
        if contact_list:
            for contact in contact_list:
                print("Id:", contact.id, "| Name:", contact.name, "| E-mail:", contact.email, "| Phone:", contact.phone, "| Is Favorite:", contact.favorite, "\n")
        else:
            print("Contact list is empty.\n")

        should_end_program()
    elif menu_choice == "3":
      contact_id_to_edit = input("Choose the ID of the contact you want to edit: ")

      contact_to_edit = 0

      for contact in contact_list:
        if contact.id == int(contact_id_to_edit):
          contact_to_edit = contact
          break
      
      if contact_to_edit:
        name = input("Tell me, what's the new contact name? ")
        email = input("And the new contact email? ")
        phone = input("New phone number? ")
        favorite = input("Is the contact a favorite? (y/n) ")

        if favorite == "y":
          favorite = True
        else:
          favorite = False
        
        contact_to_edit.name = name
        contact_to_edit.email = email
        contact_to_edit.phone = phone
        contact_to_edit.favorite = favorite
        
        print("Contact updated!")
      else:
        print("Contact with ID", contact_id_to_edit, "not found.")

      should_end_program()
    elif menu_choice == "4":
      contact_id_to_edit = input("Choose the ID of the contact you want to edit: ")

      contact_to_edit = 0

      for contact in contact_list:
        if contact.id == int(contact_id_to_edit):
          contact_to_edit = contact
          break
      
      if contact_to_edit:
        contact_to_edit.favorite = True
        
        print("Contact Marked as favorite!")
      else:
        print("Contact with ID", contact_id_to_edit, "not found.")

      should_end_program()
    elif menu_choice == "5":
      contact_id_to_edit = input("Choose the ID of the contact you want to edit: ")

      contact_to_edit = 0

      for contact in contact_list:
        if contact.id == int(contact_id_to_edit):
          contact_to_edit = contact
          break
      
      if contact_to_edit:
        contact_to_edit.favorite = False
        
        print("Contact Unmarked as favorite!")
    elif menu_choice == "6":
      if contact_list:
        print("Favorite Contacts:")
        for contact in contact_list:
          if contact.favorite:
            print("Id:", contact.id, "| Name:", contact.name, "| E-mail:", contact.email, "| Phone:", contact.phone, "| Is Favorite:", contact.favorite, "\n")
      else:
        print("Contact list is empty.\n")
      should_end_program()
    elif menu_choice == "7":
      contact_id_to_edit = input("Choose the ID of the contact you want to delete: ")

      contact_to_edit = 0

      for contact in contact_list:
        if contact.id == int(contact_id_to_edit):
          contact_to_edit = contact
          break
      
      if contact_to_edit:
        contact_list.remove(contact_to_edit)
        print("Contact Deleted!")
    elif menu_choice == "8":
      end_program()
    else:
      print("Invalid option. Please choose a valid option.\n")
      should_end_program()


