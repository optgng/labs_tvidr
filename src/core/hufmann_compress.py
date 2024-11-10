import heapq
from collections import defaultdict


class Node:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(data):
    frequency = defaultdict(int)
    for number in data:
        frequency[number] += 1

    priority_queue = [Node(value, freq) for value, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node is not None:
        if node.value is not None:
            codebook[node.value] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_compress(data):
    if not data:
        return {}, ""

    huffman_tree = build_huffman_tree(data)
    huffman_codes = generate_codes(huffman_tree)

    compressed_data = ''.join(huffman_codes[number] for number in data)

    return huffman_codes, compressed_data
