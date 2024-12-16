from flask import Flask
from routes.main import main
from routes.operations import operations
app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(operations)



if __name__ == '__main__':
    app.run()
