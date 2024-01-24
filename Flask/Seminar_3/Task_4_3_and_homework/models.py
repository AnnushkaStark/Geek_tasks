from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """
    Moдель пользователя
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    # Добавим уникальность чтобы с одной почты можно было зарегистрировать  только один аккаунт
    email = db.Column(db.String(40), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)


class Faculty(db.Model):
    """
    Модель факультет из семинара
    """

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    students = db.relationship("Student", backref=db.backref("faculty_id"), lazy=True)

    def __str__(self):
        return f"{self.title}"


class Student(db.Model):
    """
    Moдель студент из семинра
    """

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_pk = db.Column(db.Integer, db.ForeignKey("faculty.pk"), nullable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.age} {self.gender} {self.group}"


class Rates(db.Model):
    """
    Модель оценка (из семинара)
    """

    pk = db.Column(db.Integer, primary_key=True)
    student_pk = db.Column(db.Integer, db.ForeignKey("student.pk"), nullable=False)
    subject_title = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.subject_title
