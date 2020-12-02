from app import app
from modules import calculator

@app.route('/')
def index():
    return "Hello, World"

# @app.route('/<name>')
# def greet(name):
#     return f"Hello, {name}"

# @app.route('/news')
# def news():
#     return "Here is the news"

# @app.route('/data/<name>/<age>')
# def data(name, age):
#     return f"Name is {name} is {int(age) + 1} years old"