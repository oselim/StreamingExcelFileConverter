import pandas as pd
import re
import os


def float_splitter(column_data):
    score_one_array = []
    score_zero_array = []
    for label, value in column_data.iteritems():
        float_numbers = re.findall(r"[-+]?\d*\.*\d+[E]?[-+]?[\d+]?", value)
        try:
            if float_numbers[0] == "1.0":
                score_one_array.append(float(float_numbers[1]))
            elif float_numbers[2] == "1.0":
                score_one_array.append(float(float_numbers[3]))
        except IndexError:
            score_one_array.append(0.0)
        try:
            if float_numbers[2] == "0.0":
                score_zero_array.append(float(float_numbers[3]))
            elif float_numbers[0] == "0.0":
                score_zero_array.append((float(float_numbers[1])))
        except IndexError:
            score_zero_array.append(0.0)
    return score_one_array, score_zero_array


excel_file_path = "C:\\Users\\selim\\PycharmProjects\\StreamingExcelFileConverter\\data\\"
excel_file_path_destination = "C:\\Users\\selim\\PycharmProjects\\StreamingExcelFileConverter\\data\\converted\\"
excel_file_extension = ".xlsx"
scores = ["Precision", "Recall", "F1 Score"]

file_list = os.listdir(excel_file_path)

if not os.path.exists(excel_file_path_destination):
    os.mkdir(excel_file_path_destination)

for file_name in file_list:
    excel_file_name = file_name.rstrip(excel_file_extension)
    data = pd.read_excel(excel_file_path + excel_file_name + excel_file_extension)
    for score in scores:
        data_score = data[score]
        data_score_one, data_score_zero = float_splitter(data_score)
        data[score + " One"] = data_score_one
        data[score + " Zero"] = data_score_zero

    data.to_excel(excel_file_path_destination + excel_file_name + "_converted" + excel_file_extension,
                  sheet_name=excel_file_name,
                  index=False)
