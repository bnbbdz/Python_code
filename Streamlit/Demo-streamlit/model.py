import numpy as np

class IncomePrediction:
    def __init__(self):
        pass

    def predict(self, name:str, age:int, occupation:str):
        seed = len(name) + age + len(occupation)
        np.random.seed(seed)
        return np.random.randint(500, 5000)