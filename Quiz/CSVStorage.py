import csv
from pathlib import Path

class CSVWriter(): #will make in the form "question,answer,difficulty,topic"

    def initCSVWriter(self, relativefilepath):
        self.relativefilepath = relativefilepath
    
    def writeToFile(self, text): #writes in a line then moves to newline
        writer = open(self.relativefilepath, mode="a", newline="")
        writer.write(f"{text}\n")
        writer.close()
        