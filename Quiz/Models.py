from dataclasses import dataclass
from Quiz.CSVStorage import CSVWriter, CSVReader

class Question:

    allQuestions = []

    def __init__(self, text, subject, answers, answernum, difficulty): #constructor to create a question, will get from csv file
        self.text = text
        self,subject
        self.answers = answers
        self.answernum = answernum
        self.difficulty = int(difficulty)
        #self.difficulty = difficulty #should be at least 1
        Question.allQuestions.append(self)

    def loadAllQuestions(filename):
        csvr = CSVReader()
        csvr.readQuestionFromFile(filenameloc=filename)

    def checkAnswer(self, useranswer): # returns a bool true if correct false if otherwise
        if(useranswer == self.answer):
            return True
        else:
            return False

    
    def  getMaxDifficulty(): #checks every question to get the highest difficulty rating
        temp = 0
        for question in Question.allQuestions:
            if question.difficulty > temp:
                temp = question.difficulty
        return temp
    
    def getDifficultiesAsList(): #will add each difficulty option to a list for a streamlit cmd to look at
        difficultylist = []

        count = 0
        while len(difficultylist) < Question.getMaxDifficulty(): #adds a number to the list
            count += 1
            difficultylist.append(count)

        return difficultylist
    
    def addQuestion(csvs: CSVWriter, questiontext, questionsubject, questionanswers, questionanswernum, questiondifficulty):
        csvs.writeToFile(f"{questiontext},{questionsubject},{questionanswers[0]},{questionanswers[1]},{questionanswers[2]},{questionanswernum},{questiondifficulty}")
        temp = Question(text=questiontext, subject=questionsubject, answers=questionanswers, answernum=questionanswernum, difficulty=questiondifficulty)
        




class Session:
    
    sessionQuestions = []

    def __init__(self, userdifficulty): #constructor to setup Session
        self.correctanswers = [] #instantiated for future class
        self.sessionQuestions = [] #instantiated
        for question in Question.allQuestions: #checks through each question in existence and adds it only if the difficulty level is qual to or less than what is set
            if(int(question.difficulty) <= int(userdifficulty)):
                self.sessionQuestions.append(question)

    def getScore(self):
        score = sum(2 for question in self.questions if question.checkAnswer) #adds 2 point per correct question, uses function checkAnswer to make sure each question is correct
        return score

    def addCorrectQuestion(self, correctquestion):        
        self.correctanswers.append(correctquestion)

