import streamlit as sl
from Quiz.Models import Session, Question

#run command: cd "D:\Users\jonat\Documents\Personal\Uni\Coding\Computer Science Module\Summative 2 Code"
#run command: streamlit run app.py

sl.title("Networking Fundamentals Quiz") #title on browser
sl.write()
username = sl.text_input("Enter Name: ") #get name and set to username var


# difficultylist = [1, 2, 3, 4] test
difficulty = sl.select_slider("Select Difficulty", Question.getDifficultiesAsList) #change to Question.getDifficultiesAsList