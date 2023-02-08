from flask import Flask, render_template, send_file, redirect

app = Flask(__name__)

@app.route('/')
def name_card():
    return render_template("name_card.html")

@app.route('/cv')
def cv():
    return render_template("cv.html")


if __name__ == "__main__":
    app.run(debug=True)
