# Random Username Generator

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

> A Python GUI application for generating creative usernames 🎮

## 📌 Overview

A desktop application that provides a graphical interface for generating unique usernames by combining adjectives and nouns with optional numbers and special characters.

## 🚀 Features

- Modern Tkinter GUI interface
- 200+ adjectives and nouns for combinations
- Customizable username generation:
  - Add numbers (1-4 digits)
  - Include special characters
  - Generate multiple usernames at once
- Save generated names to file
- No external dependencies

## Preview

<div style="display: flex; justify-content: center;">
    <img src="https://github.com/user-attachments/assets/bec6f97f-df37-4015-81a8-ae22d7588e99" width="400" height="600" />
    <img src="https://github.com/user-attachments/assets/74152756-22ac-4ba1-b62b-6486c3015a1e" width="400" height="600" />
</div>

## 💻 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/sanjeeviraju/random-username-generator.git
cd random-username-generator
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Run the application:
```bash
python src/main.py
```

## 📁 Project Structure

```
username-generator/
├── src/                  # Source code
│   ├── data/            # Word lists
│   │   ├── adjectives.txt
│   │   └── nouns.txt
│   ├── main.py          # Entry point
│   ├── gui.py           # GUI implementation
│   ├── generator.py     # Username generation logic
│   └── constants.py     # Configuration
├── LICENSE              # MIT license
├── README.md           # This file
└── requirements.txt     # Project dependencies
```

## 🛠️ Requirements

- Python 3.6+
- Tkinter (included in standard Python installation)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

Create an issue or submit a pull request.

Project Link: [https://github.com/sanjeeviraju/random-username-generator](https://github.com/sanjeeviraju/random-username-generator)

## 📝 License

```
MIT License

Copyright (c) 2025 sanjeeviraju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

