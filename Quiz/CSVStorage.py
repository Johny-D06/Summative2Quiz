import csv
from pathlib import Path

class CSVWriter():

    def initCSVWriter(self, relativefilepath):
        self.relativefilepath = relativefilepath
    
    def writeToFile(self):
        open(self.relativefilepath, "w", newline="")