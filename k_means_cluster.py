import clusters, data_processing

'''Import Dataset'''
data = data_processing.open_csv_file('dataset.csv')

'''Create a list of countries in the order of the similarity matrix'''
countries_list = data_processing.get_country_names(data)

'''Create numerical attributes matrix'''
attr_matrix = data_processing.create_attribute_matrix(data)
data_processing.str_to_float(attr_matrix)
