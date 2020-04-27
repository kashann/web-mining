from sample import sample
from PIL import Image, ImageDraw
import pprint

class DecisionNode(object):
    def __init__(self, col = -1, value = None, results = None, falseSubtree = None, trueSubtree = None):
        self.col = col
        self.value = value
        self.results = results
        self.falseSubtree = falseSubtree
        self.trueSubtree = trueSubtree

def unique_counts(rows):
    results = {}
    for row in rows:
        outcome = row[-1]
        results.setdefault(outcome, 0)
        results[outcome] += 1
    return results

def entropy(rows):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(rows)
    h = 0.0 # entropy
    for c in results.values():
        p = c / len(rows)
        h -= p * log2(p)
    return h

def gini_impurity(rows):
    total = len(rows)
    counts = unique_counts(rows)
    impurity = 1
    for c in counts:
        impurity -= (counts[c] / total)**2
    return impurity

def divide_set(rows, column, value):
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row: row[column] >= value
    else:
        split_function = lambda row: row[column] == value
    true_set = [row for row in rows if split_function(row)]
    false_set = [row for row in rows if not split_function(row)]
    return (false_set, true_set)

def build_tree(rows, scoref = entropy):
    if len(rows) == 0:
        return DecisionNode()
    current_score = scoref(rows)
    best_gain = 0
    best_criterion = None
    best_sets = None
    column_count = len(rows[0]) - 1
    for col in range(0, column_count):
        column_values = {}
        for row in rows:
            column_values[row[col]] = 1
        for value in column_values.keys():
            (false_set, true_set) = divide_set(rows, col, value)
            p = len(false_set) / len(rows)
            gain = current_score - p * scoref(false_set) - (1 - p) * scoref(true_set)
            if gain > best_gain and len(false_set) > 0 and len(true_set) > 0:
                best_gain = gain
                best_criterion = (col, value)
                best_sets = (false_set, true_set)
    if best_gain > 0:
        false_branch = build_tree(best_sets[0])
        true_branch = build_tree(best_sets[1])
        return DecisionNode(col = best_criterion[0], value = best_criterion[1], falseSubtree = false_branch, trueSubtree = true_branch)
    else:
        return DecisionNode(results = unique_counts(rows))

def print_tree(tree, indent = ''):
    if tree.results != None:
        print(tree.results)
    else:
        print(tree.col, ' : ', tree.value, '?')
        print(indent + 'True branch ', end = '')
        print_tree(tree.trueSubtree, indent + '    ')
        print(indent + 'False branch ', end = '')
        print_tree(tree.falseSubtree, indent + '    ')

def classify(item, tree):
    if tree.results != None:
        return tree.results
    value = item[tree.col]
    branch = None
    if isinstance(value, int) or isinstance(value, float):
        if value >= tree.value:
            branch = tree.trueSubtree
        else:
            branch = tree.falseSubtree
    else:
        if value == tree.value:
            branch = tree.trueSubtree
        else:
            branch = tree.falseSubtree
    return classify(item, branch)

def get_width(tree):
    if tree.trueSubtree == None and tree.falseSubtree == None:
        return 1
    else:
        return get_width(tree.falseSubtree) + get_width(tree.trueSubtree)

def get_height(tree):
    if tree.trueSubtree == None and tree.falseSubtree == None:
        return 0
    return 1 + max(get_height(tree.trueSubtree), get_height(tree.falseSubtree))

def draw_tree(tree, file = 'tree.jpeg'):
    w = get_width(tree) * 100
    h = get_height(tree) * 100 + 200
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_node(draw, tree, w / 2, 20)
    img.save(file, 'JPEG')

def draw_node(draw, tree, x, y):
    if tree.results == None:
        false_width = get_width(tree.falseSubtree) * 100
        true_width = get_width(tree.trueSubtree) * 100
        left = x - (true_width + false_width) / 2
        right = x + (true_width + false_width) / 2
        draw.text((x - 20, y - 10), str(tree.col) + ':' + str(tree.value), (0, 0, 0))
        draw.line((x, y, left + false_width / 2, y + 100), fill = (255, 0, 0))
        draw.line((x, y, right - true_width / 2, y + 100), fill = (0, 255, 0))
        draw_node(draw, tree.falseSubtree, left + false_width / 2, y + 100)
        draw_node(draw, tree.trueSubtree, right - true_width / 2, y + 100)
    else:
        results = ['{outcome}:{count}'.format(outcome = k, count = v) for k, v in tree.results.items()]
        text = ', '.join(results)
        draw.text((x - 20, y), text, (0, 0, 0))

def main():
    # print(entropy(sample))
    # pprint.pprint(divide_set(sample, 1, 'USA'))
    tree = build_tree(sample, scoref = gini_impurity)
    # print_tree(tree)
    result = classify(['(direct)', 'New Zealand', 'no', 12], tree)
    # print(result)
    draw_tree(tree, file = 'output.jpeg')

if __name__ == '__main__':
    main()