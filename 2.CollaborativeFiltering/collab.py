import data_sample
import distances
import transform
import pprint

def top_matches(prefs, me, n = 5, similarity = distances.euclidean):
    scores = [(similarity(prefs, me, other), other) for other in prefs if other != me]
    scores.sort()
    scores.reverse()
    return scores[:n]

def get_recommendations(prefs, me, n = 5, similarity = distances.euclidean):
    totals = {}
    similarity_sums = {}
    for other in prefs:
        if other == me:
            continue
        sim = similarity(prefs, me, other)
        if sim == 0:
            continue
        for item in prefs[other]:
            if item not in prefs[me]:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                similarity_sums.setdefault(item, 0)
                similarity_sums[item] += sim
    rankings = [(total / similarity_sums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[:n]

def get_similar_items(prefs, item_data, n = 5, similarity = distances.euclidean):
    results = {}
    for item in item_data:
        scores = top_matches(item_data, item, similarity = similarity)
        results[item] = scores
    return results

def get_recommended_items(prefs, item_similarities, me):
    my_ratings = prefs[me]
    scores = {}
    totals = {}
    for item, rating in my_ratings.items():
        for sim, other_item in item_similarities[item]:
            if other_item in my_ratings:
                continue
            scores.setdefault(other_item, 0)
            scores[other_item] += sim * rating
            totals.setdefault(other_item, 0)
            totals[other_item] += sim
    rankings = [(score / totals[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

def main():
    data = data_sample.critics
    pprint.pprint(top_matches(data, 'Lisa Rose'))
    print()
    pprint.pprint(get_recommendations(data, 'Toby'))
    print()
    item_data = transform.transform_prefs(data)
    pprint.pprint(top_matches(item_data, 'Superman Returns'))
    print()
    item_similarities = get_similar_items(data, item_data)
    pprint.pprint(get_recommended_items(data, item_similarities, 'Toby'))

if __name__ == "__main__":
    main()