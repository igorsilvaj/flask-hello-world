from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.jinja2")


@app.route("/teste")
def teste():
    return 'teste'


@app.route("/<hello_again>")
def hello_world_again(hello_again):
    return render_template("home.jinja2", hello_again=hello_again)


# if __name__ == "__main__":
#     app.run(debug=True)
