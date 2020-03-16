from distances import pearson
from PIL import Image, ImageDraw

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        parts = line.strip().split('\t')
        rownames.append(parts[0])
        data.append([float(x) for x in parts[1:]])
    return colnames, rownames, data

class BiCluster():
    def __init__(self, vec, left = None, right = None, distance = 0.0, id = None):
        self.vec = vec
        self.left = left
        self.right = right
        self.distance = distance
        self.id = id

def print_cluster(cluster, labels = None, n = 0):
    for i in range(n):
        print(' ', end = '')
    if cluster.id < 0:
        print('-')
    else:
        if labels == None:
            print(cluster.id)
        else:
            print(labels[cluster.id])
    if cluster.left != None:
        print_cluster(cluster.left, labels = labels, n = n + 1)
    if cluster.right != None:
        print_cluster(cluster.right, labels = labels, n = n + 1)

def hcluster(rows, distance = pearson):
    distances = {}
    current_cluster_id = -1
    clusters = [BiCluster(rows[i], id = i) for i in range(len(rows))]
    while len(clusters) > 1:
        print('Current cluster vector length: ', len(clusters))
        lowest_pair = (0, 1)
        closest = distance(clusters[0].vec, clusters[1].vec)
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if (clusters[i].id, clusters[j].id) not in distances:
                    distances[(clusters[i].id, clusters[j].id)] = distance(clusters[i].vec, clusters[j].vec)
                current_distance = distances[(clusters[i].id, clusters[j].id)]
                if current_distance < closest:
                    closest = current_distance
                    lowest_pair = (i, j)
        merge_vector = [(clusters[lowest_pair[0]].vec[i] + clusters[lowest_pair[1]].vec[i]) / 2.0 for i in range(len(clusters[0].vec))]
        merged_cluster = BiCluster(merge_vector, left = clusters[lowest_pair[0]], right = clusters[lowest_pair[1]], distance = closest, id = current_cluster_id)
        current_cluster_id -= 1
        # print(len(clusters))
        # print(lowest_pair)
        del clusters[lowest_pair[1]]
        del clusters[lowest_pair[0]]
        clusters.append(merged_cluster)
    return clusters[0]

def rotate(data):
    new_data = []
    for i in range(len(data[0])):
        new_row = [data[j][i] for j in range(len(data))]
        new_data.append(new_row)
    return new_data 

def draw_dendrogram(clust, labels, jpeg = 'clusters.jpg'):
	h = get_height(clust) * 20
	w = 1200
	depth = get_depth(clust)
	scaling = float(w - 300) / depth
	img = Image.new('RGB', (w, h), (255,255,255))
	draw = ImageDraw.Draw(img)
	draw.line((0, h / 2, 10, h / 2), fill = (255,0,0))
	draw_node(draw, clust, 10, (h/2), scaling, labels)
	img.save(jpeg, 'JPEG')

def get_height(clust):
	if clust.left == None and clust.right == None:
		return 1
	return get_height(clust.left) + get_height(clust.right)

def get_depth(clust):
	if clust.left == None and clust.right == None:
		return 0
	return max(get_depth(clust.left), get_depth(clust.right)) + clust.distance

def draw_node(draw, clust, x, y, scaling, labels):
	if clust.id < 0:
		h1 = get_height(clust.left) * 20
		h2 = get_height(clust.right) * 20
		top = y - (h1 + h2) / 2
		bottom = y + (h1 + h2) / 2
		ll = clust.distance * scaling
		draw.line((x, top + h1 / 2, x, bottom - h2 / 2), fill = (255, 0, 0))
		draw.line((x, top + h1 / 2, x + ll,top + h1 / 2), fill = (255, 0, 0))
		draw.line((x, bottom - h2 / 2, x + ll, bottom - h2 / 2), fill = (255, 0, 0))
		draw_node(draw, clust.left, x + ll, top + h1 / 2, scaling, labels)
		draw_node(draw, clust.right, x + ll, bottom - h2 / 2, scaling, labels)
	else:
		draw.text((x + 5,y - 7),labels[clust.id],(0,0,0))

def main():
    colnames, rownames, data = read_file('blogdata.txt')
    cluster = hcluster(data)
    # print_cluster(cluster, labels = rownames, n = 0)
    # rotated_data = rotate(data)
    # cluster = hcluster(rotated_data)
    # print_cluster(cluster, labels = rownames, n = 0)
    draw_dendrogram(cluster, labels = rownames)

if __name__ == "__main__":
    main()