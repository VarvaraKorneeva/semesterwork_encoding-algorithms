def read_file(filename):
    with open(filename, "r") as f:
        alph = f.readline()
        if alph[-1] == "\n":
            alph = alph[:-1:]
        alph = alph.split(" ")
        prob = f.readline()
        if prob[-1] == "\n":
            prob = prob[:-1:]
        prob = prob.split(" ")
        if ',' in prob[0]:
            prob = [x.replace(',', '.') for x in prob]
        try:
            prob = [float(x) for x in prob]
        except ValueError:
            print("Not correct alphabet")
            exit()
        if sum(prob) != 1:
            print("Not correct alphabet")
            exit()

    return alph, prob


def get_dict(alph_list, prob_list):
    alph = {}
    for i in range(len(alph_list)):
        alph[alph_list[i]] = prob_list[i]

    return alph


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self, alph: dict):
        self.alph = alph
        self.leaves = [Node(k, v) for k, v in alph.items()]
        while len(self.leaves) != 1:
            self.leaves.sort(key=lambda item: item.value, reverse=True)
            node = Node(value=(self.leaves[-1].value + self.leaves[-2].value))
            node.lchild = self.leaves.pop(-1)
            node.rchild = self.leaves.pop(-1)
            self.leaves.append(node)
        self.root = self.leaves[0]

    def decode_huffman(self, bin_code):
        curr_node = self.root
        result = ""
        for el in bin_code:
            if curr_node.key is not None:
                result += curr_node.key
                curr_node = self.root
                continue
            if el == "0":
                curr_node = curr_node.lchild
            elif el == "1":
                curr_node = curr_node.rchild

        return result


if __name__ == '__main__':
    alphabet, probabilities = read_file("alphabet_for_huf.txt")
    alph_dict = get_dict(alphabet, probabilities)
    tree = Tree(alph_dict)
    bin_str = input()
    if bin_str == "":
        print("Not correct string")
        exit()
    result = tree.decode_huffman(bin_str)
    print(result)
