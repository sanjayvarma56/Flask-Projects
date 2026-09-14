from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def home():
    words = 0
    if request.method == "POST":
        text = request.form["text"]
        words = len(text.split())
        return render_template("index_word_count.html", words=words)
    return render_template("index_word_count.html")
if __name__ == "__main__":
    app.run(debug = True)