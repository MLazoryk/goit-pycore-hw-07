"""
📒 CONTACT BOOK BOT WITH BIRTHDAY REMINDERS 
"""

from collections import UserDict
from datetime import datetime, timedelta
import re

class Stickers: 
    EMOJI = {
        "welcome": "🌟",
        "success": "✅",
        "error": "❌",
        "info": "ℹ️",
        "birthday": "🎂",
        "contact": "👤",
        "phone": "📱",
        "exit": "👋",
        "command": ">",
        "separator": "=" * 50,
        "thin_separator": "-" * 40
    }

    @staticmethod
    def print_welcome():
        """ Display welcome message with decorative border"""
        print(f"\n{Stickers.EMOJI['separator']}")
        print(f"{Stickers.EMOJI['welcome']} WELCOME TO CONTACT BOOK BOT {Stickers.EMOJI['welcome']}")
        print(f"{Stickers.EMOJI['separator']}")
        print(f"{Stickers.EMOJI['info']} Type 'help' to see available commands")
        print(f"{Stickers.EMOJI['separator']}\n")

    @staticmethod
    def print_help():
        print (f"\n{Stickers.EMOJI['Seperator']}")
        print(f"{Stickers.EMOJI['info']} AVAILABLE COMMANDS {Stickers.EMOJI['info']}")
        print(f"{Stickers.EMOJI['seperator']}\n")

    commands = [
        (f"add [name] [phone]", "Add new contact or phone to existing"),
        (f"change [name] [old] [new]", "Change phone number"),
        (f"phone [name]", f"{Stickers.EMOJI['phone']} Show contact's phones"),
        (f"all", f"{Stickers.EMOJI['contact']} Show all contacts"),
        (f"add-birthday [name] [DD.MM.YYYY]", f"{Stickers.EMOJI['birthday']} Add birthday"),
        (f"show-birthday [name]", f"{Stickers.EMOJI['birthday']} Show birthday"),
        (f"birthdays", f"{Stickers.EMOJI['birthday']} Upcoming birthdays (next week)"),
        (f"hello", "Get greeting"),
        (f"help", "Show this help"),
        (f"close/exit", f"{Stickers.EMOJ['exit']} Exit program")
    ]
    


if __name__ == "__main__":
    # Run the main program
    main()