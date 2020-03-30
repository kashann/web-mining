from sklearn.naive_bayes import GaussianNB
import util

def main():
    messages = util.get_spam_features_sk('spambase')
    test_data = messages[:460]
    training_data = messages[460:]
    training_inputs = [item['features'] for item in training_data]
    training_outputs = [item['outcome'] for item in training_data]
    classifier = GaussianNB()
    classifier = classifier.fit(training_inputs, training_outputs)
    test_inputs = [item['features'] for item in test_data]
    test_outputs = [item['outcome'] for item in test_data]
    predicted = classifier.predict(test_inputs)
    correct = len([item for item in zip(test_outputs, predicted) if item[0] == item[1]])
    total = len(test_data)
    print('correct/incorrect/total: ', correct, '/', total - correct, '/', total)

if __name__ == "__main__":
    main()