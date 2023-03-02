import pandas as pd
import json

df = pd.read_csv('dataset.csv')

def __df_to_json(dataframe):
    json_obj = json.loads(dataframe.to_json())
    dict_keys = list(json_obj.keys())
    json_list = []

    for index in range(len(json_obj[dict_keys[0]])):
        row_obj = dict()
        for column in dict_keys:
            row_obj[column] = json_obj[column][str(index)]
        json_list.append(row_obj)
        
    return json_list