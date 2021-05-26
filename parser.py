# Import `load_workbook` module from `openpyxl`
import regex as regex
from openpyxl import load_workbook
import pandas
import json_parser


# Load in the workbook
wb = load_workbook('./NBS_Office_Packages.xlsx')
sheet_list = wb.get_sheet_names()

def find_sheet(sheet_name):
    r ="(" + str(sheet_name) + ")"
    for sheet in sheet_list:
        if len(regex.findall(r, sheet)) > 0:
            return sheet

sheet = find_sheet(952)

excel_data_df = pandas.read_excel('NBS_Office_Packages.xlsx', sheet_name=sheet)
print(excel_data_df.to_dict())
# re ="\'(" + str(234) + ")\'"
# print(re)  "CNVR-37650.json"

print(json_parser.find_catalogId("CNVR-37650.json"))