from flask import Flask, render_template, request
import random
app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        guess = int(request.form["guess"])
        number = random.randint(1, 10)
        if guess > number:
            message = f"Your guess {guess} is too high. The number was {number}."
        elif guess < number:
            message = f"Your guess {guess} is too low. The number was {number}."
        else:
            message = f"Congratulations! Your guess {guess} is correct."    
    return render_template("index_numguess.html", message=message)
if __name__ == "__main__":
    app.run(debug=True)
