"""
Data analysis module for the Expense Tracker application.

This module provides functionality for analyzing expense data,
generating summaries, and producing insight reports.

Classes:
    Analytics: Provides expense data analysis capabilities
"""
from datetime import datetime
from decimal import Decimal
from collections import defaultdict

class Analytics:
    """
    Provides expense data analysis capabilities.
    
    This class offers methods to analyze expense data and generate
    various reports and summaries.
    
    Attributes:
        storage (Storage): Storage instance to access expense data
    """
    
    def __init__(self, storage):
        """
        Initialize the analytics engine.
        
        Args:
            storage (Storage): Storage instance to access expense data
        """
        self.storage = storage

    def monthly_summary(self):
        """
        Generate a monthly summary of expenses.
        
        Retrieves all expenses and groups them by month, calculating
        the total for each month.
        
        Returns:
            dict: Monthly expense totals, with month keys in format 'YYYY-MM'
        """
        expenses = self.storage.get_expenses()
        monthly_totals = defaultdict(Decimal)

        for expense in expenses:
            date = datetime.fromisoformat(expense['date'])
            month_key = f"{date.year}-{date.month:02d}"
            monthly_totals[month_key] += Decimal(expense['amount'])

        print("\nMonthly Summary:")
        for month, total in sorted(monthly_totals.items()):
            print(f"{month}: ${total:.2f}")

    def category_analysis(self):
        """
        Generate a summary of expenses by category.
        
        Retrieves all expenses and groups them by category, calculating
        the total for each category.
        
        Returns:
            dict: Category expense totals
        """
        expenses = self.storage.get_expenses()
        category_totals = defaultdict(Decimal)
        
        for expense in expenses:
            category_totals[expense['category']] += Decimal(expense['amount'])

        print("\nCategory Analysis:")
        for category, total in sorted(category_totals.items()):
            print(f"{category.capitalize()}: ${total:.2f}")
