from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def home():
    characters = 0
    if request.method == "POST":
        text = request.form["text"]
        characters = len(text)
        return render_template("index_char_count.html", characters=characters)
    return render_template("index_char_count.html")
if __name__ == "__main__":
    app.run(debug = True)   
    