from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "VexaPay Bot is running successfully!"
