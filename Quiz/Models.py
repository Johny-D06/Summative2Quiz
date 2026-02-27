from Quiz.CSVStorage import CSVWriter, CSVReader

class Question:

    allQuestions = []

    def __init__(self, text, subject, answers, correctanswer, difficulty): #constructor to create a question, will get from csv file
        self.text = text
        self.subject = subject
        self.answers = answers
        self.correctanswer = correctanswer
        self.difficulty = int(difficulty)
        #self.difficulty = difficulty #should be at least 1
        Question.allQuestions.append(self)

    def loadAllQuestions(filename):
        """loads all questions from the csv file"""
        csvr = CSVReader()
        csvr.readQuestionFromFile(filenameloc=filename)

    def checkAnswer(self, useranswer): # returns a bool true if correct false if otherwise

        count = 0
        for answer in self.answers:

            if (answer == self.correctanswer):
                break
            count += 1

        if(useranswer == self.correctanswer):
            return True
        else:
            return False

    
    def  getMaxDifficulty(): #checks every question to get the highest difficulty rating
        """Gets the max difficulty in all Questions in the csv file """
        temp = 0
        for question in Question.allQuestions:
            if question.difficulty > temp:
                temp = question.difficulty
        return temp
    
    def getDifficultiesAsList(): #will add each difficulty option to a list for a streamlit cmd to look at
        """puts each difficulty into a list for use on streamlit"""
        difficultylist = []

        count = 0
        while len(difficultylist) < Question.getMaxDifficulty(): #adds a number to the list
            count += 1
            difficultylist.append(count)

        return difficultylist
    
    def addQuestion(csvs: CSVWriter, questiontext, questionsubject, questionanswers, questionanswernum, questiondifficulty):
        """adds a question to the csv reader and to the current running instance"""
        csvs.writeToFile(f"{questiontext},{questionsubject},{questionanswers[0]},{questionanswers[1]},{questionanswers[2]},{questionanswernum},{questiondifficulty}")
        temp = Question(text=questiontext, subject=questionsubject, answers=questionanswers, correctanswer=questionanswernum, difficulty=questiondifficulty)
        




class Session:
    
    sessionQuestions = []
    correctanswers = []
    """adds all the questions in the current session (usually definded by difficulty) that will be asked to the user"""

    def __init__(self, userdifficulty): #constructor to setup Session
        self.correctanswers = [] #instantiated for future class
        self.sessionQuestions = [] #instantiated
        for question in Question.allQuestions: #checks through each question in existence and adds it only if the difficulty level is qual to or less than what is set
            if(int(question.difficulty) <= int(userdifficulty)):
                self.sessionQuestions.append(question)

    def getScore(self):
        """Adds a score for correct questinons"""
        score = sum(int(self.difficulty) for question in self.questions if question.checkAnswer) #adds the difficulty value as an int per correct question, uses function checkAnswer to make sure each question is correct
        return score

    def addCorrectQuestion(self, correctquestion = Question):
        """adds a correct question to a session instance so that they can be reviewed or saved at the end"""
        self.correctanswers.append(correctquestion)

