def get_spam_features(filename, threshold = 0.1):
    results = []
    with open(filename + '.names') as f:
        lines = f.readlines()
        names = [line.split(':')[0] for line in lines]
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [float(item.strip()) for item in items]
            classification = items[-1]
            word_features = items[:-10]
            features = []
            for index, item in enumerate(word_features):
                if item > threshold:
                    features.append(names[index])
            result = {'features' : features, 'outcome' : 'bad' if classification == 1 else 'good'}
            results.append(result)
    return results
    
def get_features(item):
    return item['features']

def get_spam_features_sk(filename):
    results = []
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [float(item.strip()) for item in items]
            classification = items[-1]
            word_features = items[:-1]
            result = {'features' : word_features, 'outcome' : 'bad' if classification == 1 else 'good'}
            results.append(result)
    return results

def main():
    results = get_spam_features('spambase')
    print(results[:5])

if __name__ == "__main__":
    main()