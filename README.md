# Django Project Setup

Follow these steps to set up and run the Django project.

## Prerequisites

- Python installed (Version 3.x recommended)
- pip (Python package manager)

## Setup Instructions

1. **Create a Virtual Environment**  
   ```sh
   python -m venv venv
   ```

2. **Activate the Virtual Environment**  
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Django**  
   ```sh
   pip install Django
   ```

4. **Create a Django Project**  
   ```sh
   django-admin startproject loginSignup
   ```

5. **Navigate to the Project Directory**  
   ```sh
   cd loginSignup
   ```

6. **Create a Django App**  
   ```sh
   python manage.py startapp base
   ```

7. **Apply Migrations**  
   ```sh
   python manage.py migrate
   ```

8. **Run the Development Server**  
   ```sh
   python manage.py runserver
   ```

## Additional Notes

- The default server runs at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Ensure that `base` is added to `INSTALLED_APPS` in `settings.py` if necessary.

