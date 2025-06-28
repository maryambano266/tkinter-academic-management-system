
# IIT KGP Registration System (Tkinter GUI)

## Overview

This is a Python GUI application for managing registration, login, and profile functionalities for users at IIT Kharagpur. It supports three types of users:

* Undergraduate (UG) Students
* Postgraduate (PG) Students
* Teachers

The system uses Tkinter for the GUI, JSON for data storage, and includes password and email validation.

---

## Features

### User Registration

* Register as UG student, PG student, or teacher
* Gmail format email validation
* Strong password requirement (8–12 characters with uppercase, lowercase, digit, and special character)
* Prevents duplicate email registration

### User Login

* Secure login with role selection
* Account locked after 3 failed attempts
* Logout and session handling

### Profile Management

* Change password with validation
* Update email address
* Deregister (delete account)

### Admin Functions

* View lists of all registered UG, PG, and Teacher accounts
* Save and load user data using JSON files
* Persistent data between sessions

---

## Installation

### Requirements

* Python 3.x
* Tkinter (included by default in Python)
* Pillow library for handling images

Install Pillow using:

```bash
pip install pillow
```

### Running the App

1. Ensure a background image named `origi.png` is in the same directory
2. Run the application using:

```bash
python iit_kgp_registration.py
```

---

## File Structure

* `iit_kgp_registration.py` – Main script
* `origi.png` – Background image
* `ug_dic.json`, `pg_dic.json`, `tea_dic.json` – User data stored separately

---

## Security and Validation

* Password must contain 8–12 characters, with at least one uppercase, one lowercase, one digit, and one special character
* Gmail-format required for email
* Account locks after 3 failed login attempts
* Comprehensive error handling for invalid input, missing files, and corrupted JSON

---

## Class Structure

* `Person` – Base class
* `Student` – Inherits from Person
* `UG_Student`, `PG_Student`, `Teacher` – Role-specific classes

---

## Example JSON Format

```json
{
  "user@example.com": "Password@123"
}
```

---

## Notes

* `origi.png` must be placed in the project directory for the UI background
* All data is stored locally and persists between sessions
* Automatically loads data if JSON files are present on startup
