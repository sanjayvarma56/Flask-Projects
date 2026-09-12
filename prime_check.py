from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        num = int(request.form["num"])
        if num <= 1:
            result = f"{num} is not a prime number"
        else:
            is_prime = True
    
            for i in range(2,num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result = f"{num} is a prime number"
            else:
                result = f"{num} is not a prime number"
    return render_template("index_prime_check.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
