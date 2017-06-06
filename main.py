from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rot">
            <b>Rotate by: <b> 
            <input type="text" id="rot" name="rot" value="0"/>
            </label>
            <br><br>
            <label for="text">
            <input type="textarea" id="text" name="text"/>
            <br>
            <input type="submit" value="Submit Query"/>
    </body>
</html>
"""
@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encryption = rotate_string(text, rot)
    
    return "<h1>" + encryption + "</h1>"


@app.route("/")
def index():
    return form
app.run()