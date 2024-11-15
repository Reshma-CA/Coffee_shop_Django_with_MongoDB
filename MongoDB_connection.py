# test_mongodb.py
from pymongo import MongoClient

def test_connection():
    try:
        client = MongoClient('mongodb+srv://reshmaca70:TNa1CQYyo0nR0w3T@cluster0.3di4u.mongodb.net/Coffee_Django')
        db = client.admin
        db.command('ping')
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

if __name__ == "__main__":
    test_connection()