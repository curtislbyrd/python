# Python Virtual Environment Commands
Python's `venv` module allows you to create isolated environments for your projects. This means each project can have its own dependencies, regardless of what dependencies every other project has. Using `venv` helps prevent conflicts between packages, makes it easier to manage requirements, and keeps your global Python installation clean and stable. It's an essential tool for maintaining reproducible and organized Python development workflows.

| Action                                      | Command                                      | Platform/Notes                                                                 |
|---------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------|
| Create virtual environment (standard, Python 3.3+) | `python -m venv venv`                       | Creates a virtual environment named `venv` in the current directory.           |
| Create with specific Python version         | `python3.10 -m venv venv`                   | Use the exact Python executable (e.g., `python3.10`, `python3.11`). Must be installed. |
| Create with specific Python version (using virtualenv) | `virtualenv -p /usr/local/bin/python3.10 venv` | Requires `virtualenv` package installed (`pip install virtualenv`). Path to Python may vary. |
| Activate virtual environment                | `.\venv\Scripts\activate`                   | Windows                                                                        |
| Activate virtual environment                | `source venv/bin/activate`                  | macOS / Linux                                                                  |
| Note after activation                       | —                                           | Shell prompt should show `(venv)` prefix.                                       |
| Deactivate virtual environment              | `deactivate`                                | All platforms                                                                  |
| Note after deactivation                     | —                                           | Returns to system/global Python interpreter.                                    |