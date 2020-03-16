from distances import pearson
import random

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

def kcluster(rows, distance = pearson, k = 4):
    last_matches = None
    intervals = [(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]
    clusters = [[intervals[i][0] + random.random() * (intervals[i][1] - intervals[i][0]) for i in range(len(rows[0]))] for j in range(k)]
    MAX_EPOCHS = 10
    for t in range(MAX_EPOCHS):
        print('epoch: ', t)
        best_matches = [[] for i in range(k)]
        for j in range(len(rows)):
            current_row = rows[j]
            best_match = 0
            for i in range(k):
                d = distance(clusters[i], current_row)
                if d < distance(clusters[best_match], current_row):
                    best_match = i
            best_matches[best_match].append(j)
        if best_matches == last_matches:
            break
        for i in range(k):
            avgs = [0.0] * len(rows[0])
            if len(best_matches[i]) > 0:
                for row_id in best_matches[i]:
                    for m in range(len(rows[row_id])):
                        avgs[m] += rows[row_id][m]
                for j in range(len(avgs)):
                    avgs[j] /= len(best_matches[i])
                clusters[i] = avgs
    return best_matches

def main():
    colnames, rownames, data = read_file('blogdata.txt')
    clusters = kcluster(data)
    for k in range(4):
        print('CLUSTER ', k)
        print([rownames[row] for row in clusters[k]])

if __name__ == "__main__":
    main()