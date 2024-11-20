from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj Świecie!</h1><a href='/test'>Przejdz do storny test</a> "


@app.route("/test")
def test():
    return "<p>Storna Testowa</p><a href='/'>Wróc</a>"

app.run(debug=True)