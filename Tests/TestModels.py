import pytest
from Quiz.Models import Question, Session

def testcheckanswer():
    """checks that the marking works"""

    question = Question("null", "null", ["null", "null", "correct"], "correct", "-1") # use 2, ref starts at 0
    assert question.checkAnswer(useranswer="correct") == True

def testgetmaxdifficulty():
    """checks getting max difficulty works"""

    question = Question("null", "null", ["null", "null", "null"], "null", "2") #null as not relevant
    assert Question.getMaxDifficulty() == 2