from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """Hello, World!
    i am daxesh chaudhary
    i am doing python coding
    i am also doing my minors in robotics"""
app.run()