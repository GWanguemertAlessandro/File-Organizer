# File Organizer

[![Python CI](https://github.com/GWanguemertAlessandro/File-Organizer/actions/workflows/ci.yml/badge.svg)](https://github.com/GWanguemertAlessandro/File-Organizer/actions/workflows/ci.yml)

A command-line tool that organizes files in a directory by their file type.

-----

## Features

- Organizes files by extension into categorized folders
- Supports dry-run mode to preview changes
- Prevents overwriting existing files
- Clean CLI interface built with `argparse`
- Modular architecture
- Unit tests with `pytest`
- Continuous Integration with GitHub Actions
- Installable locally as a Python package

-----

## Example

Before:

```bash
my_folder/
├── document.txt
├── script.py
├── notes.md
```

After running the tool:

```bash
my_folder/
├── text/
│ └── document.txt
├── python/
│ └── script.py
├── markdown/
│ └── notes.md
```
----- 

## Installation (Local Development)

Clone the repository:

```bash
git clone https://github.com/GWanguemertAlessandro/File-Organizer.git
cd File-Organizer
```
Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```
Install in editable mode:

```bash
pip install -e .
```
-----

## Usage

Run the tool:

```bash
file-organizer path\to\your\folder
```
Preview changes without moving files:

```bash
file-organizer path\to\your\folder --dry-run
```
-----

## Running Tests

```bash
pytest
```
-----

## Project Structure
```bash
file_organizer/
├── organizer.py
├── cli.py
└── __init__.py

tests/
```
-----

## 🛠 Tech Stack

### Core
- Python 3.10+
- argparse
- pathlib
- logging

### Testing
- pytest
- coverage.py

### Packaging & Distribution
- setuptools
- pyproject.toml

### CI/CD
- Git
- GitHub Actions
- Semantic Versioning
