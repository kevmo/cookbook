from flask import Flask

from settings import DevConfig

# WSGI app
app = Flask(__name__)

# config
app.config.from_object(DevConfig)

@app.route('/')
def index():
    print app.config['CONFIG']
    return "Sup."


if __name__ == "__main__":
    app.run()
