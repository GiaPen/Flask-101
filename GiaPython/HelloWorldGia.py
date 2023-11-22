from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('snir.html')

@app.route('/page2')
def page2():
    return render_template('ciel.html')

@app.route('/page3')
def page3():
    return render_template('etudes_sup.html')


@app.route('/page4')
def page4():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()