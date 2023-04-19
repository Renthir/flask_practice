from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/info')
def info():
    return '<h1>This is a new website!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return f"<h1>This is {name}'s page<h1>"


@app.route('/puppy_latin/<word>')
def user(word):
    pup_word = ''
    if word[-1] == 'y':
        pup_word = word[:-1] + 'iful'
    else:
        pup_word = word + 'y'
    return f"<h1>{pup_word}<h1>"

if __name__ == '__main__':
    app.run(debug=True)