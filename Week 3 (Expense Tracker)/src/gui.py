from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from expense import Expense, ExpenseManager
from storage import Storage
from analytics import Analytics
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from themes import THEMES, DEFAULT_THEME

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker - Dashboard")
        self.root.geometry("1200x700")
        
        # Ensure window is not minimized at startup
        self.root.state('normal')  # Set window state to normal (not minimized)
        self.root.update_idletasks()  # Process any pending UI tasks
        
        # Make the window resizable and responsive
        self.root.minsize(800, 600)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Initialize theme
        self.current_theme_name = DEFAULT_THEME
        self.current_theme = THEMES[self.current_theme_name]()
        
        # Configure the root window with theme
        self.root.configure(bg=self.current_theme.bg_main)
        
        # Initialize the style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.storage = Storage()
        self.expense_manager = ExpenseManager(self.storage)
        self.analytics = Analytics(self.storage)
        
        self.apply_theme()
        self.setup_ui()
        self.center_window()
        
        # Ensure window is raised to the top and gets focus
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(lambda: self.root.attributes('-topmost', False))
        self.root.focus_force()

    def apply_theme(self):
        """Apply the current theme to all ttk widgets."""
        theme = self.current_theme
        
        # Configure ttk styles
        self.style.configure('TFrame', background=theme.bg_frame)
        self.style.configure('TLabel', background=theme.bg_frame, foreground=theme.fg_main, font=('Segoe UI', 10))
        self.style.configure('TButton', background=theme.bg_widget, foreground=theme.fg_main, padding=8)
        self.style.configure('Header.TLabel', background=theme.bg_frame, foreground=theme.fg_heading, font=('Segoe UI', 14, 'bold'))
        self.style.configure('TLabelframe', background=theme.bg_frame)
        self.style.configure('TLabelframe.Label', background=theme.bg_frame, foreground=theme.fg_heading, font=('Segoe UI', 11, 'bold'))
        self.style.configure('Add.TButton', background=theme.bg_widget, foreground=theme.fg_main, font=('Segoe UI', 10, 'bold'), padding=10)
        
        # Configure Treeview colors
        self.style.configure('Treeview', 
                             background=theme.bg_widget, 
                             fieldbackground=theme.bg_widget, 
                             foreground=theme.fg_main)
        self.style.configure('Treeview.Heading', 
                             background=theme.bg_frame,
                             foreground=theme.fg_heading, 
                             font=('Segoe UI', 10, 'bold'))
        
        # Add style for selected theme button
        self.style.configure('Selected.TButton', 
                            background=theme.highlight,
                            foreground=theme.bg_frame,
                            font=('Segoe UI', 10, 'bold'),
                            padding=8)
        
        # Update the root window
        self.root.configure(bg=theme.bg_main)
        
    def theme_changed(self, *args):
        """Handle theme change events."""
        self.current_theme_name = self.theme_var.get()
        self.current_theme = THEMES[self.current_theme_name]()
        self.apply_theme()
        
        # Refresh the UI to apply the new theme
        self.refresh_data()
        self.status_var.set(f"Theme changed to {self.current_theme_name}")

    def center_window(self):
        # Force update the window info
        self.root.update_idletasks()
        
        # Get window size
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        
        # Get screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        # Set geometry and ensure window is visible
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.deiconify()  # Ensure window is not minimized

    def setup_ui(self):
        # Main container with sections
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Configure container weights for responsiveness
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(0, weight=0) # Top panel
        main_container.rowconfigure(1, weight=20) # Content
        
        # Top panel with title and theme selector
        top_panel = ttk.Frame(main_container)
        top_panel.pack(fill=tk.X, pady=(0, 10))
        
        # Title
        ttk.Label(top_panel, text="Expense Tracker Dashboard", style="Header.TLabel").pack(side=tk.LEFT)
        
        # Replace theme dropdown with theme buttons
        theme_frame = ttk.Frame(top_panel)
        theme_frame.pack(side=tk.RIGHT, padx=10)
        
        ttk.Label(theme_frame, text="Theme:").pack(side=tk.LEFT, padx=(0, 10))
        
        # Add a button for each theme
        self.theme_buttons = {}
        for theme_name in THEMES.keys():
            # Create a button for this theme
            btn = ttk.Button(
                theme_frame, 
                text=theme_name,
                width=8,
                command=lambda tn=theme_name: self.set_theme(tn)
            )
            btn.pack(side=tk.LEFT, padx=2)
            self.theme_buttons[theme_name] = btn
        
        # Highlight the current theme button
        self._update_theme_buttons()
        
        # Rest of the UI setup continues as before
        # Create three-column layout
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Input section (fixed width)
        left_panel = ttk.Frame(content_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Input Frame
        input_frame = ttk.LabelFrame(left_panel, text="Add New Expense", padding="15")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Input fields
        fields = [
            ("Amount ($):", self.setup_amount_field),
            ("Description:", self.setup_description_field),
            ("Category:", self.setup_category_field)
        ]
        
        for i, (label, setup_func) in enumerate(fields):
            field_frame = ttk.Frame(input_frame)
            field_frame.pack(fill=tk.X, pady=5)
            ttk.Label(field_frame, text=label, width=15).pack(side=tk.LEFT)
            setup_func(field_frame)

        # Add button
        add_btn = ttk.Button(input_frame, text="Add Expense", command=self.add_expense, style='Add.TButton')
        add_btn.pack(fill=tk.X, pady=10)
        
        # Analysis buttons
        analysis_frame = ttk.LabelFrame(left_panel, text="Analysis Tools", padding="15")
        analysis_frame.pack(fill=tk.X, pady=10)
        
        buttons = [
            ("Monthly Summary", self.show_monthly_summary),
            ("Category Analysis", self.show_category_analysis)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(analysis_frame, text=text, command=command)
            btn.pack(fill=tk.X, pady=5)
        
        # Middle panel - Expense list (expands horizontally)
        middle_panel = ttk.Frame(content_frame)
        middle_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10)
        middle_panel.columnconfigure(0, weight=1)
        middle_panel.rowconfigure(0, weight=1)
        
        list_frame = ttk.LabelFrame(middle_panel, text="Expense History", padding="15")
        list_frame.pack(fill=tk.BOTH, expand=True)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview with scrollbars
        tree_frame = ttk.Frame(list_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        self.expense_tree = ttk.Treeview(tree_frame, columns=("Date", "Amount", "Category", "Description"), 
                                      show="headings", style="Treeview")
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.expense_tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.expense_tree.xview)
        
        self.expense_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Add right-click menu
        self.context_menu = tk.Menu(self.expense_tree, tearoff=0)
        self.context_menu.add_command(label="Edit Expense", command=self.edit_selected_expense)
        self.context_menu.add_command(label="Delete Expense", command=self.delete_selected_expense)
        
        # Bind right-click event
        self.expense_tree.bind("<Button-3>", self.show_context_menu)
        
        # Double-click to edit
        self.expense_tree.bind("<Double-1>", lambda event: self.edit_selected_expense())
        
        # Also allow delete with Delete key
        self.expense_tree.bind("<Delete>", lambda event: self.delete_selected_expense())
        
        # Configure columns
        columns = {
            "Date": (150, "Date"),
            "Amount": (100, "Amount ($)"),
            "Category": (120, "Category"),
            "Description": (200, "Description")
        }
        
        # Track sorting state
        self.sort_column = "Date"  # Default sort column
        self.sort_reverse = False  # Default sort direction
        
        for col, (width, heading) in columns.items():
            self.expense_tree.column(col, width=width, minwidth=width)
            self.expense_tree.heading(col, text=heading, 
                                   command=lambda c=col: self.sort_treeview(c))
        
        # Grid tree and scrollbars
        self.expense_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Right panel - Analytics dashboard (fixed proportion)
        right_panel = ttk.Frame(content_frame)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=(10, 0))
        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(0, weight=1)
        
        dashboard_frame = ttk.LabelFrame(right_panel, text="Expense Analytics", padding="15")
        dashboard_frame.pack(fill=tk.BOTH, expand=True)
        dashboard_frame.columnconfigure(0, weight=1)
        dashboard_frame.rowconfigure(0, weight=1)
        
        # Create the chart frame for the pie chart
        self.chart_frame = ttk.Frame(dashboard_frame)
        self.chart_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        status_frame = ttk.Frame(main_container, relief=tk.SUNKEN, padding=(5, 2))
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.columnconfigure(0, weight=1)
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        ttk.Label(status_frame, textvariable=self.status_var).pack(side=tk.LEFT)
        
        # Update expense list and dashboard
        self.refresh_data()

    def setup_amount_field(self, parent):
        self.amount_entry = ttk.Entry(parent, width=20)
        self.amount_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def setup_description_field(self, parent):
        self.desc_entry = ttk.Entry(parent, width=20)
        self.desc_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def setup_category_field(self, parent):
        self.category_combo = ttk.Combobox(parent, values=ExpenseManager.CATEGORIES, width=20, state="readonly")
        self.category_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.category_combo.set(ExpenseManager.CATEGORIES[0])

    def add_expense(self):
        try:
            amount = Decimal(self.amount_entry.get())
            description = self.desc_entry.get()
            category = self.category_combo.get()

            if not description:
                self.status_var.set("Error: Please enter a description")
                return
                
            if amount <= 0:
                self.status_var.set("Error: Amount must be greater than zero")
                return

            expense = Expense(amount, description, category)
            self.storage.save_expense(expense)
            
            self.amount_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.category_combo.set(ExpenseManager.CATEGORIES[0])
            
            self.refresh_data()
            self.status_var.set(f"Added expense: ${amount} for {category}")
        except ValueError as e:
            self.status_var.set(f"Error: Invalid amount - {str(e)}")

    def refresh_data(self):
        # Refresh expense tree
        self.refresh_expenses()
        
        # Update dashboard charts
        self.update_dashboard()

    def refresh_expenses(self):
        # Clear existing data
        for item in self.expense_tree.get_children():
            self.expense_tree.delete(item)
        
        # Load expenses
        expenses = self.storage.get_expenses()
        for expense in expenses:
            self.expense_tree.insert("", "end", values=(
                expense['date'],
                f"${expense['amount']}",
                expense['category'],
                expense['description']
            ))
        
        # Apply current sort after refresh
        self.sort_treeview(self.sort_column)

    def update_dashboard(self):
        # Clear existing charts
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
            
        # Get expense data
        expenses = self.storage.get_expenses()
        if not expenses:
            ttk.Label(self.chart_frame, text="No expenses recorded yet.\nAdd expenses to see analytics.",
                     font=('Segoe UI', 12), justify='center').pack(expand=True)
            return
            
        # Calculate category totals for pie chart
        category_totals = {}
        total_amount = Decimal('0')
        for expense in expenses:
            category = expense['category']
            amount = Decimal(expense['amount'])
            category_totals[category] = category_totals.get(category, Decimal('0')) + amount
            total_amount += amount
            
        # Create summary text
        summary_frame = ttk.Frame(self.chart_frame)
        summary_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(summary_frame, text=f"Total Expenses: ${total_amount:.2f}",
                 font=('Segoe UI', 12, 'bold')).pack(side=tk.LEFT)
        
        ttk.Label(summary_frame, text=f"Categories: {len(category_totals)}",
                 font=('Segoe UI', 12)).pack(side=tk.RIGHT)
        
        # Create simplified pie chart with error handling
        try:
            # Sort categories for better visualization
            sorted_items = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
            labels = [k.capitalize() for k, v in sorted_items]
            values = [float(v) for k, v in sorted_items]
            
            # Create a figure only if we have data
            if values:
                # Create frame for chart with better resizing
                chart_display = ttk.Frame(self.chart_frame)
                chart_display.pack(fill=tk.BOTH, expand=True)
                
                # Create figure with safe defaults
                plt.rcParams.update({'figure.autolayout': True})
                fig = plt.figure(figsize=(5, 4), dpi=100)
                
                # Apply theme colors to figure background
                bg_color = self.current_theme.bg_frame
                fig.patch.set_facecolor(bg_color)
                ax = fig.add_subplot(111)
                ax.set_facecolor(bg_color)
                
                # Use theme colors for the pie chart if specified, fallback to default if error occurs
                try:
                    colors = self.current_theme.pie_colors
                    wedges, texts, autotexts = ax.pie(
                        values,
                        labels=None,  
                        autopct='%1.1f%%',
                        startangle=90,
                        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
                        textprops={'color': 'white', 'weight': 'bold', 'fontsize': 9},
                        colors=colors
                    )
                except:
                    # Fallback to default matplotlib colors if custom colors cause issues
                    wedges, texts, autotexts = ax.pie(
                        values,
                        labels=None,  
                        autopct='%1.1f%%',
                        startangle=90,
                        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
                        textprops={'color': 'white', 'weight': 'bold', 'fontsize': 9}
                    )
                
                # Add legend with theme-appropriate colors
                legend = ax.legend(
                    labels,
                    loc='center left',
                    bbox_to_anchor=(0.9, 0.5),
                    fontsize=9
                )
                
                # Set legend text color based on theme
                for text in legend.get_texts():
                    text.set_color(self.current_theme.fg_main)
                
                # Set title with theme-appropriate color
                ax.set_title("Expense Distribution by Category", color=self.current_theme.fg_heading)
                
                # Create canvas for embedding plot with better resizing
                canvas = FigureCanvasTkAgg(fig, master=chart_display)
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(fill=tk.BOTH, expand=True)
                
                # Ensure plot is properly closed
                plt.close(fig)
            else:
                ttk.Label(self.chart_frame, text="No data for visualization",
                         font=('Segoe UI', 12), justify='center').pack(expand=True)
                         
        except Exception as e:
            # Log the error and show it in the UI
            import traceback
            traceback.print_exc()  # Print the full traceback for debugging
            
            # Create a text-based alternative representation
            error_frame = ttk.Frame(self.chart_frame)
            error_frame.pack(fill=tk.BOTH, expand=True)
            
            ttk.Label(error_frame, text="Chart display not available",
                     font=('Segoe UI', 11, 'bold')).pack(pady=(10, 5))
            
            # Show a simple text representation instead
            text_widget = tk.Text(error_frame, height=10, width=40)
            text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Format data as text
            text_widget.insert(tk.END, "Category Breakdown:\n\n")
            for category, amount in sorted_items:
                percentage = (float(amount) / float(total_amount)) * 100
                text_widget.insert(tk.END, f"{category.capitalize()}: ${float(amount):.2f} ({percentage:.1f}%)\n")
            
            text_widget.configure(state='disabled')

    def show_monthly_summary(self):
        expenses = self.storage.get_expenses()
        monthly_totals = {}
        grand_total = Decimal('0')
        
        for expense in expenses:
            date = datetime.fromisoformat(expense['date'])
            month_key = f"{date.strftime('%B %Y')}"
            amount = Decimal(expense['amount'])
            monthly_totals[month_key] = monthly_totals.get(month_key, Decimal('0')) + amount
            grand_total += amount
        
        if not monthly_totals:
            messagebox.showinfo("Monthly Summary", "No expenses recorded")
            return
            
        # Create a formatted summary
        summary_lines = ["Month                Amount"]
        summary_lines.append("=" * 30)
        
        for month, total in sorted(monthly_totals.items()):
            summary_lines.append(f"{month:<20} ${total:>8.2f}")
        
        summary_lines.append("=" * 30)
        summary_lines.append(f"Total:{' '*14} ${grand_total:>8.2f}")
        
        # Create a custom dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Monthly Summary")
        dialog.geometry("350x400")
        dialog.transient(self.root)  # Make dialog modal
        
        # Add content
        text_widget = tk.Text(dialog, wrap=tk.NONE, height=20, width=35, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(dialog, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        
        text_widget.insert(tk.END, "\n".join(summary_lines))
        text_widget.configure(state='disabled')
        
        # Add close button
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)

    def show_category_analysis(self):
        expenses = self.storage.get_expenses()
        category_totals = {}
        grand_total = Decimal('0')
        
        for expense in expenses:
            category = expense['category']
            amount = Decimal(expense['amount'])
            category_totals[category] = category_totals.get(category, Decimal('0')) + amount
            grand_total += amount
        
        if not category_totals:
            messagebox.showinfo("Category Analysis", "No expenses recorded")
            return
        
        # Create dialog with details
        dialog = tk.Toplevel(self.root)
        dialog.title("Category Analysis")
        dialog.geometry("400x500")
        dialog.transient(self.root)  # Make dialog modal
        
        # Add scrollable frame
        main_frame = ttk.Frame(dialog, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add total at the top
        ttk.Label(main_frame, text=f"Total Expenses: ${grand_total:.2f}", 
                 font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        # Create category list with progress bars
        category_frame = ttk.Frame(main_frame)
        category_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a canvas with scrollbar
        canvas = tk.Canvas(category_frame)
        scrollbar = ttk.Scrollbar(category_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add category details with bars
        sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        for category, amount in sorted_categories:
            percentage = (amount / grand_total) * 100 if grand_total else 0
            
            category_row = ttk.Frame(scrollable_frame)
            category_row.pack(fill=tk.X, pady=5)
            
            ttk.Label(category_row, text=f"{category.capitalize()}:", width=15).pack(side=tk.LEFT)
            ttk.Label(category_row, text=f"${amount:.2f}", width=10).pack(side=tk.LEFT)
            ttk.Label(category_row, text=f"({percentage:.1f}%)", width=10).pack(side=tk.LEFT)
        
        # Add close button
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)

    def show_context_menu(self, event):
        """Show context menu on right-click."""
        # First identify the item that was clicked on
        item = self.expense_tree.identify_row(event.y)
        if item:
            # Select the item and show menu
            self.expense_tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def edit_selected_expense(self):
        """Edit the selected expense."""
        selected_items = self.expense_tree.selection()
        if not selected_items:
            self.status_var.set("No expense selected for editing")
            return
            
        # Get the index and current values of the selected item
        selected_item = selected_items[0]
        index = self.expense_tree.index(selected_item)
        expense_details = self.expense_tree.item(selected_item, 'values')
        
        # Create edit dialog
        edit_dialog = tk.Toplevel(self.root)
        edit_dialog.title("Edit Expense")
        edit_dialog.geometry("400x250")
        edit_dialog.transient(self.root)  # Make dialog modal
        edit_dialog.grab_set()  # Make dialog modal
        
        # Dialog content
        frame = ttk.Frame(edit_dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Date display (not editable)
        date_frame = ttk.Frame(frame)
        date_frame.pack(fill=tk.X, pady=5)
        ttk.Label(date_frame, text="Date:", width=15).pack(side=tk.LEFT)
        ttk.Label(date_frame, text=expense_details[0]).pack(side=tk.LEFT)
        
        # Amount field
        amount_frame = ttk.Frame(frame)
        amount_frame.pack(fill=tk.X, pady=5)
        ttk.Label(amount_frame, text="Amount ($):", width=15).pack(side=tk.LEFT)
        amount_var = tk.StringVar(value=expense_details[1].replace('$', ''))
        amount_entry = ttk.Entry(amount_frame, textvariable=amount_var, width=20)
        amount_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Description field
        desc_frame = ttk.Frame(frame)
        desc_frame.pack(fill=tk.X, pady=5)
        ttk.Label(desc_frame, text="Description:", width=15).pack(side=tk.LEFT)
        desc_var = tk.StringVar(value=expense_details[3])
        desc_entry = ttk.Entry(desc_frame, textvariable=desc_var, width=20)
        desc_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Category field
        cat_frame = ttk.Frame(frame)
        cat_frame.pack(fill=tk.X, pady=5)
        ttk.Label(cat_frame, text="Category:", width=15).pack(side=tk.LEFT)
        cat_combo = ttk.Combobox(cat_frame, values=ExpenseManager.CATEGORIES, width=20, state="readonly")
        cat_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        cat_combo.set(expense_details[2])
        
        # Status message
        status_var = tk.StringVar()
        status_label = ttk.Label(frame, textvariable=status_var, foreground="red")
        status_label.pack(fill=tk.X, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        # Save changes function
        def save_changes():
            try:
                # Validate input
                new_amount = Decimal(amount_var.get())
                new_description = desc_var.get()
                new_category = cat_combo.get()
                
                if new_amount <= 0:
                    status_var.set("Amount must be greater than zero")
                    return
                
                if not new_description:
                    status_var.set("Description cannot be empty")
                    return
                
                # Update the expense
                updated_data = {
                    'amount': str(new_amount),
                    'description': new_description,
                    'category': new_category
                }
                
                if self.storage.update_expense(index, updated_data):
                    self.refresh_data()
                    self.status_var.set(f"Updated expense: ${new_amount} for {new_category}")
                    edit_dialog.destroy()
                else:
                    status_var.set("Failed to update expense")
            except ValueError as e:
                status_var.set(f"Invalid amount: {str(e)}")
        
        # Save and Cancel buttons
        ttk.Button(button_frame, text="Save", command=save_changes).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=edit_dialog.destroy).pack(side=tk.RIGHT, padx=5)

    def delete_selected_expense(self):
        """Delete the selected expense without confirmation popup."""
        selected_items = self.expense_tree.selection()
        if not selected_items:
            self.status_var.set("No expense selected for deletion")
            return
            
        # Get the index of the selected item
        selected_item = selected_items[0]
        index = self.expense_tree.index(selected_item)
        expense_details = self.expense_tree.item(selected_item, 'values')
        
        # Delete from storage
        if self.storage.delete_expense(index):
            # Update UI
            self.refresh_data()
            self.status_var.set(f"Deleted: {expense_details[1]} for {expense_details[2]}")
        else:
            self.status_var.set("Error: Failed to delete expense")

    def sort_treeview(self, column):
        """Sort treeview content when a column header is clicked."""
        # If already sorting by this column, reverse the order
        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            # Otherwise, sort by the new column in ascending order
            self.sort_reverse = False
            self.sort_column = column
        
        # Update header to show sort direction
        for col in ["Date", "Amount", "Category", "Description"]:
            # Remove any existing sort indicators
            text = col
            if col == self.sort_column:
                # Add sort indicator
                text = f"{col} {'↓' if self.sort_reverse else '↑'}"
            self.expense_tree.heading(col, text=text)
        
        # Get all items
        items = [(self.expense_tree.set(item, column), item) for item in self.expense_tree.get_children('')]
        
        # Sort items based on column type
        if column == "Date":
            # Sort by date
            items.sort(reverse=self.sort_reverse)
        elif column == "Amount":
            # Sort numerically by amount (remove $ sign)
            items.sort(key=lambda x: float(x[0].replace('$', '')), reverse=self.sort_reverse)
        else:
            # Sort alphabetically for other columns
            items.sort(reverse=self.sort_reverse)
        
        # Rearrange items in sorted positions
        for index, (_, item) in enumerate(items):
            self.expense_tree.move(item, '', index)
        
        # Update status bar
        self.status_var.set(f"Sorted by {column} {'descending' if self.sort_reverse else 'ascending'}")

    def set_theme(self, theme_name):
        """Change the current theme."""
        if theme_name != self.current_theme_name:
            self.current_theme_name = theme_name
            self.current_theme = THEMES[self.current_theme_name]()
            self.apply_theme()
            self._update_theme_buttons()
            
            # Refresh the UI to apply the new theme
            self.refresh_data()
            self.status_var.set(f"Theme changed to {self.current_theme_name}")

    def _update_theme_buttons(self):
        """Update theme button styles to highlight the selected one."""
        # Configure button styles
        for theme_name, button in self.theme_buttons.items():
            if theme_name == self.current_theme_name:
                button.config(style='Selected.TButton')
            else:
                button.config(style='TButton')
