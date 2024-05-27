import os
import pickle

model_path = os.path.join("artifacts", "model.pkl")

with open(model_path, "rb") as file_obj:
    model = pickle.load(file_obj)

print(model.predict())
