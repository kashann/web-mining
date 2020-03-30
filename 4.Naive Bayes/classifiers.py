import util

class Classifier(object):
    def __init__(self, get_features):
        self.get_features = get_features
        self.category_count = {}
        self.feature_count = {}
    def increment_feature(self, feature, category):
        self.feature_count.setdefault(feature, {})
        self.feature_count[feature].setdefault(category, 0)
        self.feature_count[feature][category] += 1
    def increment_category(self, category):
        self.category_count.setdefault(category, 0)
        self.category_count[category] += 1
    def get_total_count(self):
        return sum(self.category_count.values())
    def get_category_count(self, category):
        if category in self.category_count:
            return self.category_count[category]
        return 0
    def get_feature_count(self, feature, category):
        if feature in self.feature_count and category in self.feature_count[feature]:
            return self.feature_count[feature][category]
        return 0
    def get_categories(self):
        return self.category_count.keys()
    def train(self, item, category):
        features = self.get_features(item)
        for feature in features:
            self.increment_feature(feature, category)
        self.increment_category(category)
    def feature_probability(self, feature, category):
        if self.get_category_count(category) == 0:
            return 0
        return self.get_feature_count(feature, category) / self.get_category_count(category)

class NaiveBayesClassifier(Classifier):
    def __init__(self, get_features):
        Classifier.__init__(self, get_features)
        self.thresholds = {}
    def set_threshold(self, category, threshold):
        self.thresholds[category] = threshold
    def get_message_probability(self, item, category):
        features = self.get_features(item)
        p = 1
        for feature in features:
            p *= self.feature_probability(feature, category)
        return p
    def get_classifier_value(self, item, category):
        category_probability = self.get_category_count(category) / self.get_total_count()
        message_probability = self.get_message_probability(item, category)
        return category_probability * message_probability
    def classify(self, item):
        max_probability = 0
        best_category = None
        for category in self.get_categories():
            classifier_value = self.get_classifier_value(item, category)
            if classifier_value > max_probability:
                max_probability = classifier_value
                best_category = category
        return best_category
        
def main():
    messages = util.get_spam_features('spambase')
    test_set = messages[:460]
    training_set = messages[460:]
    classifier = NaiveBayesClassifier(util.get_features)
    for item in training_set:
        classifier.train(item, item['outcome'])
    correct = 0
    total = 0
    for item in test_set:
        result = classifier.classify(item)
        if item['outcome'] == result:
            correct += 1
        total += 1
    print('correct/incorrect/total: ', correct, '/', total - correct, '/', total)

if __name__ == "__main__":
    main()