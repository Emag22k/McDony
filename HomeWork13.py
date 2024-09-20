import sqlite3

conn=sqlite3.connect('mydatabase.db')
sql=conn.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, age INTEGER, grade TEXT);')
sql.execute('INSERT INTO students VALUES(1, "damir", 24, "5");')
sql.execute('INSERT INTO students VALUES(2, "konstantin", 25, "5");')
sql.execute('INSERT INTO students VALUES(3, "sasha", 25, "5");')
conn.commit()

def get_student_by_name(s_name):
    print(sql.execute('SELECT name,age,grade FROM students WHERE name=?;',(s_name,)).fetchone())

def update_student_great(mark,s_name):
    sql.execute('UPDATE students SET grade=? WHERE name=?;', (mark,s_name))

def delete_student(s_name):
    sql.execute("DELETE FROM students WHERE name=?;",(s_name,))


while True:

    acts=["1.Информация","2.Обновление","3.Удаление"]
    print('\n'.join(acts))
    act=input("Выберите действие: ")

    if act.lower()=="информация":
        s_name=input('Введите имя студента: ').lower()
        get_student_by_name(s_name)

    elif act.lower()=="обновление":
        s_name=input('Введите имя студента: ').lower()
        mark=input('Введите новую оценку- ')
        update_student_great(mark,s_name)
        print(f'Оценка студента {s_name} успешно изменена')
        conn.commit()

    elif act.lower()== "удаление":
        s_name=input('Введите имя студента: ').lower()
        delete_student(s_name)
        print(f'Студен {s_name} успешно удален')
        conn.commit()

    else:
        print('Error')