import csv
from pathlib import Path


class CSVWriter(): #will make in the form "question,answer,difficulty,topic"

    def __init__(self, relativefilepath):
        self.relativefilepath = relativefilepath
    
    def writeToFile(self, text): #writes in a line then moves to newline
        writer = open(self.relativefilepath, mode="a", newline="")
        writer.write(f"{text}\n")
        writer.close()

class CSVReader():

    def readQuestionFromFile(self, filenameloc):
        from Quiz.Models import Question
        with open(filenameloc, "r") as file:
            rdr = csv.reader(file)            
            for line in rdr:
                questext = line[0]
                quessubj = line[1]
                quesans = line[2:5]
                quesansnum = quesans.index(line[5])
                quesdif = int(line[6].replace("Difficulty ", "")) #remove difficulty from the line, not sure why its doing this? csv stores as 'n'?
                tempquestion = Question(text=questext, subject=quessubj, answers=quesans, correctanswer=quesansnum, difficulty=quesdif)
                #questions.append(tempquestion) #should not need to append due to the constructor on Question