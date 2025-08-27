from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/passagens')
def passagens():
    return render_template('passagens.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/suporte')
def suporte():
    return render_template('suporte.html')

if __name__ == '__main__':
    app.run(debug = True)