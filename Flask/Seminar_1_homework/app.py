from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def index():
    """
    Главная страница сайта
    """
    return render_template('index.html')


@app.route("/clothers/")
def clothers_page():
    """
    Страница одежда
    """
    return render_template('clothers.html')


@app.route("/boots/")
def boots_page():
    """
    Cтраница обувь
    """
    return render_template('boots.html')


@app.route("/hats/")
def hats_page():
    """
    Cтраница головные уборы
    """
    return render_template('hats.html')


if __name__ == "__main__":
    app.run(debug=True)


# Просто комментарий чтобы сделать пулл реквест, следующий раз сразу отделю ветку