# -*- coding: utf-8 -*-

from links import UrlLinks
from stack import Stack
from graph import Graph

def main():
    url = "http://www.dn.com"
    stack = Stack()
    index = 0

    for i in UrlLinks(url).getLinks():
        if i.startswith("http"):
            stack.push(i)

    while not stack.isEmpty():
        url = stack.pop()
        for u in UrlLinks(url).getLinks():
            if u.startswith("http"):
                print(u)
                stack.push(u)

#        if index >= 100:
#            break
#        index = index + 1


if __name__ == "__main__":
    main()