"""
Username Generator Application Entry Point
Launches the GUI interface for the username generator.
"""

import tkinter as tk
from gui import UsernameGeneratorGUI  # Changed to relative import

def main():
    """Initialize and start the username generator application."""
    root = tk.Tk()
    app = UsernameGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
