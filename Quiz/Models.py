from dataclasses import dataclass
from Quiz.CSVStorage import CSVWriter

class Question:

    allQuestions = []

    def __init__(self, text, subject, answers, answernum): #constructor to create a question, will get from csv file
        self.text = text
        self,subject
        self.answers = answers
        self.answernum = answernum
        #self.difficulty = difficulty #should be at least 1
        Question.allQuestions.append(self)

    def checkAnswer(self, useranswer): # returns a bool true if correct false if otherwise
        if(useranswer == self.answer):
            return True
        else:
            return False

    
    def  getMaxDifficulty(): #checks every question to get the highest difficulty rating
        temp = 0
        for question in Question.allQuestions:
            if question.difficulty > 0:
                temp = question.difficulty
        return temp
    
    def getDifficultiesAsList(): #will add each difficulty option to a list for a streamlit cmd to look at
        difficultylist = []

        count = 0
        while difficultylist.count() < Question.getMaxDifficulty(): #adds a number to the list
            count += 1
            difficultylist.append(f"Difficulty {count}")

        return difficultylist
    
    def addQuestion(csvs: CSVWriter, questiontext, questionsubject, questionanswers, questionanswernum):
        csvs.writeToFile(f"{questiontext},{questionsubject},{questionanswers[0]},{questionanswers[1]},{questionanswers[2]},{questionanswernum}")
        temp = Question(text=questiontext, )
        




class Session:
    
    sessionQuestions = []

    def initSession(self, userdifficulty): #constructor to setup Session
        for question in Question.allQuestions: #checks through each question in existence and adds it only if the difficulty level is qual to or less than what is set
            if(question.difficulty <= userdifficulty):
                self.sessionQuestions += question

    def getScore(self):
        score = sum(2 for question in self.questions if question.checkAnswer) #adds 2 point per correct question, uses function checkAnswer to make sure each question is correct
        return score