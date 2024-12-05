from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello PradeepIT, Good morning!'

if __name__ == '__main__':
    # Bind to 0.0.0.0 to make the app accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
