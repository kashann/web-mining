from math import sqrt
import statistics
import pprint

def euclidean(v1, v2):
    sum_sq = sum([(x - y) ** 2 for (x, y) in zip(v1, v2)])
    return 1 / (1 + sqrt(sum_sq))

def pearson(v1, v2):
    v1_mean = statistics.mean(v1)
    v2_mean = statistics.mean(v2)
    v1_stdev = statistics.pstdev(v1, mu = v1_mean)
    v2_stdev = statistics.pstdev(v2, mu = v2_mean)
    covariance = sum([(x - v1_mean) * (y - v2_mean) for (x, y) in zip(v1, v2)]) / len(v1)
    return covariance / (v1_stdev * v2_stdev)

def tanimoto(v1, v2):
    shared = [item for item in v1 if item in v2]
    return len(shared)

def main():
    sampleVector1 = [1,2,3,4,5,6]
    sampleVector2 = [3,4,5,6,7,8]
    pprint.pprint(euclidean(sampleVector1, sampleVector2))
    pprint.pprint(pearson(sampleVector1, sampleVector2))
    pprint.pprint(tanimoto(sampleVector1, sampleVector2))

if __name__ == "__main__":
    main()