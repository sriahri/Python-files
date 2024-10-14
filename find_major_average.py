class Student:
    def __init__(self, new_name, new_id, new_major, new_courses):
        self.name = new_name
        self.num = new_id
        self.major = new_major
        self.courses = new_courses

    def __eq__(self, other) -> bool:
        return isinstance(other, Student) and \
               self.name == other.name and \
               self.num == other.num and \
               self.major == other.major and \
               self.courses == other.courses

    def __repr__(self) -> str:
        return 'Name: {0}\nID: {1}\nMajor: {2}\nCourses: {3}.format(self.name, self.num, self.major, self.courses'


def current_year_major_average(s, current_year):
    start_year = (s.num // 1000) % 10000
    study_year = current_year - start_year + 1
    major_subject = s.major
    x = major_subject.split()
    acronym = ''
    total_marks = 0
    number_of_marks = 0
    if len(x) == 1:
        acronym += x[:4]
    else:
        for i in x:
            acronym += i[0]
    for i in s.courses.keys():
        if acronym == i[:len(acronym)]:
            if study_year == 1:
                if int(i[2:]) >= 100:
                    total_marks += sum(s.courses[i])
                    number_of_marks += len(s.courses[i])
            elif study_year == 2:
                if int(i[2:]) >= 200:
                    total_marks += sum(s.courses[i])
                    number_of_marks += len(s.courses[i])
            elif study_year == 3:
                if int(i[2:]) >= 300:
                    total_marks += sum(s.courses[i])
                    number_of_marks += len(s.courses[i])
            else:
                if int(i[2:]) >= 400:
                    total_marks += sum(s.courses[i])
                    number_of_marks += len(s.courses[i])
    return total_marks/number_of_marks


student = Student('Acacia Jones', 882020888, "Computer Science",
                  {'HIST200': [88], 'CS115': [43, 55], 'CS116': [100], 'MATH135': [77], 'CS222': [78, 80],
                   'CS445': [82]})
print(current_year_major_average(student, 2021))
