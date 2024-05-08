from flask import Flask , render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/1")
def home1():
    return render_template("/login.html")

@app.route("/2")
def home2():
    return render_template("/contact.html")

@app.route("/3")
def home3():
    return render_template("/game.html")
@app.route("/4")
def family():
    return render_template("/numbers.html")







if __name__ == "__main__":
    app.run(debug= True, port = 8000)