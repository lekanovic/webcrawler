# -*- coding: utf-8 -*-

from links import UrlLinks
from stack import Stack
from graph import Graph


def main():
    url = "http://www.google.com"
    stack = Stack()
    graph = Graph()
    graph.addVertex(url)
    index = 0

    for i in UrlLinks(url).getLinks():
        stack.push(i)
        graph.addVertex(i)
        graph.addEdge(url, i, 0)

    while not stack.isEmpty():
        url = stack.pop()
        graph.addVertex(url)

        for u in UrlLinks(url).getLinks():
            stack.push(u)
            graph.addVertex(u)
            graph.addEdge(url, u, 0)

        if index >= 10:
            break
        index = index + 1

    for v in graph:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

if __name__ == "__main__":
    main()