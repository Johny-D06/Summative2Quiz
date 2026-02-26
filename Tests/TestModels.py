import pytest
from Quiz.Models import Question, Session

def testcheckanswer():
    """checks that the marking works"""
    question = Question("null", "null", ["null", "null", "correct"], 3, "-1")
    assert question.checkAnswer(useranswer="correct") == True

def testgetmaxdifficulty():
    question = Question("null", "null", ["null", "null", "null"], -1, "2")
    Question.allQuestions.append(question)
    assert Question.getMaxDifficulty() == 2