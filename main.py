from flask import Flask
from flask import jsonify


def is_palindrome(s1: str) -> bool:
    s1 = ''.join(s1.split(' '))
    print(s1)
    return s1 == s1[::-1]

def has_space(s1: str) -> bool:
    if s1.find(' ') != -1:
        return False
    return True


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! CI/CD ver.2'

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    if(is_palindrome(name)):
        print(f"The name of the route: {name} is a Palindrome")
    else:
        print(f"The name of the route: {name} is not a Palindrome")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# print(is_palindrome('anita lava la tina'))
