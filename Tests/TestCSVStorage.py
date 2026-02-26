import pytest
from Quiz.CSVStorage import CSVReader, CSVWriter
from Quiz.Models import Question
#import classes to test

testfilename = "QuizData/QuestionForTest.csv"

def testcsvreader():
    csvr = CSVReader(testfilename) #intialized
    csvr.readQuestionFromFile() #csv reader reads the question and creates a question using constructor, this includes adding it to allquestions[]
    assert Question.allQuestions.count() == 1 #checks a question was made