from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        operation = request.form["operation"]
        if operation == "c_to_f":
            converted = (temperature * 9/5) + 32
            result = f"{temperature}°C is equal to {converted}°F"
        elif operation == "f_to_c":
            converted = (temperature - 32) * 5/9
            result = f"{temperature}°F is equal to {converted}°C"
        return render_template("index_temp_con.html", result=result)
    return render_template("index_temp_con.html")
if __name__ == "__main__":      
    app.run(debug=True)