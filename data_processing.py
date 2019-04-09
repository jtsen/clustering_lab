import csv, clusters, copy

'''PARAMETERS: path -> csv file path'''
def open_csv_file(path):
    data = []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append(list(row))
    return data


'''Convert strings to floats'''
def str_to_float(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] = float(data[row][col])
    return data


'''Create a list of country names'''
def get_country_names(data):
    countries = []
    for row in data:
        countries.append([row[0],row[1]])
    return countries


'''Remove non-numerical columns'''
def create_attribute_matrix(data):
    attr_matrix = copy.deepcopy(data)
    del attr_matrix[0]
    for row in attr_matrix:
        del row[0:2]
        del row[-1]
    return attr_matrix