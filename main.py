import os
from flask import Flask, render_template

app = Flask(__name__)


def main():
    port = int(os.environ.get("PORT", 5000))
    print(port)
    app.run(host='0.0.0.0', port=port)


@app.route('/')
@app.route('index')
def index():
    return render_template('templates/index.html')


if __name__ == '__main__':
    main()