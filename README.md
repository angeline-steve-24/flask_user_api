# flask_user_api

A simple REST API built with Flask that allows you to manage user data using basic CRUD operations: GET, POST, PUT, DELETE.
User data is stored in an in-memory dictionary for easy testing and learning.

🚀 Features

Create a new user

Retrieve all users or a single user

Update user information

Delete a user

Uses an in-memory data store (no database needed)

📦 Requirements

Install Flask:

pip install flask

▶️ Running the App

Run the API locally:

python app.py


The server starts at:

http://127.0.0.1:5000

📚 API Endpoints
Method	Endpoint	Description
GET	/users	Get all users
GET	/users/<id>	Get a specific user
POST	/users	Create a new user
PUT	/users/<id>	Update an existing user
DELETE	/users/<id>	Delete a user
📝 Example JSON (POST / PUT)
{
  "name": "Alice",
  "email": "alice@example.com"
}

🔧 Example cURL Command (Create User)
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'

🎯 Outcome

This project demonstrates the fundamentals of REST API development using Flask, including routing, JSON handling, and CRUD operations.
