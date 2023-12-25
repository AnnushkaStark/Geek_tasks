from flask import Flask, render_template

app = Flask(__name__)


@app.route("/sum/<int:a>_<int:b>/")
def sum_ab(a, b):
    return str(a + b)


@app.route("/strng/<strng>/")
def lenght(strng):
    return f"Длина строки {len(strng)}"


@app.route('/')
def my_page():
    
    return '''<h1> Hello world </h1>'''

@app.route('/students/')
def stud_list():
    people = [
        {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': 20,
         'Средний бал': 4.5},
        {'Имя': 'Петр', 'Фамилия': 'Петров', 'Возраст': 21,
         'Средний бал': 4.2},
        {'Имя': 'Сергей', 'Фамилия': 'Сергеев', 'Возраст': 19,
         'Средний бал': 4.8},
        {'Имя': 'Анна', 'Фамилия': 'Иванова', 'Возраст': 20,
         'Средний бал': 4.7}
    ]
    return render_template('students.html',students =people)




if __name__ == "__main__":
    
    app.run(debug=True)
