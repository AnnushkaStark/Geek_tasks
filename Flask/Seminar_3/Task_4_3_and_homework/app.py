from flask import (
    Flask,
    render_template,
    redirect,
    session,
    flash,
    get_flashed_messages,
    request,
    url_for,
)
from models import db, User, Faculty, Rates, Student
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "WeryLongSeretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db.init_app(app)


@app.cli.command("init_db")
def create():
    """
    Создание базы данных
    """
    db.create_all()


@app.cli.command("add_faculties")
def add_all_faculty():
    """
    Заполение таблиц базы данных Факультет
    """
    facultetes = ["Химия", "Физика", "Биология", "Экономика", "Менеджмент"]
    for title in facultetes:
        new_facultet = Faculty(title=title)
        db.session.add(new_facultet)
    db.session.commit()


@app.cli.command("add_students")
def add_all_sttudents():
    """
    Заполение таблицы базы данных студенты
    """
    students = [
        ("Ivan", "Ivanov", "my@mail.mail", 30, "M", 101, 1),
        ("Maria", "Andreeva", "my@mail_1.mail", 25, "F", 102, 2),
        ("Maksim", "Maksimov", "my@mail_2.mail", 22, "M", 201, 3),
        ("Evgenii", "Evgenev", "my@mail_3.mail", 31, "M", 203, 4),
        ("Olga", "Olegovna", "my@mail_4.mail", 34, "F", 101, 5),
    ]
    for student in students:
        first_name, last_name, email, age, gender, group, faculty = student
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
            group=group,
            faculty_pk=faculty,
        )
        db.session.add(new_student)
    db.session.commit()


@app.cli.command("add_rates")
def add_all_rates():
    rates = [
        (1, "Химия", 3),
        (2, "Биология", 2),
        (3, "Физика", 3),
        (4, "Экономика", 4),
        (5, "Менеджмент", 5),
    ]
    for rate in rates:
        new_rate = Rates(student_pk=rate[0], subject_title=rate[1], score=rate[2])
        db.session.add(new_rate)
    db.session.commit()


@app.route("/")
def index():
    """
    Просто главная страница
    """
    return render_template("index.html")


@app.route("/register/", methods=["GET", "POST"])
def register_page():
    """
    Страница регистрации
    """
    if request.method == "POST":
        form = RegisterForm()
        try:
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            password = request.form["password"]
            password_2 = request.form["password_2"]
            if password == password_2:
                password_hash = generate_password_hash(password)
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password_hash=password_hash,
                )
                db.session.add(new_user)
                db.session.commit()
                db.session.close()
                flash("Вы успешно зарегистированы")
                return redirect(url_for("login_page"))
            flash("Некорректный ввод данных")
            return redirect(url_for("register_page"))
        except Exeptions as e:
            flash("Пользовтель с таким email уже стуществует")
            return redirect(url_for("register_page"))
    return render_template("register.html")


@app.route("/login/", methods=["GET", "POST"])
def login_page():
    """
    Страница входа
    """
    if request.method == "POST":
        form = LoginForm()
        try:
            form_email = request.form["email"]
            form_password = request.form["password"]
            user = User.query.filter_by(email=form_email).first()
            if user and check_password_hash(user.password_hash, form_password):
                session["first_name"] = user.first_name
                session["email"] = form_email
                flash(f"Привет {user.first_name}")
                return redirect(url_for("user", username=session["first_name"]))
            print(user.password_hash)
            flash("Пользователь не найден")
            return redirect(url_for("login_page"))
        except Exeptions as e:
            flash("Ошибка ввода данных")
            return redirect(url_for("login_page"))
    return render_template("login.html")


@app.route("/user/<string:username>/", methods=["GET", "POST"])
def user(username, *args, **kwargs):
    """
    Старница пользователя
    вывод оценок студентов (задача с семинара)
    """
    if session:
        scores_list = {}
        for student in Student.query.all():
            temp = Rates.query.filter(Rates.student_pk == student.pk).all()
            scores_list[student] = temp or []

        context = {
            "scores_list": scores_list,
            "title": "Студенты и оценки",
        }
        if request.method == "POST":
            session.clear()
            flash("Спасибо за посещение нащего сайта")
            return redirect(url_for("index"))
        return render_template("user.html", **context)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
