# request lets me get input from users
import sqlite3
import bcrypt
from flask import Flask, request, render_template, request, redirect, session, url_for
#importing tools from Flask; Flask lets me make the app

app = Flask(__name__) # creates Flask app instance
app.secret_key = "secret-key" #required to see sessions

connection = None
@app.route("/") #route decorator - defines which URL this function will respond to 
# / for homepage
def home(): # defining function named home, Flask runs this function if smo visists
    return render_template("home.html")
    return "🌷 Hello from Flask backend!" #output (sent back to browser)

# /register
@app.route("/register", methods=["GET", "POST"]) #a new route that only responds to POST requests & GET now (able to see)
# when someone POSTS to /register, the next function will run
def register(): #define register function that handles form data
    if request.method == "GET":
        return render_template("register.html")
    # Get form data from the request
    email = request.form.get("email") #getting the value of form field named email from request
    password = request.form.get("password")
    #email & password are temporary placeholders used only while one user is interacting with the server
    #after values are saved into database, request is finished, variables are cleared from memory
    
    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
     # Save to database
    connection = sqlite3.connect("users.db") #creating/opening/connecting to my SQLite database named users.db; acts like mini spreadsheat
    cursor = connection.cursor() #creates a cursor object; it’s like a tool you use to send commands to the database
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_pw))
        connection.commit()
        message = f"✅ Registered {email}!"
    except sqlite3.IntegrityError: #runs if the email already exists, bc emails must be unique!!!
        message = "⚠️ Email already registered."
    finally:
        connection.close() #it's a good habit to close the connection to database!
    return render_template("register_result.html", message=message)
    

# /login 
@app.route("/login", methods=["Get", "POST"])  # new webpage for login, only accepting POST
def login():
    if request.method == "GET":
        return render_template("login.html")
    email = request.form.get("email")
    password = request.form.get("password")

    connection = None  # fix: declare the variable before the try

    try:
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Look for the email
        cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result:
            hashed_pw = result[0]
            # Compare hashed passwords
            if bcrypt.checkpw(password.encode("utf-8"), hashed_pw):
                session["user_id"] = email
                return render_template("dashboard.html", email=email)
                # render_template help connect backend to frontend
            else:
                message = "❌ Incorrect password."
                return render_template("wrongpw.html", message=message)
        else:
            message = "❌ Email not found."

    except Exception as e:
        message = f"⚠️ Error: {e}"

    finally:
        if connection:  # fix: only close if connection is not None
            connection.close()

    return message

@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        email = session["user_id"]
        return redirect(url_for("dashboard")) #preferred method, bc route names could be changed, 
        #this makes the redirection path more flexible
    else:
        return redirect(url_for("home")) #send back to home if not logged in


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home")) # users logout -> clear session



if __name__ == "__main__":
    app.run(debug=True)
