# Constants used to refer to the parts of the quiz question
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

#
# Splits a String containing all question information, then
# returns the specified part of the question
#

#
# Single string containing CSV formatted quiz question
#  "category,pointvalue,question,answer"
#
singleQuestionCSV = "Cats,100,Cats hate this,water"

pieces = singleQuestionCSV.split(',')
print("Category: {}".format(pieces[0]))
print("Value: {}".format(pieces[1]))
print("Question: {}".format(pieces[2]))
print("Answer: {}".format(pieces[3]))


#
# Parameters
#   question - String containing comma separated quiz question details
#   whichInfo - constant representing which part of the question to return
#                should be one of CATEGORY, VALUE, QUESTION, ANSWER
# Return
#   String containing the specified part of the question
def getInfo(question, whichInfo):
    pieces = question.split(',')
    if whichInfo.upper() == 'CATEGORY':
        return pieces[0]
    elif whichInfo.upper() == 'VALUE':
        return pieces[1]
    elif whichInfo.upper() == 'QUESTION':
        return pieces[2]
    elif whichInfo.upper() == 'ANSWER':
        return pieces[3]


#
# List of strings containing CSV formatted quiz data
#
print()
print(getInfo(singleQuestionCSV, 'CATEGORY'))
print()
questionList = ["Dinos,500,My existence has been debated but I have very long neck,brontosaurus",
                "Cats,200,This killed the cat,curiosity",
                "Math,200,Square me to get 100,10",
                "Dinos,100,Famous carnivore,t-rex",
                "Cats,400,Tiger + Lion =,liger",
                "Dinos,400,Turns out dinosaurs were covered in these,feathers",
                "Math,200,You wish you could eat this numerical constant,pi",
                "Math,400,It measures round and round and round,circumference",
                "Math,100,2 + 2 =,4",
                "Dinos,200,They have three horns,triceratops"]

print('There are {} questions'.format(len(questionList)))
print('Category -- Value')
for i in range(len(questionList)):
    question = questionList[i]
    info = question.split(',')
    print('{} -- {}'.format(info[0], info[1]))
