"""
Expense data models and management for the Expense Tracker application.

This module defines the core data structures and operations for managing
expenses, including creation, categorization, and basic validation.

Classes:
    Expense: Data model for individual expense records
    ExpenseManager: Manager for expense-related operations
"""
from datetime import datetime
from decimal import Decimal

class Expense:
    """
    Data model representing a single expense record.
    
    Attributes:
        amount (Decimal): The expense amount
        description (str): Description of the expense
        category (str): Category the expense belongs to
        date (datetime): Date and time the expense was recorded
    """
    
    def __init__(self, amount, description, category, date=None):
        """
        Initialize a new expense record.
        
        Args:
            amount: The expense amount (will be converted to Decimal)
            description (str): Description of the expense
            category (str): Category the expense belongs to
            date (datetime, optional): Date of the expense. Defaults to current time.
        """
        self.amount = Decimal(str(amount))
        self.description = description
        self.category = category
        self.date = date or datetime.now()

    def to_dict(self):
        """
        Convert the expense object to a dictionary for storage.
        
        Returns:
            dict: Dictionary representation of the expense
        """
        return {
            'amount': str(self.amount),
            'description': self.description,
            'category': self.category,
            'date': self.date.isoformat()
        }

class ExpenseManager:
    """
    Manager for expense-related operations.
    
    Handles expense creation, validation, and manages the predefined
    expense categories.
    
    Attributes:
        CATEGORIES (list): List of predefined expense categories
        storage (Storage): Data storage instance for persistence
    """
    
    CATEGORIES = [
        'food', 'transportation', 'entertainment', 'utilities',
        'housing', 'healthcare', 'education', 'shopping',
        'travel', 'insurance', 'savings', 'debt payment',
        'gifts', 'personal care', 'investments', 'other'
    ]

    def __init__(self, storage):
        """
        Initialize the expense manager.
        
        Args:
            storage (Storage): Data storage instance for persisting expenses
        """
        self.storage = storage

    def add_expense(self):
        """
        Add a new expense via CLI prompt.
        
        Collects expense details from user input, validates them,
        creates an Expense object, and saves it to storage.
        
        Returns:
            bool: True if expense was added successfully, False otherwise
        """
        try:
            amount = Decimal(input("Enter amount: "))
            description = input("Enter description: ")
            
            print("\nCategories:")
            for i, category in enumerate(self.CATEGORIES, 1):
                print(f"{i}. {category}")
            category_idx = int(input("Select category (number): ")) - 1
            category = self.CATEGORIES[category_idx]

            expense = Expense(amount, description, category)
            self.storage.save_expense(expense)
            print("Expense added successfully!")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")

    def view_expenses(self):
        """
        Display all expenses via CLI.
        
        Retrieves all expenses from storage and prints them in a
        human-readable format to the console.
        """
        expenses = self.storage.get_expenses()
        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(f"\nDate: {expense['date']}")
            print(f"Amount: ${expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
