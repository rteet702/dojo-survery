from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'tiamat is the best'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    session['form_data'] = request.form
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html', form_data=session['form_data'])

if __name__ == '__main__':
    app.run(debug=True)