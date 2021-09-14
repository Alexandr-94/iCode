class Ac_prog:

    def __init__(self):
        self.name_students = None
        self.age_students = None
    def students(self):
        import bd_students

        print('''вам доступны следующие функции\n
        1. Просмотор список студентов.\n
        2. Добавление новых студентов.\n
        3. Удаление студентов из списка.\n
        4. Редактирование списка.\n''')
        choses_students = input('Введите номер операции')
        if choses_students == '1':
            print(bd_students.inf)
        elif choses_students == '2':
            self.name_students = input('Введите Ф.И.О')
            self.age_students = input('Введите возраст')
            print(self.name_students)
            print(self.age_students)
    def teacher(self):
        pass

    def group(self):
        pass


    def item(self):
        pass


print('''Вас приветствует программа учета студентов и преподавателей,
\n что бы вы хотели сделать? выберите номер\n
 1. Студенты\n
 2. Преподаватели\n
 3. Группы\n
 4. Предметы''')
ac = Ac_prog()
choses = input('введите номер')
if choses == '1':
    ac.students()
elif choses == '2':
    ac.teacher()
elif choses == '3':
    ac.group()
elif choses == '4':
    ac.item()

name_students = ac.students()