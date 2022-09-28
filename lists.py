import pandas as pd
import csv

def gettrain(input):
        with open("trainlist.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            next(csv_reader)
            for train in csv_reader:
                if input in train[1]:
                    return str(f"vlak: {train[0]} {train[1]} {train[2]}\njede směrem: {train[3]}")

class Command:

    @classmethod
    def vypis(cls, input):
        return gettrain(input=input)