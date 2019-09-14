import collections
from random import choice
from string import ascii_lowercase
import argparse
import timeit


class TrieNode:

    """
        This is the Trie Node class
    """

    def __init__(self):
        """
            The constructor of the TrieNode class
        """

        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    """
        This is a Trie data structure class
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """

        :param word: It takes each word from the input file as a argument
        :return:
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True


class Puzzle(object):
    def findWords(self, grid, filepath):
        """
        Find word function returns valid words in a grid

        :param grid: it is 2D matrix
        :param filepath: The path of the input file consisting of various words
        :return: List of valid words
        """
        trie = Trie()
        node = trie.root
        res = []

        with open(filepath) as f:
            for line in f:
                for w in line.split():
                    trie.insert(w)

        # Start time
        start = timeit.default_timer()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, node, i, j, "", res)
        # End time
        stop = timeit.default_timer()
        print('Time in sec: ', stop - start)

        return res

    def dfs(self, grid, node, i, j, path, res):

        """
        This function does a DFS to look for the valid words

        :param grid: its a 2D matrix
        :param node: a Trie Node
        :param i: i is the row number in the grid
        :param j: j is the column number in the grid
        :param path: The path of the input file consisting of various words
        :param res: List of valid words
        :return: None
        """

        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        tmp = grid[i][j]
        node = node.children.get(tmp)

        if not node:
            return
        grid[i][j] = "#"

        ri = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        ci = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        for k in range(9):
            self.dfs(grid, node, i + ri[k], j + ci[k], path + tmp, res)

        grid[i][j] = tmp


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word Puzzle')

    parser.add_argument('-r', action="store", dest='rows', type=int, help='Number of rows')
    parser.add_argument('-c', action="store", dest='columns', type=int, help='Number of columns')
    parser.add_argument('-f', action="store", dest='filePath', help='File containing all the words')

    # call python main.py -r <value> -c <value> -f <path>

    results = parser.parse_args()

    print('number of rows     =', results.rows)
    print('number of columns     =', results.columns)
    print('path of file containing words     =', results.filePath)

    M = results.rows
    N = results.columns
    filepath = results.filePath

    board = [[choice(ascii_lowercase) for i in range(M)] for j in range(N)]
    print(board)
    print('\n')

    res = Puzzle().findWords(board, filepath)
    print('Resultant words are: ', res)
