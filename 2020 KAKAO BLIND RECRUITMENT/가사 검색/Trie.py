from collections import defaultdict

class Node:
    def __init__(self, char, length=None, data=None):
        self.char = char
        self.data = None
        self.children = {}
        self.length = defaultdict(int)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head
        node.length[len(string)] += 1
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
            node.children[char].length[len(string)] += 1
            node = node.children[char]
        node.data = string

    def start_with(self, prefix, length):
        node = self.head
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node.length[length]


def solution(words, queries):
    answer = []
    front = Trie()
    back = Trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    for word in queries:
        if word == "?" * len(word):
            answer.append(front.head.length[len(word)])

        elif word[0] == "?":
            prefix = word[::-1].split("?")[0]
            answer.append(back.start_with(prefix, len(word)))
        else:
            prefix = word.split("?")[0]
            answer.append(front.start_with(prefix, len(word)))

    return answer