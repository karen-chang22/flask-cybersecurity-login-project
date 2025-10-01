## Cybersecurity login system built with Flask
This project is a simple, self-taught project built using **Flask**. Its main focus is the backend, allowing users to **register**, **login**, and **log out**, with password hashing 
using **bcrypt** for protection. 

## Features
- User registration with secure password hashing (and salts)
- Login and session management
- Logout function
- Use of bcrypt to store passwords and not in plain text
- SQLite database integration
- Basic HTML templates for frontend
- Mainly built for learning Flask, an introduction to cybersecurity, and familiarizing with backend structure

## Purpose
I created this project to:
- Learn how web applications manage user data
- How to manage authentication securely
- Understand basic backend logic with Python and Flask
- Explore the fundamental concepts of cybersecurity (bcrypt, hasing, salts, SQL injection)
- Prepare myself for future projects with real-world relevance

## Tech Stack
- Python - Flask
- SQLite - Database
- HTML - Password security
- bcrypt - Templates

## To Get Started
You need:
- Python 3.10 or higher
- Flask
- bcrypt
To install & set up:
1. **Clone this repository**
```bash
git clone https://github.com/karen-chang22/flask-cybersecurity-login-project.git
cd flask-cybersecurity-login-project
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Instal dependencies
```bash
pip install flask bcrypt
```
4. Initialize database
```bash
python init_db.py
```
5. Run the app
```bash
python app.py
```
6. Visit and check it out in the browser
http://127.0.0.1:5000/
