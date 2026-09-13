from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        number = int(request.form["number"])
        original = number
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number = number // 10
        if original == reverse:
            result = f"{original} is a palindrome number"
        else:
            result = f"{original} is not a palindrome number"
    return render_template("index_palindrome_num1.html", result=result)         
if __name__ == "__main__":
    app.run(debug=True)