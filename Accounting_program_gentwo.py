import sqlite3
class Ac_prog:

    def __init__(self):
        # self.students = students
        # self.age_students = None
        pass
    def students(self):
        while True:
            print('''вам доступны следующие функции\n
            1. Просмотор список студентов.
            2. Добавление новых студентов.
            3. Удаление студентов из списка.
            4. Редактирование списка.''')
            choses_students = input('Введите номер операции')
            if choses_students == '1':
                cursor.execute('''SELECT*FROM tab_students''')
                students = cursor.fetchall()
                print(students)

            elif choses_students == '2':
                self.name_students = input('Введите Ф.И.О')
                self.date_students = input('Введите дату рождения')
                self.age_students = input('Введите возраст')
                cursor.execute('''INSERT INTO tab_students(name, date, age ) VALUES (?,?,?)''', (self.name_students, self.date_students, self.age_students))
                conn.commit()
                print(self.name_students)
                print(self.date_students)
                print(self.age_students)

            elif choses_students == '3':
                cursor.execute('''SELECT*FROM tab_students''')
                students = cursor.fetchall()
                print('вы хотите когото удалить! ', students)
                self.del_students = input('введите номер студента')
                print('Вы его удалили', '\U0001F62A')
                cursor.execute('''DELETE FROM tab_students WHERE id = ?''', (self.del_students))
                conn.commit()

            elif choses_students == '4':
                cursor.execute('''SELECT*FROM tab_students''')
                students = cursor.fetchall()
                print('Введите что вы хотите поменять', students)
                self.id_students = int(input('Введите номер студента'))
                self.new_id_students = int(input('Введите новй ID'))
                self.upd_name_students = input('Введите новое Ф.И.О')
                self.upd_date_students = input('Введите новую дату рождения')
                self.upd_age_students = input('Введите новый возраст')
                cursor.execute('''UPDATE tab_students SET id=?, name=?, date=?, age=? WhERE id=?''',(self.new_id_students,self.upd_name_students,self.upd_date_students,self.upd_age_students,self.id_students,))
                conn.commit()
                cursor.execute('''SELECT*FROM tab_students''')
                students = cursor.fetchall()
                print('Изменения прошли удачно, спасибо', students)


    def teacher(self):
        pass
    def group(self):
        pass
    def item(self):
        pass

conn = sqlite3.connect('accounting.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, age TEXT)''')
cursor.execute('''SELECT*FROM tab_students''')
students = cursor.fetchall()


cursor.execute('''CREATE TABLE IF NOT EXISTS tab_teacher(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rank TEXT, age TEXT)''')
cursor.execute('''SELECT*FROM tab_students''')
teacher = cursor.fetchall()



print('''Вас приветствует программа учета студентов и преподавателей,
\n что бы вы хотели сделать? выберите номер\n
 1. Студенты
 2. Преподаватели
 3. Группы
 4. Предметы''')
ac = Ac_prog()
choses = input('введите номер')
while True:
    if choses == '1':
        ac.students()
    elif choses == '2':
        ac.teacher()
    elif choses == '3':
        ac.group()
    elif choses == '4':
        ac.item()
    else:
        break
cursor.execute("""SELECT *, tab_students.name FROM tab_1
    LEFT JOIN tab_2 ON tab_2.col_1=tab_1.col_1;""")
n = cursor.fetchall()
print('обединение',n)