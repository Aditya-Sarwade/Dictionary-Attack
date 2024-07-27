# Dictionary Attack Tool

This is a simple Python script to perform a dictionary attack on an MD5 hash. The script reads passwords from a file (`wordlist.txt`), hashes each password, and compares it to a given hash.

## Prerequisites

- Python 3.x

## Setup

1. **Clone the repository** (or download the script and `wordlist.txt` file):
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:
    ```bash
    cd <repository-directory>
    ```

3. **Create or update `wordlist.txt`**:
    Ensure you have a file named `wordlist.txt` in the same directory as your Python script. This file should contain a list of possible passwords, one per line.

## Usage

Run the script with Python:

```bash
python crack_hash.py
