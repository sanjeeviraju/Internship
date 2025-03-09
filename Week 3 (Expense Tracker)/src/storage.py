"""
Data persistence module for the Expense Tracker application.

This module handles loading and saving expense data to persistent storage,
using JSON files as the primary storage mechanism.

Classes:
    Storage: Manages expense data persistence operations
"""
import json
import os
from datetime import datetime
from pathlib import Path

class Storage:
    """
    Handles data persistence for expenses.
    
    This class manages reading and writing expense data to a JSON file,
    as well as basic CRUD operations for expense records.
    
    Attributes:
        data_dir (Path): Directory path for data storage
        data_file (Path): File path for the expenses JSON file
    """
    
    def __init__(self):
        """
        Initialize the storage manager.
        
        Sets up the data directory and file paths, and ensures
        the storage structure exists.
        """
        self.data_dir = Path(__file__).parent.parent / 'data'
        self.data_file = self.data_dir / 'expenses.json'
        self._initialize_storage()

    def _initialize_storage(self):
        """
        Create necessary directories and files if they don't exist.
        
        Ensures the data directory exists and creates an empty expenses
        file if none exists.
        """
        self.data_dir.mkdir(exist_ok=True)
        if not self.data_file.exists():
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def save_expense(self, expense):
        """
        Save a new expense to storage.
        
        Args:
            expense (Expense): The expense object to save
        """
        expenses = self.get_expenses()
        expenses.append(expense.to_dict())
        with open(self.data_file, 'w') as f:
            json.dump(expenses, f, indent=2)

    def get_expenses(self):
        """
        Retrieve all expenses from storage.
        
        Returns:
            list: List of expense dictionaries, sorted by date
        """
        with open(self.data_file, 'r') as f:
            expenses = json.load(f)
        return sorted(expenses, key=lambda x: datetime.fromisoformat(x['date']))

    def delete_expense(self, expense_index):
        """
        Delete an expense by its index in the sorted list.
        
        Args:
            expense_index (int): Index of the expense to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        expenses = self.get_expenses()
        if 0 <= expense_index < len(expenses):
            del expenses[expense_index]
            with open(self.data_file, 'w') as f:
                json.dump(expenses, f, indent=2)
            return True
        return False

    def update_expense(self, expense_index, updated_data):
        """
        Update an expense at the given index with new data.
        
        Args:
            expense_index (int): Index of the expense to update
            updated_data (dict): New data to apply to the expense
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        expenses = self.get_expenses()
        if 0 <= expense_index < len(expenses):
            expenses[expense_index].update(updated_data)
            with open(self.data_file, 'w') as f:
                json.dump(expenses, f, indent=2)
            return True
        return False
