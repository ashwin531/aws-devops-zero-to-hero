from flask import Flask
#this is comment goog
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

