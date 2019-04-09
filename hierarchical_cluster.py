import clusters, data_processing

'''Import Dataset'''
data = data_processing.open_csv_file('dataset.csv')

'''Create a list of countries in the order of the similarity matrix'''
countries_list = data_processing.get_country_names(data)

'''Create numerical attributes matrix'''
attr_matrix = data_processing.create_attribute_matrix(data)
data_processing.str_to_float(attr_matrix)

'''hierachical clustering: euclidean distance'''
num_cluster=3
resulting_clusters = clusters.hcluster(attr_matrix,distance=clusters.euclidean)
print ('clusters by euclidean distance')
clusters.printhclust(resulting_clusters,labels=countries_list)
clusters.drawdendrogram(resulting_clusters,countries_list,jpeg='Euclidean Cluster.jpg')

'''hierachical clustering: tanimoto coefficient'''
resulting_clusters = clusters.hcluster(attr_matrix,distance=clusters.tanimoto)
print ('clusters by tanimoto coefficient')
clusters.printhclust(resulting_clusters,labels=countries_list)
clusters.drawdendrogram(resulting_clusters,countries_list,jpeg='Tanimoto Cluster.jpg')
print()

'''hierachical clustering: pearson similarity'''
resulting_clusters = clusters.hcluster(attr_matrix,distance=clusters.pearson)
print ('clusters by pearson correlation')
clusters.printhclust(resulting_clusters,labels=countries_list)
clusters.drawdendrogram(resulting_clusters,countries_list,jpeg='Pearson Cluster.jpg')

print()

'''hierachical clustering: cosine similarity'''
resulting_clusters = clusters.hcluster(attr_matrix,distance=clusters.cosine)
print ('clusters by cosine similarity')
clusters.printhclust(resulting_clusters,labels=countries_list)
clusters.drawdendrogram(resulting_clusters,countries_list,jpeg='Cosine Cluster.jpg')
