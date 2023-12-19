from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/multiplication')
def multiplication():  # put application's code here
    return render_template('multiplication.html', title='Multiplication')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/get_form')
def get_form():
    return render_template('get_form.html', title='Get Form')

@app.route('/hi')
def hi():
    return render_template('hi.html', title='Hi')

@app.route('/result')
def result():
    return render_template('result.html', title='Result')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
