

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def gr_average_hw(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            len_grade += len(course)
        if sum_grade == 0:
            return f'Нет оценок'
        return round(sum_grade / len_grade, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Сравнивать можно только студентов со студентами!'
        return self.gr_average_hw() < other.gr_average_hw()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Сравнивать можно только студентов со студентами!'
        return self.gr_average_hw() == other.gr_average_hw()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {self.gr_average_hw()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def gr_average(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            len_grade += len(course)
        if sum_grade == 0:
            return f'Нет оценок'
        return round(sum_grade / len_grade, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнивать можно только лекторов с лекторами!'
        return self.gr_average() < other.gr_average()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Сравнивать можно только лекторов с лекторами!'
        return self.gr_average() == other.gr_average()
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.gr_average()}'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def all_st_gr_average(st_list, ttl_course):
    sum_av_all = 0
    q_st = 0
    for st in st_list:
        sum_g = 0
        if ttl_course in st.grades:
            sum_g = sum(st.grades[ttl_course])
            sum_av_all += sum_g / len(st.grades[ttl_course])
            q_st += 1
    if sum_av_all == 0:
        return f'На курсе {ttl_course} нет оценок'
    else:
        return f'Средняя оценка по курсу {ttl_course} для всех студентаов: {round(sum_av_all / q_st, 1)}'
        
def all_lr_gr_average(lr_list, ttl_course):
    sum_av_all = 0
    q_lr = 0
    for lr in lr_list:
        sum_g = 0
        if ttl_course in lr.grades:
            sum_g = sum(lr.grades[ttl_course])
            sum_av_all += sum_g / len(lr.grades[ttl_course])
            q_lr += 1
    if sum_av_all == 0:
        return f'На курсе {ttl_course} нет оценок'
    else:
        return f'Средняя оценка по курсу {ttl_course} для всех лекторов: {round(sum_av_all / q_lr, 1)}'
        

student_1 = Student('Иван', 'Иванов', 'Male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['C++']

student_2 = Student('Анна', 'Петрова', 'Female')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['C++']


lecturer_1 = Lecturer('Петр', 'Васильев')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Виктор', 'Многознаев')
lecturer_2.courses_attached += ['Python', 'Git']


reviewer_1 = Reviewer('Олег', 'Знающий')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer('Ольга', 'Справедливая')
reviewer_2.courses_attached += ['Python']
 
student_1.rate_lect(lecturer_1, 'Python', 9)
student_1.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Python', 10)

student_2.rate_lect(lecturer_2, 'Python', 10)
student_2.rate_lect(lecturer_2, 'Python', 10)
student_2.rate_lect(lecturer_2, 'Python', 10)


reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)

reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Git', 10)

print('-'*20)
print('Студенты:')
print()
print(student_1)
print()
print(student_2)
print()
print('-'*20)
print('Лекторы:')
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print('-'*20)
print('Ревьюверы:')
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print('-'*20)
print('Работа метода __lt__ (лектор_1 < лектор_2):')
print(lecturer_1.__lt__(lecturer_2))
print('-'*20)
print('Работа метода __lt__ (лектор_1 < студента_1):')
print(lecturer_1.__lt__(student_1))

st_list = [student_1, student_2]
lr_list = [lecturer_1, lecturer_2]
print('-'*20)
print('Работа функции средняя оценка по студентам:')
print(all_st_gr_average(st_list, 'Git'))
print('-'*20)
print('Работа функции средняя оценка по лекторам:')
print(all_lr_gr_average(lr_list, 'Python'))


