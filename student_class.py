class Student:
    def __init__(self):
        self.studentId = 'No id'
        self.studentName = 'No name'
        self.pScores = []
        self.aScores = []
        self.mScores = []
        self.eScores = []

    def register(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

    def setPScores(self, pScores):
        self.pScores = pScores

    def setAScores(self, aScores):
        self.aScores = aScores

    def setMScores(self, mScores):
        self.mScores = mScores

    def setEScores(self, eScores):
        self.eScores = eScores

    def getStudentId(self):
        return self.studentId

    def getStudentName(self):
        return self.studentName

    def getPScores(self):
        return self.pScores

    def getAScores(self):
        return self.aScores

    def getMScores(self):
        return self.mScores

    def getEScores(self):
        return self.eScores

    def getFinalScores(self):
        finalScores = 0
        for score in self.getPScores():
            finalScores += score * 0.1
        for score in self.getAScores():
            finalScores += score * 0.2
        for score in self.getMScores():
            finalScores += score * 0.3
        for score in self.getEScores():
            finalScores += score * 0.4

        return finalScores

    def getGrade(self):
        final_scores = self.getFinalScores()
        average = final_scores/len(self.getEScores())
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        elif average >= 50:
            return 'E'
        else:
            return 'F'

    def getReport(self):
        res = ''
        res += self.getStudentId() + '\n' + self.getStudentName() + '\n'
        res += 'pScores: ' + ', '.join(map(str, self.getPScores())) + '\n'
        res += 'aScores: ' + ', '.join(map(str, self.getAScores())) + '\n'
        res += 'mScores: ' + ', '.join(map(str, self.getMScores())) + '\n'
        res += 'eScores: ' + ', '.join(map(str, self.getEScores())) + '\n'
        res += 'final scores: ' + str(self.getFinalScores()) + '\n'
        res += 'grade: ' + self.getGrade()

        return res


student = Student()
student.register('1234', 'John')
student.setPScores([97, 98, 97, 96])
student.setAScores([89, 90, 97, 96])
student.setMScores([79, 80, 82, 81])
student.setEScores([84, 86, 89, 90])
print(student.getReport())
