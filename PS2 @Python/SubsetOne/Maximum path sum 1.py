# 18


triangleDict = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def make_tree():
    class Tree:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    bottom_list = []
    tri_dict_selector = triangleDict[-1]
    for val in tri_dict_selector:
        bottom_list.append(Tree(val))
    for row in reversed(triangleDict[:-1]):
        index = 0
        new_list = []
        for val in row:
            max_value = max((bottom_list[index]).get_value(), (bottom_list[index + 1]).get_value())
            max_value += val
            tree = Tree(max_value)
            new_list.append(tree)
            index += 1
        bottom_list = new_list.copy()
    return bottom_list[0].get_value()


def start():
    print(make_tree())
    pass


start()
