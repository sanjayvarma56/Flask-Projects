from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        word = request.form["word"]
        if word == word[::-1]:
            result = f"{word} is a palindrome"
        else:
            result = f"{word} is not a palindrome"
    return render_template("index_palindrome.html", result=result)
if __name__ == "__main__":
    app.run(debug=True) 