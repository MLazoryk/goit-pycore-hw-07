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
        



if __name__ == "__main__":
    # Run the main program
    main()