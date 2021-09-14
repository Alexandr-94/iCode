import sqlite3
# Создаем класс студенты в нем описываем основной функционал
class Students:

    def __init__(self):
        pass
    def watch(self):
        cursor.execute('''SELECT*FROM tab_students''')
        students = cursor.fetchall()
        print(students)
    def insert(self):
        self.name = input('Введите Ф.И.О')
        cursor.execute('''INSERT INTO tab_students(name) VALUES (?)''',
                       (self.name,))
        conn.commit()
        print(self.name)


    def delete(self):
        cursor.execute('''SELECT*FROM tab_students''')
        students = cursor.fetchall()
        print('вы хотите когото удалить! ', students)
        self.del_one = input('введите номер студента')
        print('Вы его удалили', '\U0001F62A')
        cursor.execute('''DELETE FROM tab_students WHERE id = ?''', (self.del_one))
        conn.commit()

    def select(self):
        cursor.execute('''SELECT*FROM tab_students''')
        students = cursor.fetchall()
        print('Введите что вы хотите поменять', students)
        self.id = int(input('Введите номер студента'))
        self.new_id = int(input('Введите новй ID'))
        self.upd_name = input('Введите новое Ф.И.О')
        cursor.execute('''UPDATE tab_students SET id=?, name=? WhERE id=?''',
                       (self.new_id,
                        self.upd_name,
                        self.id,))
        conn.commit()

# Создаем 2 класс преподаватели его дочерним от студентов поскольку у нас одинаковый функционал нам не требуется
# каждый класс делать полностью занова


class Teache(Students):
    def __init__(self):
        super().__init__()

    def watch(self):
        cursor.execute('''SELECT*FROM tab_teacher''')
        teacher = cursor.fetchall()
        print(teacher)

    def insert(self):
        self.name = input('Введите Ф.И.О')
        cursor.execute('''INSERT INTO tab_teacher(name ) VALUES (?)''',
                       (self.name,))
        conn.commit()
        print(self.name)

    def delete(self):
        cursor.execute('''SELECT*FROM tab_teacher''')
        teacher = cursor.fetchall()
        print('вы хотите когото удалить! ', teacher)
        self.del_one = input('введите номер преподавателя')
        print('Вы его удалили', '\U0001F62A')
        cursor.execute('''DELETE FROM tab_teacher WHERE id = ?''', (self.del_one))
        conn.commit()

    def select(self):
        cursor.execute('''SELECT*FROM tab_teacher''')
        teacher = cursor.fetchall()
        print('Введите что вы хотите поменять', teacher)
        self.id = int(input('Введите номер преподавателя'))
        self.new_id = int(input('Введите новй ID'))
        self.upd_name = input('Введите новое Ф.И.О')
        cursor.execute('''UPDATE tab_students SET id=?, name=? WhERE id=?''',
                       (self.new_id,
                        self.upd_name,
                        self.id,))
        conn.commit()

# так же создае 3 класс группы он так же наследует все от класса студенты


class Group(Students):
    def __init__(self):
        super().__init__()

    def watch(self):
        cursor.execute('''SELECT*FROM tab_groups''')
        group = cursor.fetchall()
        print(group)

    def insert(self):
        self.name = input('Введите Группу')
        cursor.execute('''INSERT INTO tab_groups(grupp) VALUES (?)''',
                       (self.name,))
        conn.commit()
        print(self.name)

    def delete(self):
        cursor.execute('''SELECT*FROM tab_groups''')
        group = cursor.fetchall()
        print('вы хотите когото удалить! ', group)
        self.del_one = input('введите номер группу')
        print('Вы его удалили', '\U0001F62A')
        cursor.execute('''DELETE FROM tab_groups WHERE id = ?''', (self.del_one,))
        conn.commit()

    def select(self):
        cursor.execute('''SELECT*FROM tab_groups''')
        group = cursor.fetchall()
        print('Введите что вы хотите поменять', group)
        self.id = int(input('Введите номер преподавателя'))
        self.new_id = int(input('Введите новй ID'))
        self.upd_name = input('Введите новое Ф.И.О')
        cursor.execute('''UPDATE tab_groups SET id=?, grupp=? WhERE id=?''',
                       (self.new_id,
                        self.upd_name,
                        self.id,))
        conn.commit()

# так же создае 4 класс предметы он так же наследует все от класса студенты

class Item(Students):
    def watch(self):
        cursor.execute('''SELECT*FROM tab_items''')
        item = cursor.fetchall()
        print(item)

    def insert(self):
        self.name = input('Введите Ф.И.О')
        cursor.execute('''INSERT INTO tab_items(item) VALUES (?)''',
                       (self.name,))
        conn.commit()
        print(self.name)

    def delete(self):
        cursor.execute('''SELECT*FROM tab_items''')
        item = cursor.fetchall()
        print('вы хотите когото удалить! ', item)
        self.del_one = input('введите номер группу')
        print('Вы его удалили', '\U0001F62A')
        cursor.execute('''DELETE FROM tab_items WHERE id = ?''', (self.del_one,))
        conn.commit()

    def select(self):
        cursor.execute('''SELECT*FROM tab_items''')
        item = cursor.fetchall()
        print('Введите что вы хотите поменять', item)
        self.id = int(input('Введите номер преподавателя'))
        self.new_id = int(input('Введите новй ID'))
        self.upd_name = input('Введите новое Ф.И.О')
        cursor.execute('''UPDATE tab_items SET id=?, item=? WhERE id=?''',
                       (self.new_id,
                        self.upd_name,
                        self.id,))
        conn.commit()

# создаем базу данных

conn = sqlite3.connect('accounting.db')
cursor = conn.cursor()
# первая таблица в этой бд будет студенты
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_students(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT)''')
cursor.execute('''SELECT*FROM tab_students''')
students = cursor.fetchall()
# вторая таблица в этой бд будет преподаватели
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_teacher(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT)''')
cursor.execute('''SELECT*FROM tab_teacher''')
teacher = cursor.fetchall()
# третья таблица в этой бд будет группы
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_groups(id INTEGER PRIMARY KEY AUTOINCREMENT,
grupp TEXT)''')
cursor.execute('''SELECT*FROM tab_groups''')
tab_groups = cursor.fetchall()
# и четвертая таблица в этой бд будет предметы
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_items(id INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT)''')
cursor.execute('''SELECT*FROM tab_items''')
tab_items = cursor.fetchall()

# Тут описывается логика обращения к классам
print('''Вас приветствует программа учета студентов и преподавателей,
\n что бы вы хотели сделать? выберите номер\n
 1. Студенты
 2. Преподаватели
 3. Группы
 4. Предметы''')

choses = input('введите номер')
# Тут описывается логика обращения уже к разным объектам класса
while True:
    if choses == '1':
        st = Students()
        print('''вам доступны следующие функции\n
        1. Просмотор список студентов.
        2. Добавление новых студентов.
        3. Удаление студентов из списка.
        4. Редактирование списка.''')
        choses_two = input('Введите номер операции')
        if choses_two == '1':
                st.watch()
        elif choses_two == '2':
                st.insert()
        elif choses_two == '3':
                st.delete()
        elif choses_two == '4':
                st.select()
        else:
            break
    elif choses == '2':
        th = Teache()
        print('''вам доступны следующие функции\n
            1. Просмотор список преподавателей.
            2. Добавление новых преподавателей.
            3. Удаление преподавателей из списка.
            4. Редактирование списка.''')
        choses_two = input('Введите номер операции')
        if choses_two == '1':
            th.watch()
        elif choses_two == '2':
            th.insert()
        elif choses_two == '3':
            th.delete()
        elif choses_two == '4':
            th.select()
        else:
            break

    elif choses == '3':
        gp=Group()
        print('''вам доступны следующие функции\n
                1. Просмотор список групп.
                2. Добавление новых групп.
                3. Удаление групп из списка.
                4. Редактирование списка.''')
        choses_two = input('Введите номер операции')
        if choses_two == '1':
            gp.watch()
        elif choses_two == '2':
            gp.insert()
        elif choses_two == '3':
            gp.delete()
        elif choses_two == '4':
            gp.select()
        else:
            break
    elif choses == '4':
        it=Item()
        print('''вам доступны следующие функции\n
                1. Просмотор список предмет.
                2. Добавление новых предмет.
                3. Удаление предмет из списка.
                4. Редактирование списка.''')
        choses_two = input('Введите номер операции')
        if choses_two == '1':
            it.watch()
        elif choses_two == '2':
            it.insert()
        elif choses_two == '3':
            it.delete()
        elif choses_two == '4':
            it.select()
        else:
            break
    else:
        break

# Объединение немного не понятно, никак не могу понять что не так ((
# cursor.execute("""SELECT *, tab_students.name FROM tab_groups
#     LEFT JOIN tab_students ON tab_students.name=tab_groups.name;""")
# n = cursor.fetchall()
# print('объединение',n)