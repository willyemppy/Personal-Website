from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/home/")
def homepage():
    return render_template('index.html')
@app.route("/contacts")
def contact():
    return render_template('contact.html')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('contact'))

if __name__ == '__main__':
    app.run()