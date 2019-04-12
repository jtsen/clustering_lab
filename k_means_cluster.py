import clusters, data_processing

'''Import Dataset'''
data = data_processing.open_csv_file('dataset.csv')

'''Create a list of countries in the order of the similarity matrix'''
countries_list = data_processing.get_country_names(data)

'''Create numerical attributes matrix'''
attr_matrix = data_processing.create_attribute_matrix(data)
data_processing.str_to_float(attr_matrix)

'''k-means clustering: euclidean distance'''
num_cluster=4
resulting_clusters, centroids = clusters.kcluster(attr_matrix,distance=clusters.euclidean,k=num_cluster)
print ('clusters by euclidean distance')
print(centroids)
for i in range(num_cluster):
    print ('cluster {}:'.format(i+1))
    print ([countries_list[r] for r in resulting_clusters[i]])
    print([r for r in resulting_clusters[i]])

print()

# '''k-means clustering: tanimoto coefficient'''
# resulting_clusters, centroids = clusters.kcluster(attr_matrix,distance=clusters.tanimoto,k=num_cluster)
# print ('clusters by tanimoto coefficient')
# for i in range(num_cluster):
#     print ('cluster {}:'.format(i+1))
#     print ([countries_list[r] for r in resulting_clusters[i]])
#
# print()
#
# '''k-means clustering: pearson similarity'''
# resulting_clusters, centroids = clusters.kcluster(attr_matrix,distance=clusters.pearson,k=num_cluster)
# print ('clusters by pearson correlation')
# for i in range(num_cluster):
#     print ('cluster {}:'.format(i+1))
#     print ([countries_list[r] for r in resulting_clusters[i]])
#
# print()
#
# '''k-means clustering: cosine similarity'''
# resulting_clusters, centroids = clusters.kcluster(attr_matrix,distance=clusters.cosine,k=num_cluster)
# print ('clusters by cosine similarity')
# for i in range(num_cluster):
#     print ('cluster {}:'.format(i+1))
#     print ([countries_list[r] for r in resulting_clusters[i]])

