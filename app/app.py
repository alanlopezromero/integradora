from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

def pagina_no_encontrada(error):
    return "has sido jakiado"

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__== '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)