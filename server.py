from flask import Flask, request, render_template
from calc import Calc

app = Flask(__name__)

values = []

@app.route('/', methods=['POST', 'GET'])
def inp():
    if request.method == 'POST':
        butt = list(request.form.keys())[1]
        if butt == "addVal":
            values.append(request.form['massBox'])
        elif butt == "submit":
            Calc(values)

    return render_template('main.html')


if __name__ == '__main__':
    app.run()