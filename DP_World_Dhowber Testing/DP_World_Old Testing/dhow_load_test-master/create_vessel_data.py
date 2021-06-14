#!/usr/bin/env python3


import sys
import csv
import random
import uuid

print("Start")

def append_double_quote(data):
    for dict_item in data:
        # print(dict_item)
        for key in dict_item:
            # print(key)
            text = dict_item[key]
            text = '"' + text + '"'
            dict_item[key] = text
    return data

data = []

for i in range(5):
    random_string = str(uuid.uuid4())[0:10].replace('-', '')
    data.append(
        {
            "vessel_name": random_string + "name",
            "vessel_registration": random_string + "regno",
            "port_of_origin": "IRBUZ",
            "vessel_type": "SHIP"

            
        })

data = append_double_quote(data)


keys = ["vessel_name", "vessel_registration" , "port_of_origin","vessel_type"]
filename = "vessel_details.csv"

with open(filename, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)


print("End")
