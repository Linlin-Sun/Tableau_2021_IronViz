import pandas as pd
import json
import csv
import sys

heaheaderding = ""
row_list = []
with open("data/data.json", "r", encoding = "utf-8") as file_handler:
    lines = file_handler.readlines()
    print(f"Line count: {len(lines)}")
    for index, line in enumerate(lines):
        try:
            line_dict = json.loads(line)
        except:
            print("Error:", sys.exc_info()[0])
        if index == 0:
            header = [key for key in line_dict.keys()]
        else:
            for i, key in enumerate(line_dict.keys()):
                if key not in header:
                    header.insert(i, key)
        row_list.append(line_dict)
with open("data/data.csv", "w") as output_handler:
    writer = csv.DictWriter(output_handler, fieldnames = header)
    writer.writeheader()
    for row_num, row in enumerate(row_list):
        try:
            writer.writerow(row)
        except:
            print("Error: row_num: ", row_num, sys.exc_info()[0])