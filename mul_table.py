from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    table = None
    number = None
    if request.method == "POST":
        number = int(request.form["number"])
        table = []
        for i in range(1,21):
            result = number * i
            table.append(result)
        return render_template("index_mul_table.html",table=table,number=number)
    return render_template("index_mul_table.html",table = table,number = number)
if __name__ == "__main__":
    app.run(debug=True)