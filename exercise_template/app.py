from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    email = request.args.get("email")
    password = request.args.get("password")
    return render_template('result.html',email=email)
if __name__ == "__main__":
     app.run(debug=True)
