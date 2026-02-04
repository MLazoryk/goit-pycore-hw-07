"""
📒 CONTACT BOOK BOT WITH BIRTHDAY REMINDERS 
"""

from collections import UserDict
from datetime import datetime, timedelta

# =========================
# ERROR HANDLING DECORATOR
# =========================
def input_error(func):
    def inner (*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except KeyError:
            return "❌ Contact not found."
        except IndexError:
            return "❌ PLease provide all required arguments."
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"
        
    return inner

# =========================
# FIELD CLASSES
# =========================
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone must be 10 digits like 1234567890")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try: 
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Use DD.MM.YYYY format (e.g. 15.03.1990)")
        
# =========================
# RECORD CLASS
# =========================
class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phones(self, phone_number):
        self.phones.append(Phone, phone_number):

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return True
        return False
    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                if not (new_phone.isdigit() and len(new_phone) == 10):
                    raise ValueError("New phone must be 10 digits")
                phone.value = new_phone
                return True
            raise ValueError (f"Phone '{old_phone}' not found")
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
            return None
        
    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        result = f"👤 {self.name.value} | 📱 {phones}" if phones else f"👤 {self.name.value}"
        if self.birthday:
            result += f" | 🎂 {self.birthday}"
        return result

# =========================
# ADDRESS BOOK CLASS
# =========================







if __name__ == "__main__":
    # Run the main program
    main()