
# Coffee Shop Management System with MongoDB and Django

This project is a full-stack Coffee Shop Management System built using Django as the backend framework and MongoDB as the database. The system handles multiple functionalities, including user authentication, a list of different kinds of coffee, and an interactive user interface.

**Key Features:**


1, User Registration and Login (with password hashing).

2, Role-based access (Admin and Customer).

3, List of different Coffee

**Technologies Used:**


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
        'CLIENT': {
            'host': '<your-mongodb-connection-string>', # Replace with your MongoDB server address
            'port': 27017,               # Replace with your MongoDB port if different
            'username': '<your-username>', # Replace with your MongoDB username (optional)
            'password': '<your-password>', # Replace with your MongoDB password (optional)
            'authSource': 'admin', # Replace with your MongoDB authentication database (optional)
        },
        'NAME': '<your-Databasename>',
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

## Note
The MongoDB atlas's network access should change to **0.0.0.0/0**. This can handle every IP address connection to proceed otherwise, a connection error occurs.

![WhatsApp Image 2024-11-18 at 12 25 34_4498cc5a](https://github.com/user-attachments/assets/dd83abe8-5c86-41c1-ba9f-aa3c11ee35a5)

![WhatsApp Image 2024-11-18 at 12 25 57_8d60fdb3](https://github.com/user-attachments/assets/759c94e7-d81f-4d56-942b-9ab9fd72406d)

![WhatsApp Image 2024-11-18 at 12 26 21_19b480c1](https://github.com/user-attachments/assets/837db3ea-620b-42d9-adb3-2a2b4a037cb5)

![WhatsApp Image 2024-11-18 at 12 27 29_0d77ff20](https://github.com/user-attachments/assets/84aaf7d9-91af-4005-8c20-5ac75add17af)

##  4 ,Connection with MongoDB


![WhatsApp Image 2024-11-18 at 12 29 14_96bad4e1](https://github.com/user-attachments/assets/0e027071-888a-4a4e-9d79-7d5d9c585727)


Project Demo : https://youtu.be/aev6UgPIDyE
