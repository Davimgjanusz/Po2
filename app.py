from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/passagens')
def passagens():
    return render_template('passagens.html')

if __name__ == '__main__':
    app.run(debug = True)