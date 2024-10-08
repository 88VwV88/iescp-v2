from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/login", methods=("POST",))
@cross_origin()
def login():
    if request.method == "POST":
        print(f"Hello, {request.json.get("username", "abc")}!")
        print(
            f"password hash is: {generate_password_hash(request.form.get("password", "1234"))}"
        )
        return ""


if __name__ == "__main__":
    app.run(debug=True, port=8080)
