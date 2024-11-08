# Itinerary Planner

A Django-based application for planning and booking itineraries with collaboration features.

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saikat-Raj/Itinerary-Planner.git
   cd Itinerary-Planner

2. **Create and activate a virtual environment:**
   ```bash
   conda create -n itinerary-planner
   conda activate itinerary-planner

3. **Install dependencies:**
   ```bash
   conda env create -f environment.yml
   conda activate itinerary-planner

4. **Set up the MySQL database:**
+ Open the MySQL command line or MySQL Workbench and run:

   ```bash
   CREATE DATABASE itinerary_planner;
   CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
   GRANT ALL PRIVILEGES ON itinerary_planner.* TO 'admin'@'localhost';
   FLUSH PRIVILEGES;

+ Update your settings.py file in Django to configure the MySQL database:
   ```bash
   DATABASES = 
   {
    'default': 
    {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itinerary_planner',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
   }

5. **Apply migrations:**
   ```bash
   python manage.py migrate


5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser

6. **Run the development server:**
   ```bash
   python manage.py runserver

You can now access the app in your browser at http://127.0.0.1:8000/.

## Running Tests

1. **Clone the repository**
   ```bash
   pip install pytest pytest-django

2. **Run the tests:**
   ```bash
   pytest

This will automatically discover and run tests from your project’s tests directory.

## Contributing

If you want to contribute to the project:

1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine.
3. **Create a new feature branch** and implement your changes.
4. **Push your changes** and open a pull request to the main repository.

Please ensure that your changes are well-tested and follow the project’s code style.
