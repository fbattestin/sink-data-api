from flask import Flask
from views.sns import sns_blueprint

app = Flask(__name__)
app.register_blueprint(sns_blueprint)

if __name__ == '__main__':
    app.run(port=5000)
