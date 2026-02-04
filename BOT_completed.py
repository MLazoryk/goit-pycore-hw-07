from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value         # Store the actual value of the field

    def __str__(self):
        return str(self.value)     # Convert value to string when we print it

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):  # Validate that phone number is exactly 10 digits and all digits
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Birthday(Field):  # NEW CLASS for birthday
    def __init__(self, value):
        try:
            # Convert string like "15.03.1990" to a date object
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")  # Show error if format is wrong

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None  # NEW: Add optional birthday field

    def add_phone(self, phone_number):
        phone = Phone(phone_number)  # Create Phone object with validation
        self.phones.append(phone)    # Add to phones list

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True             # Return True to show removal was successful
        return False                    # Return False if phone wasn't found

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                if not (new_phone.isdigit() and len(new_phone) == 10):  # Check that new phone is 10 digits
                    raise ValueError("New phone number must be 10 digits")
                phone.value = new_phone  # Update the phone number
                return True  # Success
        raise ValueError("Phone number not found")  # Error if old phone not found

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None  # Return None if phone not found

    def add_birthday(self, birthday_str):  # NEW METHOD: Add birthday to contact
        self.birthday = Birthday(birthday_str)  # Create Birthday object with validation

    def __str__(self):
        phone_str = '; '.join(p.value for p in self.phones)  # Join all phones with semicolon
        result = f"Contact name: {self.name.value}, phones: {phone_str}"
        if self.birthday:
            result += f", birthday: {self.birthday}"  # Add birthday if exists
        return result

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # Example: {"John": Record("John")}

    def find(self, name):
        if name in self.data:
            return self.data[name]  # Return Record if found
        return None  # Return None if contact not found

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True  # Success
        return False  # Contact not found

    def get_upcoming_birthdays(self):  # NEW METHOD: Get birthdays in next 7 days
        today = datetime.today().date()
        next_week = today + timedelta(days=7)  # Calculate date 7 days from now
        upcoming_birthdays = []
        
        for record in self.data.values():  # Check each contact
            if record.birthday:
                # Get birthday for current year (replace year with current year)
                birthday_this_year = record.birthday.value.replace(year=today.year)
                
                # If birthday already passed this year, check next year
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                # Check if birthday is within next 7 days
                if today <= birthday_this_year <= next_week:
                    # Adjust for weekends: Saturday(5) → Monday, Sunday(6) → Monday
                    if birthday_this_year.weekday() == 5:  # Saturday
                        congratulation_date = birthday_this_year + timedelta(days=2)
                    elif birthday_this_year.weekday() == 6:  # Sunday
                        congratulation_date = birthday_this_year + timedelta(days=1)
                    else:
                        congratulation_date = birthday_this_year
                    
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                    })
        
        return upcoming_birthdays

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # Try to run the function
        except ValueError as e:
            return f"Error: {str(e)}"  # Return error message
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Invalid number of arguments."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.strip().split()  # Split input into command and arguments
    cmd = cmd.strip().lower()  # Convert command to lowercase
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args  # Get name and phone from arguments
    record = book.find(name)  # Look for existing contact
    message = "Contact updated."
    if record is None:
        record = Record(name)  # Create new Record if not found
        book.add_record(record)  # Add to address book
        message = "Contact added."
    if phone:
        record.add_phone(phone)  # Add phone number
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args[0], args[1], args[2]  # Get all three arguments
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    record.edit_phone(old_phone, new_phone)  # Change phone number
    return "Phone number updated."

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]  # Get name from arguments
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    phone_list = [phone.value for phone in record.phones]  # Extract phone values
    return f"{name}: {', '.join(phone_list)}"

@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    result = []
    for name, record in book.data.items():  # Loop through all contacts
        result.append(str(record))
    return "\n".join(result)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_str = args[0], args[1]  # Get name and birthday
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    record.add_birthday(birthday_str)  # Add birthday to contact
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]  # Get name from arguments
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found")
    if record.birthday:
        return f"{name}'s birthday: {record.birthday}"
    else:
        return f"{name} doesn't have a birthday set."

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()  # Get birthdays in next week
    if not upcoming:
        return "No birthdays in the next week."
    result = ["Upcoming birthdays:"]
    for entry in upcoming:  # Loop through each upcoming birthday
        result.append(f"- {entry['name']}: congratulate on {entry['congratulation_date']}")
    return "\n".join(result)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()