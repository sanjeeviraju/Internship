"""
Username Generator GUI Implementation
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_username  # Changed to relative import
from constants import DEFAULT_ADJECTIVES, DEFAULT_NOUNS  # Changed to relative import

class UsernameGeneratorGUI:
    """
    Main GUI class for the Username Generator application.
    
    Handles the creation and management of all GUI elements, user interactions,
    and username generation requests.
    """

    def __init__(self, root):
        """
        Initialize the GUI window and setup all widgets.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Random Username Generator")
        self.root.geometry("700x700")
        
        # Simplified colors for light theme only
        self.colors = {
            'bg': '#ffffff',
            'fg': '#333333',
            'button': '#4CAF50',
            'button_fg': '#000000',
            'input_bg': '#f8f9fa',
            'input_fg': '#333333',
            'hover': '#45a049',
            'border': '#cccccc'
        }
        
        self._create_widgets()
        self.setup_styles()
        self.apply_theme()

    def _create_widgets(self):
        """Create and configure all GUI widgets with proper layout."""
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Title
        title_label = ttk.Label(self.main_frame, 
                               text="✨ Username Generator", 
                               font=("Consolas", 24, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Input section
        input_frame = ttk.LabelFrame(self.main_frame, text="Options", padding=15)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Grid layout for inputs
        ttk.Label(input_frame, text="Number of usernames:").grid(row=0, column=0, pady=5)
        self.num_usernames = ttk.Spinbox(
            input_frame, 
            from_=1, 
            to=1000, 
            width=10,
            validate='key',
            validatecommand=(self.root.register(self.validate_number), '%P')
        )
        self.num_usernames.set(5)
        self.num_usernames.grid(row=0, column=1, pady=5, padx=10)
        
        # Numbers option with its spinbox
        numbers_frame = ttk.Frame(input_frame)
        numbers_frame.grid(row=1, column=0, columnspan=2, pady=5)
        
        self.use_numbers = tk.BooleanVar()
        ttk.Checkbutton(numbers_frame, 
                       text="Include numbers", 
                       variable=self.use_numbers,
                       command=self.toggle_digits).pack(side=tk.LEFT)
        
        self.num_digits = ttk.Spinbox(numbers_frame, 
                                     from_=1, to=4, 
                                     width=5, 
                                     state="disabled")
        self.num_digits.set(2)
        self.num_digits.pack(side=tk.LEFT, padx=10)
        
        # Special characters option
        self.use_special = tk.BooleanVar()
        ttk.Checkbutton(input_frame, 
                       text="Include special characters", 
                       variable=self.use_special).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Generate button
        generate_btn = ttk.Button(
            self.main_frame, 
            text="🎲 Generate Usernames",
            command=self.generate_usernames,
            style='Accent.TButton'
        )
        generate_btn.pack(pady=20, padx=20, fill=tk.X)
        
        # Result area
        result_frame = ttk.LabelFrame(self.main_frame, text="Generated Usernames", padding=15)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.result_text = tk.Text(result_frame, 
                                 height=8,
                                 width=50, 
                                 font=("Consolas", 11))
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Save button
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        save_btn = ttk.Button(
            button_frame, 
            text="💾 Save to File",
            command=self.save_results,
            style='Accent.TButton'
        )
        save_btn.pack(pady=5, padx=20, fill=tk.X)

    def setup_styles(self):
        """Configure ttk styles for consistent widget appearance."""
        style = ttk.Style()
        style.configure('Accent.TButton', 
                       font=('Consolas', 12, 'bold'),
                       padding=10)
        style.configure('TSpinbox', 
                       font=('Consolas', 11),
                       background=self.colors['input_bg'],
                       fieldbackground=self.colors['input_bg'])
        style.configure('TFrame', 
                       background=self.colors['bg'])
        style.configure('TLabelframe', 
                       font=('Consolas', 11),
                       background=self.colors['bg'])
        style.configure('TLabel', 
                       font=('Consolas', 11))
        style.configure('TLabelframe.Label', 
                       font=('Consolas', 11))
        style.configure('TCheckbutton', 
                       font=('Consolas', 11))

    def apply_theme(self):
        self.root.configure(bg=self.colors['bg'])
        style = ttk.Style()
        
        # Configure all the styles
        for widget in ['TFrame', 'TLabelframe', 'TLabel', 'TCheckbutton']:
            style.configure(widget, background=self.colors['bg'])
        
        style.configure('Accent.TButton',
                       background=self.colors['button'],
                       foreground=self.colors['button_fg'])

        # Configure text widget
        self.result_text.configure(
            bg=self.colors['input_bg'],
            fg=self.colors['fg'],
            insertbackground=self.colors['fg']
        )

    def toggle_digits(self):
        state = "normal" if self.use_numbers.get() else "disabled"
        self.num_digits.configure(state=state)

    def validate_number(self, value):
        if value == "":
            return True
        try:
            num = int(value)
            return num > 0
        except ValueError:
            return False

    def generate_usernames(self):
        """
        Generate usernames based on current user selections.
        Handles error cases and updates the display with results.
        """
        try:
            num = int(self.num_usernames.get())
            if num <= 0:
                messagebox.showerror("Error", "Please enter a positive number")
                return
            num_digits = int(self.num_digits.get()) if self.use_numbers.get() else 0
            
            generated = set()
            attempts = 0
            max_attempts = num * 100

            while len(generated) < num and attempts < max_attempts:
                attempts += 1
                username = generate_username(
                    use_numbers=self.use_numbers.get(),
                    num_digits=num_digits,
                    use_special=self.use_special.get()
                )
                generated.add(username)

            self.result_text.delete(1.0, tk.END)
            for i, uname in enumerate(generated, 1):
                self.result_text.insert(tk.END, f"{i}. {uname}\n")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    def save_results(self):
        """
        Save generated usernames to a text file.
        Provides user feedback through message boxes.
        """
        if not self.result_text.get(1.0, tk.END).strip():
            messagebox.showwarning("Warning", "No usernames to save!")
            return

        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = "usernames.txt"
        filepath = os.path.join(script_dir, filename)

        try:
            with open(filepath, 'w') as file:
                file.write(self.result_text.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Saved usernames to {filename}")
        except IOError as e:
            messagebox.showerror("Error", f"Could not save file: {e}")
