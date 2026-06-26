from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    image_path = None

    if request.method == "POST":
        image = request.files["image"]

        if image.filename != "":
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload and Display Image</title>
    </head>
    <body>
        <h1>Upload and Display an Image</h1>

        <form method="POST" enctype="multipart/form-data">
            <label>Select an image:</label>
            <input type="file" name="image" accept="image/*" required>
            <br><br>
            <button type="submit">Upload Image</button>
        </form>

        {% if image_path %}
            <h2>Uploaded Image:</h2>
            <img src="{{ image_path }}" width="400">
        {% endif %}
    </body>
    </html>
    """, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)