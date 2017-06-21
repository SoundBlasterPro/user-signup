from flask import Flask, request, redirect, render_template
import cgi
import os
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ["POST"])
def process_submission():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["verify"]
    email = request.form["email"]
    error = 0
    username_error = ''
    password_error = ''
    email_error = ''
    validate_error = ''

    if validate(username) != username:
        username_error = validate(username)
        error += 1
    if validate(password) != password:
        password_error = validate(password)
        error += 1
    if email:
        if validate_address(email) != email:
            email_error = validate_address(email)
            error += 1
    if password_match(password, password2) != True:
        validate_error = "Passwords do not match"
        error +=1

    if error > 0:
        return render_template("submit.html", title = "User Signup",
                        username = username,
                        email = email, 
                        invalid_username = username_error, 
                        invalid_password = password_error, 
                        invalid_email = email_error, 
                        verify_error = validate_error
                        )
    if error == 0:
        return redirect("/submission-success?username={0}".format(username))

def validate(text):

    if not text: #user submits a blank rotation field
        error = "This section cannot be left blank."
        return error
    if contains_spaces(text):
        error = "Username cannot contain spaces."
        return error
    if len(text) <= 3:
        error = "Please enter a value greater than 3 characters."
        return error
    if len(text) > 20:
        error = "Please enter a value less than 20 characters."
        return error
    
    return text

def validate_address(email):

    at_symbol = 0
    period = 0
    if contains_spaces(email):
        error = "Username cannot contain spaces."
        return error
    if len(email) <= 3:
        error = "Please enter a value greater than 3 characters."
        return error
    if len(email) > 20:
        error = "Please enter a value less than 20 characters."
        return error
    for character in email:
        if character == '@':
            at_symbol += 1
        if character == ".":
            period += 1
    if at_symbol > 1 or at_symbol == 0:
        return "Invalid email address"
    if period > 1 or period == 0:
        return "Invalid email address"
    return email

def password_match(password, verify):
    if password != verify:
        return False
    else:
        return True

def contains_spaces(text):
    
    for character in text:
        if character == " ":
            return True
    
    return False

@app.route("/submission-success")
def valid_user():
    username = request.args.get("username")
    return "<h1>You submitted {0}. You're a real boy!</h1>".format(username)

@app.route("/")
def index():
    return render_template('submit.html', title="User Signup")

app.run()