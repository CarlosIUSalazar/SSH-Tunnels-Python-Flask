from flask import Flask

app2 = Flask(__name__)

@app2.route('/')
def index():
    return '<h1 style="color:red;">This is the the super secret page</h1>'

if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5002)