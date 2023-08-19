from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def inp():
    if request.method == 'POST':
        mass = request.form['massBox']
        print(mass)

    return render_template('main.html')


if __name__ == '__main__':
    app.run()