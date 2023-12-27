from flask import Flask, render_template, redirect, make_response, request



app = Flask(__name__) 


@app.route('/', methods = ['GET','POST'])
def index():
    """
    Страница с формой ввода
    пользовательских данных
    """
    #if request.method == 'POST':
       #username = request.form.get('username')
       #email = request.form.get('email')
    return render_template("index.html")


@app.route('/user/')
def user():
    """
    Старница приветствия ползователя
    """
    return render_template("user.html")


if __name__ == '__main__':
    app.run()