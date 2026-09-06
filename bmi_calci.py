from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        height = height / 100  # Convert height from cm to meters
        bmi = weight/ (height * height)
        #bmi = weight / (height ** 2)
        if bmi < 18.5:
            result = f"Your BMI is {bmi:.2f}. You are underweight."
        elif 18.5 <= bmi < 24.9:
            result = f"Your BMI is {bmi:.2f}. You are in normal weight."
        elif 25 <= bmi < 29.9:
            result = f"Your BMI is {bmi:.2f}. You are overweight."
        else:
            result = f"Your BMI is {bmi:.2f}. You are obese."
        return render_template("index_bmi_calci.html", result=result)
    return render_template("index_bmi_calci.html")
if __name__ == "__main__":
    app.run(debug=True)