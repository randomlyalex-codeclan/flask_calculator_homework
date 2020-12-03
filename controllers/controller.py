from app import app
from modules.calculator import Calculator

@app.route('/')
def index():
    return "Please use the url bar to either add, divde, subtract or divde two numbers separated by a /"

@app.route('/add/<number_1>/<number_2>')
def add(number_1, number_2):
    return str(Calculator.add_two_numbers(number_1, number_2))


@app.route('/subtract/<number_1>/<number_2>')
def subtract(number_1, number_2):
    return str(Calculator.subtract_two_numbers(number_1, number_2))

@app.route('/divide/<number_1>/<number_2>')
def multiply(number_1, number_2):
    return str(Calculator.multiply_two_numbers(number_1, number_2))

@app.route('/multiply/<number_1>/<number_2>')
def divide(number_1, number_2):
    return str(Calculator.divide_two_numbers(number_1, number_2))