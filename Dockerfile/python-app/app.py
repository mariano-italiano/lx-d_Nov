from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Simple docker container application"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
