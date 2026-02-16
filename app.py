from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    income = float(request.form['income'])
    expenses = float(request.form['expenses'])

    savings = income - expenses

    if expenses > income:
        advice = "You are overspending!"
    elif savings > income * 0.3:
        advice = "Good saving habit!"
    else:
        advice = "Try to save more."

    return render_template("result.html", income=income, expenses=expenses, savings=savings, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
