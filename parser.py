import regex
from openpyxl import load_workbook
import pandas
import json_parser, find_in_string

# string = "CNVR-37458 LBO_AU_150_1 Google_50DL_HD/DL-BAS/SM/LM/ICI/NM (POC ann)"
# string = "CNVR-37461 LBO_AU_148_1 RC_Phone_20DL_HD/DL-HDSK/LR (POC/inv mon)"
string = "CNVR-37461 LBO_AU_148_1 RC_Phone_20DL_HD/DL-HDSK/LR (POC/inv mon)"
number_test = find_in_string.find_number_test(string)
number_flow = find_in_string.find_number_flow(string)
name_test = find_in_string.replace_character(string)
print(name_test)
name_json = "CNVR-" + number_test +".json"

wb = load_workbook('./NBS_Office_Packages.xlsx')
sheet_list = wb.get_sheet_names()

def find_sheet(sheet_name):
    r ="(" + str(sheet_name) + ")"
    for sheet in sheet_list:
        if len(regex.findall(r, sheet)) > 0:
            return sheet

sheet = find_sheet(number_flow)
excel_data_df = pandas.read_excel('NBS_Office_Packages.xlsx', sheet_name=sheet)

def find_data(x):
    x_list = [find_in_string.find_number_user(string)]
    x_list.append(list(x))
    if (len(excel_data_df[excel_data_df['Unnamed: 3'] == x[0]]['Common Package Properties']) > 0):
        x_list.append(excel_data_df[excel_data_df['Unnamed: 3'] == x[0]]['Common Package Properties'].values[0])
        price_all = excel_data_df[excel_data_df['Unnamed: 3'] == x[0]]['Unnamed: 4'].values[0]
        x_list.append(price_all)
        return x_list
    else:
        return 0

def wrapLines(line_length, words):
    print("---")
    for i in range(0, len(str(words)), line_length):
        print(str(words)[i:i + line_length])

json_parser.add_info(name_json)
data_list = json_parser.find_catalogId(name_json)
for data in data_list[0]:
    wrapLines(150, find_data(data))

print(json_parser.full_data(name_json, string))