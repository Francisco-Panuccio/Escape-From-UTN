import re

def format_function(data_list):
    result = re.sub("},", "\n", data_list)
    result = re.sub("\[|\]", "", result)
    result = re.sub("\{|\}", "", result)
    result = re.sub(" ", "", result)
    result = re.sub(",", "\n", result)
    result = re.sub("6'", "6'\n", result)
    result = re.sub("'", "", result)
    result = re.sub(":", ": ", result)
    return result