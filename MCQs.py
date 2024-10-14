class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.solution = solution

    def get_question(self):
        return self.question

    def get_answer1(self):
        return self.answer1

    def get_answer2(self):
        return self.answer2

    def get_answer3(self):
        return self.answer3

    def get_answer4(self):
        return self.answer4

    def get_solution(self):
        return self.solution

    def set_question(self, question):
        self.question = question

    def set_answer1(self, answer1):
        self.answer1 = answer1

    def set_answer2(self, answer2):
        self.answer1 = answer2

    def set_answer3(self, answer3):
        self.answer1 = answer3

    def set_answer4(self, answer4):
        self.answer1 = answer4

    def set_solution(self, solution):
        self.solution = solution

    def __str__(self):
        return '{}\nOptions\n{}\n{}\n{}\n{}\n'.format(self.question, self.answer1, self.answer2, self.answer3, self.answer4)


questions = []
question1 = Question('OS computer abbreviation usually means?', 'Order of Significance', 'Open Software', 'Operating '
                                                                                                          'System',
                     'Optical Sensor', 'c')
question2 = Question('.MOV extension refers usually to what kind of file?', 'Image file', 'Animation/movie file', 'Audio file', 'MS Office document', 'b')
question3 = Question('.MPG extension refers usually to what kind of file', 'Word Perfect Document file', 'MS Office '
                                                                                                         'document',
                     'Animation/movie file', 'Image file', 'c')
question4 = Question('What is part of a database that holds only one type of information?', 'Report', 'Field', ' Record', 'File', 'b')
question5 = Question('Who developed Yahoo?', 'Dennis Ritchie & Ken Thompson', 'David Filo & Jerry Yang', 'Vint Cerf & '
                                                                                                         'Robert '
                                                                                                         'Kahn',
                     'Steve Case & Jeff Bezos', 'b')
question6 = Question('DB computer abbreviation usually means?', ' Database', 'Double Byte', 'Data Block', 'Driver Boot', 'a')
question7 = Question('INI extension refers usually to what kind of file?', 'Image file', 'System file', 'Hypertext '
                                                                                                        'related '
                                                                                                        'file',
                     ' Image Color Matching Profile file', 'b')
question8 = Question('The sampling rate, (how many samples per second are stored) for a CD is?', '48.4 kHz', '22,050 Hz', '44.1 kHz', '48 kHz', 'c')
question9 = Question('What do we call a network whose elements may be separated by some distance? It usually involves '
                     'two or more small networks and dedicated high-speed telephone lines.', 'URL (Universal Resource '
                                                                                             'Locator)', 'LAN (Local '
                                                                                                         'Area '
                                                                                                         'Network)',
                     'WAN (Wide Area Network)', 'World Wide Web', 'c')
question10 = Question('Sometimes computers and cache registers in a food mart are connected to a UPS system. What does '
                      'UPS mean?', 'United Parcel Service', 'Uniform Product Support', 'Under Paneling Storage',
                      'Un interruptable Power Supply', 'd')
question11 = Question('What is FMD?', 'Fast-Ethernet Measuring Device', 'Flashing Media Diode', 'Fluorescent '
                                                                                                'Multi-Layer Disc',
                      'Flash Media Driver', 'c')
question12 = Question('Which of these is a documented hoax virus?', 'McDonalds screensaver', 'Alien.worm', 'Merry Xmas', 'Adolph', 'a')
question13 = Question('What does SSL stand for?', 'Secure Socket Layer', 'System Socket Layer', 'Superuser System Login', 'Secure System Login', 'a')
question14 = Question('What is a URL?', 'A computer software program', 'A type of UFO', 'The address of a document or '
                                                                                        '"page" on the World Wide '
                                                                                        'Web', 'An acronym for '
                                                                                               'Uniform Resources '
                                                                                               'Learning', 'c')
question15 = Question('In which language UNIX is written?', ' C++', 'C', ' JAVA', ' Python', 'b')
questions.append(question1)
questions.append(question2)
questions.append(question3)
questions.append(question4)
questions.append(question5)
questions.append(question6)
questions.append(question7)
questions.append(question8)
questions.append(question9)
questions.append(question10)
questions.append(question11)
questions.append(question12)
questions.append(question13)
questions.append(question14)
questions.append(question15)
print('-----------Student 1----------')
print()
player1_correct_answers = 0
for i in range(5):
    print(questions[i])
    choice = input('Enter your choice (A, B , C, D): ')
    if choice.lower() == questions[i].solution:
        player1_correct_answers += 1

print('The number of answers correctly answered by Student 1 is {}'.format(player1_correct_answers))
player2_correct_answers = 0
print()
print('----------Student 2----------')
print()
for i in range(5, 10):
    print(questions[i])
    choice = input('Enter your choice (A, B , C, D): ')
    if choice.lower() == questions[i].solution:
        player2_correct_answers += 1

print('The number of answers correctly answered by Student 2 is {}'.format(player2_correct_answers))

print('----------Student 3----------')
print()
player3_correct_answers = 0
for i in range(10, 15):
    print(questions[i])
    choice = input('Enter your choice (A, B , C, D): ')
    if choice.lower() == questions[i].solution:
        player3_correct_answers += 1

print('The number of answers correctly answered by Student 3 is {}'.format(player3_correct_answers))
