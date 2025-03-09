"""
Theme definitions for the Expense Tracker application.

This module defines visual themes for the application, including
color schemes for the UI and data visualizations.

Classes:
    Theme: Base class for theme definitions
    LightTheme: Standard light theme
    DarkTheme: Dark theme for reduced eye strain
    AmoledTheme: True black theme for AMOLED displays
"""

class Theme:
    """
    Base class for application theme definitions.
    
    This class defines the basic structure and default values
    for application themes. Specific themes inherit from this class
    and override values as needed.
    
    Attributes:
        name (str): Theme name
        bg_main (str): Main background color (hex)
        bg_frame (str): Frame background color (hex)
        bg_widget (str): Widget background color (hex)
        fg_main (str): Main text color (hex)
        fg_heading (str): Heading text color (hex)
        fg_accent (str): Accent color for highlights (hex)
        border (str): Border color (hex)
        highlight (str): Selection highlight color (hex)
        chart_bg (str): Chart background color (hex)
        chart_text (str): Chart text color (hex)
        chart_grid (str): Chart grid line color (hex)
        pie_colors (list): List of colors for pie chart segments
    """
    name = "Base"
    
    # Background colors
    bg_main = "#ffffff"
    bg_frame = "#f5f5f7"
    bg_widget = "#ffffff"
    
    # Text colors
    fg_main = "#000000"
    fg_heading = "#000000"
    fg_accent = "#0066cc"
    
    # Border and highlight colors
    border = "#cccccc"
    highlight = "#0066cc"
    
    # Chart specific colors
    chart_bg = "#ffffff"
    chart_text = "#333333"
    chart_grid = "#dddddd"
    
    # Graph colors
    pie_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                 '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


class LightTheme(Theme):
    """
    Standard light theme with soft colors.
    
    A clean, professional light theme designed for daily use,
    with high readability and contrast.
    """
    name = "Light"
    
    bg_main = "#f5f5f7"
    bg_frame = "#ffffff"
    bg_widget = "#ffffff"
    
    fg_main = "#333333"
    fg_heading = "#222222"
    fg_accent = "#0066cc"
    
    border = "#dddddd"
    highlight = "#0066cc"
    
    # Chart specific colors
    chart_bg = "#f5f5f7"
    chart_text = "#333333"
    chart_grid = "#dddddd"
    
    # Use a safe color palette that works well on light backgrounds
    pie_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                 '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


class DarkTheme(Theme):
    """
    Dark theme with reduced brightness.
    
    Designed for low-light environments and reduced eye strain,
    with carefully balanced contrast for readability.
    """
    name = "Dark"
    
    bg_main = "#2d2d2d"
    bg_frame = "#333333"
    bg_widget = "#3c3c3c"
    
    fg_main = "#e0e0e0"
    fg_heading = "#ffffff"
    fg_accent = "#66b3ff"
    
    border = "#555555"
    highlight = "#66b3ff"
    
    # Chart specific colors
    chart_bg = "#333333"
    chart_text = "#e0e0e0"
    chart_grid = "#444444"
    
    # Use brighter colors for dark theme
    pie_colors = ['#5dade2', '#ff9f7f', '#7dcea0', '#f1948a', '#bb8fce',
                 '#d7bde2', '#f8c471', '#73c6b6', '#f7dc6f', '#85c1e9']


class AmoledTheme(Theme):
    """
    AMOLED theme with pure black backgrounds.
    
    Optimized for OLED/AMOLED displays to save battery and
    provide maximum contrast, with vibrant accent colors.
    """
    name = "AMOLED"
    
    bg_main = "#000000"
    bg_frame = "#0f0f0f"
    bg_widget = "#1a1a1a"
    
    fg_main = "#f0f0f0"
    fg_heading = "#ffffff"
    fg_accent = "#00ccff"
    
    border = "#333333"
    highlight = "#00ccff"
    
    # Chart specific colors
    chart_bg = "#0f0f0f"
    chart_text = "#f0f0f0"
    chart_grid = "#333333"
    
    # Use high contrast colors for AMOLED theme
    pie_colors = ['#00bfff', '#ff6666', '#66ff66', '#ffcc00', '#cc66ff', 
                 '#00ffff', '#ff66cc', '#66ffcc', '#ffff66', '#ff66ff']


# Available themes
THEMES = {
    "Light": LightTheme,
    "Dark": DarkTheme,
    "AMOLED": AmoledTheme
}

# Default theme
DEFAULT_THEME = "Light"
