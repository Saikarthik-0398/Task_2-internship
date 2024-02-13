from flask import Flask, request, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

@app.route('/')
def index():
    return render_template('prog1.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except Exception as e:
        result = "Invalid expression. Error: " + str(e)
    return render_template('prog1.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
