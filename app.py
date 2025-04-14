from flask import Flask, render_template

app = Flask(__name__)

@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)

