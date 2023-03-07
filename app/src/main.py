from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from api.user import user_route
import os
from config import ProductionConfig

config = ProductionConfig()

app = Flask(__name__)
app.register_blueprint(user_route)

CORS(app)
app.config.from_object(config)
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug='False', host='0.0.0.0')
