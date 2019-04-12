import clusters, data_processing

'''Import Dataset'''
data = data_processing.open_csv_file('dataset.csv')

'''Create a list of countries in the order of the similarity matrix'''
countries_list = data_processing.get_country_names(data)

'''Create numerical attributes matrix'''
attr_matrix = data_processing.create_attribute_matrix(data)
data_processing.str_to_float(attr_matrix)

results = [['Country/Region', 'Cluster']]

herro = clusters.bisect_k_means(attr_matrix, k=5)
for i in range(5):
    print ('cluster {}:'.format(i+1))
    print ([countries_list[r] for r in herro[i]])
    print([r for r in herro[i]])
    for j in herro[i]:
        results.append([countries_list[j],i+1])

clusters.results_to_js(results)


