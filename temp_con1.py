from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        unit = request.form["unit"]
        if unit == "C":
            converted = (temperature * 9/5) + 32
            result = f"{temperature}°C is equal to {converted}°F"
        elif unit == "F":
            converted = (temperature - 32) * 5/9
            result = f"{temperature}°F is equal to {converted}°C"
        return render_template("index_temp_con1.html", result=result)
    return render_template("index_temp_con1.html")
if __name__ == "__main__":
    app.run(debug=True) 
