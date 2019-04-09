import clusters, data_processing

'''Import Dataset'''
data = data_processing.open_csv_file('dataset.csv')

'''Create a list of countries in the order of the similarity matrix'''
countries_list = data_processing.get_country_names(data)

'''Create numerical attributes matrix'''
attr_matrix = data_processing.create_attribute_matrix(data)
data_processing.str_to_float(attr_matrix)

'''Create Similarity Matrix'''
num_cluster=5
herro = clusters.kcluster(attr_matrix,distance=clusters.euclidean,k=num_cluster)
print ('clusters by euclidean distance')
for i in range(num_cluster):
    print ('cluster {}:'.format(i+1))
    print ([countries_list[r] for r in herro[i]])