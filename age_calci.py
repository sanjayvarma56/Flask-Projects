from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        birth_year = request.form["birth_year"]
        birth_year = int(birth_year)
        current_year = 2026
        age = current_year - birth_year
        return render_template("index_age.html",age = age)
    return render_template("index_age.html")

if __name__ == "__main__":
    app.run(debug = True)
    