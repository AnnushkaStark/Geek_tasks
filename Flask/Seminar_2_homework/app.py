from flask import (
    Flask,
    render_template,
    redirect,
    make_response,
    request,
    session,
    url_for,
)


app = Flask(__name__)
app.secret_key = "WeryLongSeretKey"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Страница с формой ввода
    пользовательских данных
    """
    if request.method == "POST":
        response = make_response("Cookies")
        username = request.form.get("username")
        email = request.form.get("email")
        if len(email) != 0 and len(username) != 0:
            cookie_name = response.set_cookie("username", value="username", max_age=None)
            cookie_mail = response.set_cookie("email", value="email", max_age=None)
            session["usename"] = username
            print(request.form)
            print(response)
            return redirect(url_for("user", username=username))
        return redirect(url_for("index"))
    return render_template("index.html")


@app.route("/user/<string:username>/", methods=["GET", "POST"])
def user(username, *args, **kwargs):
    """
    Старница приветствия ползователя
    """
  
    if session:
        if request.method == "POST":
            response = make_response("Cookie clear")
            if request.cookies.get("sessionid") and request.cookies.get("session"):
                response.set_cookie("username", "", expires=0)
                response.set_cookie("email", "", expires=0)
                print('Cookie удалены')
                session.clear()
                return redirect(url_for("index"))
            print(request.cookies)
            print(response)
            print("Не удалось очистить Cookie")
            return redirect(url_for("index"))
        return render_template("user.html", username=username)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
