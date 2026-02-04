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
class AddressBook(UserDict):
    """
    Dictionary-like container for all contacts.
    """
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        # Find contact by name.
        return self.data.get(name)
    
    def delete (self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
    
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days = 7)
        upcoming = []

        for record in self.data.values():
            if record.birthdays:
                # Get this yeat's birthday date
                bday_thi_year = record.birthday.value.replace(year = today.year)

                # If birthday already passed, check next year
                if bday_this_year < today:
                    bday_thi_year = bday_thi_year.replace(year=today.year + 1)

                # Check if whithin next 7 day
                if today <= bday_thi_year <= next_week:
                    if bday_thi_year.weekday() == 5: # Saturday
                        congrats_date = bday_thi_year + timedelta(days=2)
                    elif bday_thi_year.weekday() == 6: # Sunday
                        congrats_date = bday_thi_year + timedelta(days=1)
                    else:
                        congrats_date = bday_thi_year

                    upcoming.append({
                        "name": record.name.value,
                        "congratulation_date": congrats_date.strftime("%d.%m.%Y")
                    })
        return upcoming
    
    # =========================
    




if __name__ == "__main__":
    # Run the main program
    main()