from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        distance = float(request.form["distance"])
        operation = request.form["operation"]
        if operation == "km_to_miles":
            converted = distance * 0.621371
            result = f"{distance} kilometers is equal to {converted} miles"
        elif operation == "miles_to_km":
            converted = distance / 0.621371
            result = f"{distance} miles is equal to {converted} kilometers"
        elif operation == "m_to_km":
            converted = distance / 1000
            result = f"{distance} meters is equal to {converted} kilometers"
        elif operation == "km_to_m":
            converted = distance * 1000
            result = f"{distance} kilometers is equal to {converted} meters"    
        elif operation == "m_to_cm":
            converted = distance * 100
            result = f"{distance} meters is equal to {converted} centimeters"
        elif operation == "cm_to_m":
            converted = distance / 100
            result = f"{distance} centimeters is equal to {converted} meters"
        elif operation == "m to feet":
            converted = distance * 3.28084
            result = f"{distance} meters is equal to {converted} feet"
        elif operation == "feet to m":
            converted = distance / 3.28084
            result = f"{distance} feet is equal to {converted} meters"
        elif operation == "cm to inches":
            converted = distance * 0.393701
            result = f"{distance} centimeters is equal to {converted} inches"
        elif operation == "inches to cm":
            converted = distance / 0.393701
            result = f"{distance} inches is equal to {converted} centimeters"
        elif operation == "kg_to_pounds":
            converted = distance * 2.20462
            result = f"{distance} kilograms is equal to {converted} pounds"
        elif operation == "pounds_to_kg":
            converted = distance / 2.20462
            result = f"{distance} pounds is equal to {converted} kilograms"
        return render_template("index_unit_con.html", result=result)
    return render_template("index_unit_con.html")
if __name__ == "__main__":
    app.run(debug=True)