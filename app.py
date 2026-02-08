import streamlit as sl
from Quiz.Models import Session, Question

#run command: cd "D:\Users\jonat\Documents\Personal\Uni\Coding\Computer Science Module\Summative 2 Code"
#run command: streamlit run app.py

sl.title("Networking Fundamentals Quiz") #title on browser
sl.write()
username = sl.text_input("Enter Name: ") #get name and set to username var


difficultylist = ["dif 1", "dif 2", "dif 3", "dif 4"]
difficulty = sl.select_slider("Select Difficulty", difficultylist) #change to Question.getDifficultiesAsList