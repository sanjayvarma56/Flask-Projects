from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        number = int(request.form["number"])
        factorial = 1
        for i in range(1,number + 1):
            factorial = factorial * i
        result = f"The factorial of {number} is {factorial}"
        return render_template("index_fact.html", result=result)
    return render_template("index_fact.html")
if __name__ == "__main__":
    app.run(debug=True)