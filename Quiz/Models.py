from dataclasses import dataclass

class Question:

    allQuestions = []

    def initQuestion(self, text, answer, difficulty): #constructor to create a question, will get from csv file
        self.text = text
        self.answer = answer
        self.difficulty = difficulty #should be at least 1
        Question.allQuestions += self

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
            difficultylist += f"Difficulty {count}"

        return difficultylist




class Session:
    
    sessionQuestions = []

    def initSession(self, userdifficulty): #constructor to setup Session
        for question in Question.allQuestions: #checks through each question in existence and adds it only if the difficulty level is qual to or less than what is set
            if(question.difficulty <= userdifficulty):
                self.sessionQuestions += question

    def getScore(self):
        score = sum(2 for question in self.questions if question.checkAnswer) #adds 2 point per correct question, uses function checkAnswer to make sure each question is correct
        return score