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
                qtext = line[0]
                qsubj = line[1]
                qans = line[2:5]
                qansnum = qans.index(line[5])
                qdif = int(line[6].replace("Difficulty ", "")) #remove difficulty from the line, not sure why its doing this? csv stores as 'n'?
                tempquestion = Question(text=qtext, subject=qsubj, answers=qans, answernum=qansnum, difficulty=qdif)
                #questions.append(tempquestion) #should not need to append due to the constructor on Question