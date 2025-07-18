# password-manager
A simple command-line password manager built with Python. Supports secure password generation, storage, viewing, and deletion of credentials for various services.

## Features

- Add new password entries manually
- Generate secure passwords with uppercase, lowercase, digits, and symbols
- View saved passwords in a readable format
- Delete password entries by service name
- Stores passwords in a local file (`pwd_manager.txt`)

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager

2. (Optional) Create a virtual environment:
    Bash:
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

3. Run the script:
    Bash:
    python password_manager.py

Usage:
When you run the script, you'll be prompted to choose an option:- 

- add: Add a new password manually
- create: Generate a secure password and optionally save it
- view: Display all saved passwords
- delete: Remove a password entry by service name
- q: Quit the application
Passwords are stored in pwd_manager.txt in the same directory.

Security Notes:
- Passwords are stored in plain text. Do not use this tool for sensitive or personal credentials without adding encryption.

- The file pwd_manager.txt is excluded from version control using .gitignore.

Contributing:
Feel free to fork this repository and submit pull requests with improvements or new features.

License:
This project is open-source and available under the MIT License.

Author:
Ashish Ganapati Patil
