from flask import Flask

app = Flask(__name__)

print(__name__)


def make_bold(func):
    def wrapper_func():
        text = func()
        return f"<b>{text}</b>"
    return wrapper_func


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           '<img src="https://media1.giphy.com/media/yXBqba0Zx8S4/200w.webp?cid' \
           '=ecf05e472f38dx52d68mx6cs51vwrwu71spnern0ztr340d8&rid=200w.webp&ct=g">'


@app.route("/bye")
@make_bold
def Bye_world():
    return "bye!"


if __name__ == "__main__":
    app.run(debug=True)
