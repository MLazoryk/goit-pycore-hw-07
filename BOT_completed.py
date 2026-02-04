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
        



if __name__ == "__main__":
    # Run the main program
    main()