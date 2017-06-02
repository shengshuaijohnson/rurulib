# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yixuan Zhao <johnsonqrr (at) gmail.com>
# TODO:AC以后写篇总结
import time
BEGIN =  time.time()
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import Queue
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = {i:set() for i in wordList}   # 建立一个双向图，然后用dij可破
        all_neighbor_cases = {i:set() for i in wordList}
        all_neighbor_cases = {}
        for word in  wordList:
            for index in xrange(len(word)):
                new_word = word
                new_word = word[:index]+ '_' + word[index+1:]
                if all_neighbor_cases.get(new_word, False):
                    all_neighbor_cases[new_word].add(word)
                else:
                    all_neighbor_cases[new_word] = set([word])

        for word1 in wordList:
                for index in range(len(word1)):
                    new_word = word1[:index]+ '_' + word1[index+1:]
                    for word in all_neighbor_cases[new_word]:
                        graph[word1].add(word)
                        graph[word].add(word1)


        length = {i:len(wordList)*2 for i in wordList}
        length[beginWord] = 0
        myqueue = Queue.Queue()
        myqueue.put(beginWord)
        while not myqueue.empty():
            current_word = myqueue.get()
            current_length = length[current_word]
            for neighbor in graph[current_word]:
                if current_length + 1 < length[neighbor]:
                    length[neighbor] = current_length + 1
                    myqueue.put(neighbor)
        # print time.time() - BEGIN
        return length[endWord] + 1 if length[endWord] <= len(wordList) else 0



o = Solution()
beginWord = "lost"
endWord = "cost"
wordList = ["most","fist","lost","cost","fish"]
print o.ladderLength(beginWord, endWord, wordList)

