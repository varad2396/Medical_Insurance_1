import pickle
import json
import pandas as pd
import numpy as np

class Medical_Insurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    def load_model(self):
        with open("med_insurance.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("project_data.json", "r") as f:
            self.js = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        region_index = np.where(np.array(self.js['Columns']) == self.region)[0][0]

        test_array = np.zeros(len(self.js['Columns']))

        test_array[0] = self.age
        test_array[1] = self.js['gender'][self.gender]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.js['smoker'][self.smoker]
        test_array[region_index] = 1

        print("Test Array \n",test_array)
        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        print("predicted_charges",predicted_charges)
        return predicted_charges


