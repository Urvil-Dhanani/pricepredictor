import pandas as pd

custom_data_input_dict = {
                'carat':5,
                'depth':6,
                'table':7,
                'x':[4],
                'y':[2],
                'z':[1],
                'cut':["cct"],
                'color':["cclr"],
                'clarity':["cclari"]
                }

df = pd.DataFrame(custom_data_input_dict)
print(df)