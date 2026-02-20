import streamlit as sl
from Quiz.Models import Session, Question
from Quiz.CSVStorage import CSVWriter

filename = "QuizData/Questions.csv" #uplevels using .. then uses relative folder and file

#run command: cd "D:\Users\jonat\Documents\Personal\Uni\Coding\Computer Science Module\Summative 2 Code"
#run command: streamlit run app.py

if "beginquiz" not in sl.session_state:
            sl.session_state.beginquiz = False

csvs = CSVWriter(filename)
Question.allQuestions = []
Question.loadAllQuestions(filename)

sl.title("Networking Fundamentals Quiz") #title on browser
sl.write()
action = sl.selectbox("Choose Action", ["Start Quiz", "Add Question"])


if "next" not in sl.session_state:
    sl.session_state.next = False

if "addq" not in sl.session_state:
    sl.session_state.addq = False

if sl.button("Confirm"):
    sl.session_state.next = True

if sl.session_state.next:

    if(action == "Add Question"):
        questiontext = sl.text_input("Enter Question Text: ", key="q")
        questiondesc = sl.text_input("Enter Topic", key="t")

        if "questionanswers" not in sl.session_state:
            sl.session_state.questionanswers = ["", "", ""]

        for i in range(3):
            sl.session_state.questionanswers[i] = (sl.text_input(f"Enter multi choice answer {i+1}: ", key=f"i{i}"))

        questioncorrectopt = sl.selectbox("Choose which multi choice answer is correct: ", [sl.session_state.questionanswers[0], sl.session_state.questionanswers[1], sl.session_state.questionanswers[2]], key="c")

        difficulties = [1, 2, 3, 4]
        questiondifficulty = sl.select_slider("Difficulty", difficulties)

        if (sl.button("Add Question")):
            sl.session_state.addq = True

        if (sl.session_state.addq):
            sl.session_state.addq = False
            Question.addQuestion(csvs, questiontext, questiondesc, sl.session_state.questionanswers, questioncorrectopt, questiondifficulty)    
            sl.success
        
    else:
        #username = sl.text_input("Enter Name: ") #get name and set to username var
        # difficultylist = [1, 2, 3, 4] test

        #if "beginquiz" not in sl.session_state:
        #    sl.session_state.beginquiz = False

        #selecteddifficulty = 0

        if not sl.session_state.beginquiz:
            name = sl.text_input("Enter Name")
            selecteddifficulty = sl.select_slider("Select Difficulty", Question.getDifficultiesAsList()) #change to Question.getDifficultiesAsList 

            if sl.button("Begin Quiz"):
                sl.session_state.beginquiz = True
                sl.session_state.selecteddifficulty = selecteddifficulty
        else:            

            if "session" not in sl.session_state:
                sl.session_state.session = Session(sl.session_state.selecteddifficulty)

            CurrentSession = sl.session_state.session
            
            if ("questionindex" not in sl.session_state):
                sl.session_state.questionindex = 0


            if sl.session_state.questionindex >= len(CurrentSession.sessionQuestions):
                #sl.write(f"lentest: {len(CurrentSession.sessionQuestions)}") #debug purposes
                #sl.write(f"lentest: {len(Question.allQuestions)}") #debug purposes
                sl.write("Quiz Over")
                sl.write("")
                sl.write("Correct answers:")
                for q in CurrentSession.correctanswers: #grabs all correct answers
                    sl.write(f"{q.text} | {q.answer}") #writes all questions and answers that were correct
                
                sl.session_state.beginquiz = False
                sl.stop()

            currentquestion = CurrentSession.sessionQuestions[sl.session_state.questionindex] #local var set to the session var
            sl.write(currentquestion.text) #writes q out
            useranswer = sl.radio("Choose", currentquestion.answers) #selection box for the answers
            if(useranswer == currentquestion.answernum): # answer correct
                CurrentSession.addCorrectQuestion(CurrentSession.sessionQuestions[sl.session_state.questionindex])


            if sl.button("Next Question"): #shows button for next question
                sl.session_state.questionindex += 1 #increments to the next question in the active session
                sl.rerun()
                