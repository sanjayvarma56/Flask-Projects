from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        num1 = int(num1)
        num2 = int(num2)
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        return render_template("index_calci.html",result = result)
    return render_template("index_calci.html")
if __name__ == "__main__":
    app.run(debug=True)