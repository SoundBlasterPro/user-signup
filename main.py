from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def validate_username(text):

    if not text: #blank entry
        error = "This section cannot be left blank."
        return form.format(error) 
    if contains_spaces(text):
        error = "Username cannot contain spaces!"
        return form.format(error)

def contains_spaces(text):
    istrue = True
    for characters in text:
        if character == " ":
            istrue = False
    
    return istrue

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('submit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()