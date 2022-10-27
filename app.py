import json
from flask import Flask, render_template, request, jsonify

# from views import views

app = Flask(__name__)


# app.register_blueprint(views, url_prefix="/")


@app.route("/")
def home():
    # result = get_post_javascript_data()  # menu.getResult()
    return render_template("home.html", result="HI")


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        message = {'greeting': 'Hello from Flask!'}
        return jsonify(message)
    if request.method == 'POST':
        print(request.get_json())
        return 'Sucesss', 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)
