import streamlit as sl
from Quiz.Models import Session, Question
from Quiz.CSVStorage import CSVWriter

filename = "../QuizData/Questions.csv" #uplevels using .. then uses relative folder and file

#run command: cd "D:\Users\jonat\Documents\Personal\Uni\Coding\Computer Science Module\Summative 2 Code"
#run command: streamlit run app.py

csvs = CSVWriter.initCSVWriter(relativefilepath=filename)

sl.title("Networking Fundamentals Quiz") #title on browser
sl.write()
action = sl.selectbox("Choose Action", ["Start Quiz", "Add Question"])
if(action == "Add Question"):
    Question.addQuestion(csvs)

username = sl.text_input("Enter Name: ") #get name and set to username var


# difficultylist = [1, 2, 3, 4] test




difficulty = sl.select_slider("Select Difficulty", Question.getDifficultiesAsList) #change to Question.getDifficultiesAsList