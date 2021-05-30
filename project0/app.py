from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hallo"
    return render_template("flask.html", name=name)

if __name__ == '__main__':
    app.run()