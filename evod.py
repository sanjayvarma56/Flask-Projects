from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        number = request.form["number"]
        number = int(number)
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
    return render_template("index_evod.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
