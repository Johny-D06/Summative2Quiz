import pytest
from Quiz.CSVStorage import CSVReader, CSVWriter
from Quiz.Models import Question
#import classes to test

testfilename = "QuizData/QuestionForTest.csv"

def testcsvreader():
    """tests that the csvreader works as intended"""

    csvr = CSVReader() #intialized
    csvr.readQuestionFromFile(filenameloc=testfilename) #csv reader reads the question and creates a question using constructor, this includes adding it to allquestions[]
    assert len(Question.allQuestions) == 1 #checks a question was made
