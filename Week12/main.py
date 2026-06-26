from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask CSS Activity</title>
    </head>

    <body style="background-color: green; color: red;">

        <h1>Welcome to Flask!</h1>

        <p>This is my first HTML page using Flask.</p>

        <p>
            Learn Flask by visiting the
            <a href="https://flask.palletsprojects.com/en/stable/quickstart/" target="_blank">
                Flask Quickstart Documentation
            </a>.
        </p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)