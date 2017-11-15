from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

main_html = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <!-- create your form here -->
      <form method="post">
          <label for="rot">Rotate by:  </label>
          <input type="text" name="rot" />
          <br>
          <textarea name="text" type="text" cosl="30" rows="5">{0}</textarea>
          <br>
          <input type="submit" value="Submit Query" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return main_html.format("")

@app.route("/", methods=['POST'])
def encrypt():
    answer = rotate_string(request.form['text'], int(request.form['rot']))
    return main_html.format(answer)

app.run()
