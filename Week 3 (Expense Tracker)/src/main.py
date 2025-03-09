"""
Main entry point for the Expense Tracker application.

This module initializes and runs the application in either GUI
or CLI mode, based on command-line arguments.

Functions:
    run_cli: Start the application in command-line interface mode
    run_gui: Start the application in graphical user interface mode
"""
import sys
import tkinter as tk
from expense import ExpenseManager
from storage import Storage
from analytics import Analytics
from gui import ExpenseTrackerGUI

def display_menu():
    """
    Display the main CLI menu and get user selection.
    
    Returns:
        str: The user's menu selection
    """
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Monthly Summary")
    print("4. View Category Analysis")
    print("5. Exit")
    return input("Select an option: ")

def run_cli():
    """
    Run the application in command-line interface mode.
    
    Initializes required components and starts the CLI
    interaction loop.
    """
    storage = Storage()
    expense_manager = ExpenseManager(storage)
    analytics = Analytics(storage)

    while True:
        choice = display_menu()
        if choice == "1":
            expense_manager.add_expense()
        elif choice == "2":
            expense_manager.view_expenses()
        elif choice == "3":
            analytics.monthly_summary()
        elif choice == "4":
            analytics.category_analysis()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid option. Please try again.")

def run_gui():
    """
    Run the application in graphical user interface mode.
    
    Initializes the main window and GUI components, and
    starts the tkinter event loop.
    """
    root = tk.Tk()
    
    # Set default window state
    root.withdraw()  # Hide initially to avoid flashing
    
    # Create the application
    app = ExpenseTrackerGUI(root)
    
    # Now show the window properly
    root.deiconify()
    root.lift()
    root.focus_force()
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_gui()
