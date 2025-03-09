"""
Username Generator Core Logic
Handles the generation of usernames by combining words from predefined lists
with optional numbers and special characters.
"""

import random
from constants import (SPECIAL_CHARS, DEFAULT_ADJECTIVES, DEFAULT_NOUNS,
                      ADJECTIVES_FILE, NOUNS_FILE)

def load_words(filename):
    """
    Load words from a text file, filtering out empty lines and comments.
    
    Args:
        filename (str): Path to the word list file
        
    Returns:
        list: List of words if file exists, None otherwise
    """
    try:
        with open(filename, 'r') as file:
            return [line.strip().lower() for line in file if line.strip() and not line.startswith('//')]
    except FileNotFoundError:
        return None

# Initialize word lists from files or fallback to defaults
ADJECTIVES = load_words(ADJECTIVES_FILE) or DEFAULT_ADJECTIVES
NOUNS = load_words(NOUNS_FILE) or DEFAULT_NOUNS

def generate_username(adjectives=None, nouns=None, use_numbers=False, num_digits=2, use_special=False):
    """
    Generate a unique username by combining an adjective and noun with optional elements.
    
    Args:
        adjectives (list, optional): Custom list of adjectives. Defaults to None.
        nouns (list, optional): Custom list of nouns. Defaults to None.
        use_numbers (bool): Include random numbers in username. Defaults to False.
        num_digits (int): Number of digits to append (1-4). Defaults to 2.
        use_special (bool): Include special character at end. Defaults to False.
    
    Returns:
        str: Generated username string
    """
    adj_list = adjectives if adjectives is not None else ADJECTIVES
    noun_list = nouns if nouns is not None else NOUNS
    
    adjective = random.choice(adj_list).capitalize()
    noun = random.choice(noun_list).capitalize()
    username = adjective + noun
    
    if use_numbers:
        max_num = 10 ** num_digits - 1
        numbers = str(random.randint(0, max_num)).zfill(num_digits)
        username += numbers
    
    if use_special:
        username += random.choice(SPECIAL_CHARS)
    
    return username
