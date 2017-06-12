from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

string = ""

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
    """
textedit = """
    <body>
        <form method="post">
            <label for="rot">
            <b>Rotate by: <b> 
            <input type="text" id="rot" name="rot" value="0"/>
            </label>
            <br><br>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encryption = rotate_string(text, rot)
    return form + textedit.format(encryption)


@app.route("/")
def index():
    return form + textedit.format(string)




app.run()