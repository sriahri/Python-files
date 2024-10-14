class Chapter:
    def __init__(self, number, page, marks, name):
        self.number = number
        self.page = page
        self.marks = marks
        self.name = name

class Exam:
    def __init__(self, examName, chapterList):
        self.examName = examName
        self.chapterList = chapterList
    
    def findMinimumChapterByMarks(self):
        if not self.chapterList:
            return None
        p = []
        for i in self.chapterList:
            p.append(i.marks)
        res = min(p)
        for i in self.chapterList:
            if i.marks == res:
                print(i.number)
                print(i.page)
                print(i.marks)
                print(i.name)
    
    def sortChapterByPage(self):
        if not self.chapterList:
            return None
        m = []
        for i in self.chapterList:
            m.append(i.page)
        m.sort()
        for i in m:
            print(i)

n = int(input())
chli = []
for i in range(n):
    number = input()
    page = int(input())
    marks = int(input())
    name = input()
    ch = Chapter(number, page, marks, name)
    chli.append(ch)
ex = Exam('hello', chli)
ex.findMinimumChapterByMarks()
ex.sortChapterByPage()