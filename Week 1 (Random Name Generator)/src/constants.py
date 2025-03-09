"""
Application Constants and Configuration
Defines global constants, file paths, and default word lists used throughout the application.
"""

import os

# Special characters available for username generation
SPECIAL_CHARS = ['@', '#', '$', '%', '&', '_', '?', '-']

# File path configuration for word lists - using relative paths
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PACKAGE_DIR, 'data')
ADJECTIVES_FILE = os.path.join(DATA_DIR, 'adjectives.txt')
NOUNS_FILE = os.path.join(DATA_DIR, 'nouns.txt')

# Default word lists used when external files are not available
# These provide a fallback to ensure the application remains functional
DEFAULT_ADJECTIVES = [
    'quick', 'lazy', 'happy', 'silly', 'brave', 'calm', 'eager', 'gentle', 'jolly', 'kind',
    'bold', 'clever', 'daring', 'witty', 'merry', 'noble', 'proud', 'fierce', 'lively', 'wild',
    'quiet', 'swift', 'tough', 'vivid', 'zesty', 'angry', 'busy', 'chill', 'dapper', 'epic',
    'fancy', 'gloomy', 'hasty', 'icy', 'jovial', 'keen', 'mighty', 'nifty', 'odd', 'peppy',
    'quirky', 'radiant', 'sly', 'tricky', 'upbeat', 'vivid', 'witty', 'excited', 'young', 'zealous'
]

DEFAULT_NOUNS = [
    'tiger', 'dragon', 'eagle', 'wolf', 'bear', 'shark', 'phoenix', 'lion', 'fox', 'owl',
    'panther', 'raven', 'hawk', 'falcon', 'viper', 'scorpion', 'rhino', 'buffalo', 'goat', 'snake',
    'spider', 'knight', 'wizard', 'giant', 'thief', 'pirate', 'ninja', 'samurai', 'mage', 'warrior',
    'king', 'queen', 'prince', 'princess', 'robot', 'alien', 'ghost', 'zombie', 'vampire', 'demon',
    'angel', 'dwarf', 'elf', 'orc', 'goblin', 'troll', 'sphinx', 'griffin', 'unicorn', 'pegasus',
    'gladiator', 'sorcerer', 'assassin', 'monk', 'cleric', 'bard', 'ranger', 'paladin', 'berserker',
    'necromancer', 'warlock', 'archer', 'captain', 'commander', 'jester', 'merchant', 'smith', 'alchemist'
]
