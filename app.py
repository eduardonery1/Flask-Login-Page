from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/') #where to go and not 404
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)