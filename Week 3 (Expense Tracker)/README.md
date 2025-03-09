<div align="center">

# Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/expense-tracker/graphs/commit-activity)

A sophisticated expense tracking solution with data visualization and analysis capabilities.

</div>

## 🌟 Features

### 🎨 Modern Interface
- Adaptive themes (Light/Dark/AMOLED)
- Responsive design
- Real-time data visualization
- Cross-platform compatibility

### 💰 Financial Management
- Quick expense entry
- Category-based organization
- Multi-column sorting and filtering
- Comprehensive expense history

### 📊 Analytics & Insights
- Interactive pie charts
- Monthly summaries
- Category-wise analysis
- Financial trends visualization

### ⚙️ Technical Highlights
- JSON-based persistent storage
- CLI support for automation
- Modular architecture
- Theme-aware visualization engine

## Preview
<<<<<<< HEAD
=======
![Light](https://github.com/user-attachments/assets/211a2269-bdcc-45f1-99b7-35af95ab7b71)

![Dark](https://github.com/user-attachments/assets/49d93ba2-6677-42db-8887-ba962659ac6f)
>>>>>>> 243e7cde6bb406fa37d662b11e0fd64fc571ead2

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

### Installation Steps

1. Clone & Navigate
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   venv\Scripts\activate     # Windows
   ```

3. Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Launch
   ```bash
   python src/main.py       # GUI Mode
   python src/main.py --cli # CLI Mode
   ```

## 🎯 Usage

### Dashboard Layout

| Section | Purpose | Features |
|---------|---------|----------|
| Left Panel | Input & Controls | • Expense entry<br>• Category selection<br>• Analysis tools |
| Center Panel | Expense History | • Sortable columns<br>• Edit/Delete functions<br>• Quick filters |
| Right Panel | Analytics | • Pie charts<br>• Category breakdown<br>• Total summaries |

### Key Operations

#### Adding Expenses
1. Enter amount
2. Provide description
3. Select category
4. Click "Add Expense"

#### Managing Records
- **Edit**: Double-click or right-click → Edit
- **Delete**: Select + Delete key or context menu
- **Sort**: Click column headers
- **Filter**: Use quick filter buttons

#### Theme Customization
Choose your preferred visual style:
- **☀️ Light**: Professional day mode
- **🌙 Dark**: Reduced eye strain
- **⚫ AMOLED**: Maximum contrast, power-efficient

## 🏗️ Architecture

```
expense_tracker/
├── src/                 # Source code
│   ├── __init__.py      
│   ├── main.py          # Application entry point
│   ├── gui.py           # Graphical user interface
│   ├── expense.py       # Core expense models
│   ├── storage.py       # Data persistence
│   ├── analytics.py     # Analysis functionality
│   └── themes.py        # UI theme definitions
├── data/                # Data storage
│   └── expenses.json    # Expense records
├── docs/                # Documentation
│   └── user_guide.md    # Detailed user instructions
├── tests/               # Unit tests
│   ├── __init__.py
│   ├── test_expense.py
│   └── test_storage.py
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
├── README.md            # Project information
└── requirements.txt     # Dependencies
```

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
