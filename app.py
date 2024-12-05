from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello PradeepIT, Good morning This is nagaraj here and this is the testing purpose"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
