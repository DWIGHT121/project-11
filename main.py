from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def first():
    return "Hello Everyone! It's me buddie. aba chai pull garnu la?? "


if __name__ == "__main__":
    app.run(debug=True)
