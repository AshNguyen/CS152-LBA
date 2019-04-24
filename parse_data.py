import pandas as pd 
import numpy as np

data = pd.read_csv('restaurant_data.csv')

def parse_one_restaurant(row): 
    string = "restaurant('{}') :- price('{}'), distance('{}'), cuisine_type('{}').".format(
                   str(row['Name']), str(row['Price']).lower(), \
                   str(row['Distance']).lower(), str(row['Type of Cuisine']).lower()) 

    return string

def parse_data(restaurant_data): 
    result = ""
    for _ in range(restaurant_data.shape[0]):
        result = result + " " + parse_one_restaurant(restaurant_data.iloc[_]) + "\n"
    return result

print(parse_data(data))