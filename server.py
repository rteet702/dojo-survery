from flask import Flask

app = Flask(__name__)
app.secret_key = 'tiamat is the best'

if __name__ == '__main__':
    app.run(debug=True)