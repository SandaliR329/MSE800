from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    bmi = ""
    category = ""

    if request.method == "POST":

        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    html = open("index.html").read()

    html = html.replace("{{bmi}}", str(bmi))
    html = html.replace("{{category}}", category)

    if bmi == "":
        html = html.replace("{{display}}", "none")
    else:
        html = html.replace("{{display}}", "block")

    return html


@app.route("/style.css")
def css():
    return send_file("style.css", mimetype="text/css")


if __name__ == "__main__":
    app.run(debug=True)