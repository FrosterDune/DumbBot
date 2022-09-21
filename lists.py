import pandas as pd
import numpy as np

def gettrain(input: int):

    df = pd.read_csv("trainlist.csv", encoding="windows 1250", delimiter=";")
    specifictrain = df[df.eq(input).any(1)]
    return str(specifictrain.to_string(index=False, header=False, na_rep=" "))

class Command:

    @classmethod
    def vypis(cls, input):
        return gettrain(input=input)