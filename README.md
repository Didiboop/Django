# Didintle Electrical Maintenance Services

This is a Django web application for managing electrical maintenance service requests.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Setting Up the Database](#setting-up-the-database)
- [Running the Development Server](#running-the-development-server)
- [Accessing the Admin Interface](#accessing-the-admin-interface)
- [Database Troubleshooting](#database-troubleshooting)

## Requirements

- Python 3.x
- Django 3.x or 4.x
- A virtual environment (recommended)

## Installation

1. **Clone the Repository:**

   Clone the project from your repository:

   ```bash
   git clone https://github.com/your-repo-url.git

cd your-project-directory

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py migrate

python manage.py migrate --run-syncdb

python manage.py createsuperuser

python manage.py runserver

