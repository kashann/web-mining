import data_sample
import pprint

def transform_prefs(prefs):
    results = {}
    for person in prefs:
        for item in prefs[person]:
            results.setdefault(item, {})
            results[item][person] = prefs[person][item]
    return results

def main():
    data = data_sample.critics
    pprint.pprint(transform_prefs(data))

if __name__ == "__main__":
    main()