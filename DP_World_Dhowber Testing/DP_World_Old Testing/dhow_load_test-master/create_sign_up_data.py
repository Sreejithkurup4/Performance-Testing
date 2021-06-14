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


if len(sys.argv) < 3:
    raise Exception("Please enter Account type and row number")

account_type = sys.argv[1]
row_number = sys.argv[2]

if account_type not in ["CARR", "SHPR", "BOTH"]:
    raise Exception("Invalid account type")

try:
    row_number = int(row_number)
except:
    raise Exception("Please enter valid number")


data = []

for i in range(row_number):
    random_string = str(uuid.uuid4())[0:15].replace('-', '')
    random_number = random.randint(0, 9999999999)
    mobile_number = "".join('{0:010}'.format(random_number))
    data.append(
        {
            "business_type": "BSNS",
            "type_of_signup": "normal",
            "company_name": random_string + " Co",
            "country": "IN",
            "first_name": random_string + " F name",
            "last_name":  random_string + " L name",
            "email": random_string + "@gmail.com",
            "account_type": account_type,
            "phone_number": "+91-" + mobile_number + "0"
            
        })

data = append_double_quote(data)


keys = ["business_type", "type_of_signup", "company_name",
        "country", "first_name", "last_name", "email", "account_type", "phone_number"]
filename = "sign_up_" + account_type + "_" + str(row_number) + ".csv"

with open(filename, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)


print("End")
