import streamlit as sl
from Quiz.Models import Session, Question
from Quiz.CSVStorage import CSVWriter

filename = "../QuizData/Questions.csv" #uplevels using .. then uses relative folder and file

#run command: cd "D:\Users\jonat\Documents\Personal\Uni\Coding\Computer Science Module\Summative 2 Code"
#run command: streamlit run app.py

csvs = CSVWriter(filename)

sl.title("Networking Fundamentals Quiz") #title on browser
sl.write()
action = sl.selectbox("Choose Action", ["Start Quiz", "Add Question"])


if "next" not in sl.session_state:
    sl.session_state.next = False

if sl.button("Confirm"):
    sl.session_state.next = True

if sl.session_state.next:

    if(action == "Add Question"):
        questiontext = sl.text_input("Enter Question Text: ", key="q")
        questiondesc = sl.text_input("Enter Topic", key="t")

        if "questionanswers" not in sl.session_state:
            questionanswers = ["", "", ""]

        for i in range(3):
            questionanswers[i] = (sl.text_input(f"Enter multi choice answer {i+1}: ", key=f"i{i}"))

        questioncorrectopt = sl.selectbox("Choose which multi choice answer is correct: ", [questionanswers[0], questionanswers[1], questionanswers[2]], key="c")


        Question.addQuestion(csvs, questiontext, questiondesc, questionanswers, questioncorrectopt)
    else:
        username = sl.text_input("Enter Name: ") #get name and set to username var
        # difficultylist = [1, 2, 3, 4] test
        difficulty = sl.select_slider("Select Difficulty", Question.getDifficultiesAsList) #change to Question.getDifficultiesAsList