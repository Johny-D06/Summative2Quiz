import pytest
from Quiz.Models import Question, Session

def test_CheckAnswer():
    """checks that the marking works"""

    question = Question("null", "null", ["null", "null", "correct"], "correct", "-1") # use 2, ref starts at 0
    assert question.checkAnswer("correct") == True

def test_GetMaxDifficulty():
    """checks getting max difficulty works"""

    question = Question("null", "null", ["null", "null", "null"], "null", "2") #null as not relevant
    assert Question.getMaxDifficulty() == 2