
# Coffee Shop Management System with MongoDB and Django

This project is a full-stack Coffee Shop Management System built using Django as the backend framework and MongoDB as the database. The system handles multiple functionalities, including user authentication, a list of different kinds of coffee, and an interactive user interface.

Key Features:

1, User Registration and Login (with password hashing).
2, Role-based access (Admin and Customer).
3, List of different Coffee

Technologies Used:

Backend: Django Framework.
Database: MongoDB.
Frontend: HTML, CSS, Bootstrap.

##  1,Set Up a Virtual Environment



```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

```

##  2,  Configure MongoDB



```bash
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'coffee_shop_db',
        'CLIENT': {
            'host': '<your-mongodb-connection-string>',
            'username': '<your-username>',
            'password': '<your-password>',
        }
    }
}


```

# 3,Additional Packages Added

### 1, Djongo (v1.3.6):

A Django adapter for MongoDB, allowing seamless integration with MongoDB while maintaining Django's ORM functionalities.
Enables usage of Django's models, migrations, and admin features with MongoDB.

### 2, dnspython (v2.3.0):
A DNS toolkit for Python.
Essential for resolving DNS in connection strings, especially for cloud-based MongoDB instances like MongoDB Atlas.

### 3,pymongo (v3.12.3):
The official MongoDB driver for Python.
Allows communication between Django and MongoDB.
Used internally by Djongo for database operations.

##  4 ,Run Migrations


```bash
python manage.py makemigrations
python manage.py migrate


```

##  4 , Create a Superuser


```bash
python manage.py createsuperuser

```

##  4 ,Run the Server



```bash
python manage.py runserver


```



Project Demo : https://youtu.be/aev6UgPIDyE
