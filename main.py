from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"]) / 100
        time = float(request.form["time"])
        interest = principal * rate * time  # Rumus bunga sederhana
        total = principal + interest
        return render_template("result.html", total=total, interest=interest)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


